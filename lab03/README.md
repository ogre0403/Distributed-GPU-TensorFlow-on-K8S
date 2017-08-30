## Run distributed Tensorflow in multiple Pods

According to [ClusterSpec](https://github.com/ogre0403/Distributed-GPU-TensorFlow-on-K8S/blob/cd074f2d5d8c64126752e06971b7a3cff1421b77/lab03/bg_dist.py#L5)  in this example, we have one parameter server  and two workers. These servers are launched in seperated Pods. 
```bash
$ kubectl create -f ps0.yml
$ kubectl create -f worker0.yml
$ kubectl create -f worker1.yml
```

Because workers are configured as  [Job](https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/), Job will be compete. Use `--show-all` to display completed Pod.
```bash
$ kubectl get pod --show-all
NAME                   READY     STATUS      RESTARTS   AGE
ps0-3586931332-7zh2x   1/1       Running     0          3m
worker0-vrmmm          0/1       Completed   0          3m
worker1-gpjkf          0/1       Completed   0          3m
```

Let's check output of each Pod. 
```bash
$ kubectl logs worker0-vrmmm
...
步驟: 36399, loss: 70.5243148804
步驟: 36499, loss: 70.4399795532
步驟: 36599, loss: 70.3558349609
步驟: 36699, loss: 70.2718963623
步驟: 36799, loss: 70.1881408691
步驟: 36899, loss: 70.1045303345
步驟: 36999, loss: 70.021156311
步驟: 37099, loss: 69.9379501343

$ kubectl logs worker1-gpjkf
...
步驟: 32898, loss: 70.9882125854
步驟: 33098, loss: 70.8080062866
步驟: 33297, loss: 70.6313705444
步驟: 33498, loss: 70.4501571655
步驟: 33698, loss: 70.272567749
步驟: 33899, loss: 70.0951843262
步驟: 34100, loss: 69.9206085205
```
Finally, delete all Pods. 
```bash
$ kubectl delete -f ps0.yml
$ kubectl delete -f worker0.yml
$ kubectl delete -f worker1.yml
```