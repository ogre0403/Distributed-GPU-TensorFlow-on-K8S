## Run pseudo-distributed Tensorflow in single Pod
```bash
$ kubectl create -f pseudo-distributed.yml
```
According to [ClusterSpec](https://github.com/ogre0403/Distributed-GPU-TensorFlow-on-K8S/blob/048c9a1c1792bc7aaff0b843cd8e94daefa795fb/lab02/bg_dist.py#L15) in this example, we have one parameter server  and two workers.  We  create 3 ssh sessions and launch each manually. 
In SSH  session 1: 
```bash
$ kubectl exec -ti pseudo-distributed /bin/bash
root@pseudo-distributed:/$ python /opt/bg_dist.py --job_name=ps --task_index=0
...
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:200] Initialize GrpcChannelCache for job ps -> {0 -> localhost:2222}
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:200] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2223, 1 -> localhost:2224}
I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:221] Started server with target: grpc://localhost:2222
```
In SSH session 2: 
```bash
$ kubectl exec -ti pseudo-distributed /bin/bash
root@pseudo-distributed:/$  python /opt/bg_dist.py --job_name=worker --task_index=0
...
步驟: 29686, loss: 70.861618042
步驟: 29885, loss: 70.673828125
步驟: 30085, loss: 70.4847793579
步驟: 30285, loss: 70.2967453003
步驟: 30484, loss: 70.111907959
步驟: 30684, loss: 69.9257965088
```
In SSH  session 3: 
```bash
$ kubectl exec -ti pseudo-distributed /bin/bash
root@pseudo-distributed:/$ python /opt/bg_dist.py --job_name=worker --task_index=1
...
步驟: 37398, loss: 70.4796524048
步驟: 37498, loss: 70.3968429565
步驟: 37598, loss: 70.314239502
步驟: 37698, loss: 70.231803894
步驟: 37798, loss: 70.1495361328
步驟: 37898, loss: 70.0674819946
步驟: 37998, loss: 69.9855728149
```
Finally, delete the Pod
```bash
$ kubectl delete -f pseudo-distributed.yml
```