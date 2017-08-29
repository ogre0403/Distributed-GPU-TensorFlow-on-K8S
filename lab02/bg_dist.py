# coding=utf-8
import tensorflow as tf
import numpy as np

parameter_servers = ["localhost:2222"]
workers = ["localhost:2223","localhost:2224"]

tf.app.flags.DEFINE_string("job_name", "", "輸入 'ps' 或是 'worker'")
tf.app.flags.DEFINE_integer("task_index", 0, "Job 的任務 index")
FLAGS = tf.app.flags.FLAGS


def main(_):

    cluster = tf.train.ClusterSpec({"ps": parameter_servers, "worker": workers})
    server = tf.train.Server(cluster,job_name=FLAGS.job_name,task_index=FLAGS.task_index)

    if FLAGS.job_name == "ps":
        server.join()
    elif FLAGS.job_name == "worker":

        train_X = np.linspace(-1.0, 1.0, 100)
        train_Y = 2.0 * train_X + np.random.randn(*train_X.shape) * 0.33 + 10.0

        X = tf.placeholder("float")
        Y = tf.placeholder("float")

        # Assigns ops to the local worker by default.
        with tf.device(tf.train.replica_device_setter(
                worker_device="/job:worker/task:%d" % FLAGS.task_index,
                cluster=cluster)):

            w = tf.Variable(0.0, name="weight")
            b = tf.Variable(0.0, name="bias")
            # 損失函式，用於描述模型預測值與真實值的差距大小，常見為`均方差(Mean Squared Error)`
            loss = tf.square(Y - tf.multiply(X, w) - b)

            global_step = tf.Variable(0)

            train_op = tf.train.AdagradOptimizer(0.01).minimize(
                loss, global_step=global_step)

            saver = tf.train.Saver()
            summary_op = tf.summary.merge_all()
            init_op = tf.global_variables_initializer()


        # 建立 "Supervisor" 來負責監督訓練過程
        sv = tf.train.Supervisor(is_chief=(FLAGS.task_index == 0),
                                 logdir="/tmp/train_logs",
                                 init_op=init_op,
                                 summary_op=summary_op,
                                 saver=saver,
                                 global_step=global_step,
                                 save_model_secs=600)

        with sv.managed_session(server.target) as sess:
            loss_value = 100
            while not sv.should_stop() and loss_value > 70.0:
                # 執行一個非同步 training 步驟.
                # 若要執行同步可利用`tf.train.SyncReplicasOptimizer` 來進行
                for (x, y) in zip(train_X, train_Y):
                    _, step = sess.run([train_op, global_step],
                                       feed_dict={X: x, Y: y})

                loss_value = sess.run(loss, feed_dict={X: x, Y: y})
                print("步驟: {}, loss: {}".format(step, loss_value))

        sv.stop()


if __name__ == "__main__":
    tf.app.run()
