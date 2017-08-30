## Run distributed GPU Tensorflow in multiple Pods

This example is identical to [lab3](https://github.com/ogre0403/Distributed-GPU-TensorFlow-on-K8S/tree/master/lab03) except enabling GPU support. Each Pod only [require one GPU](https://github.com/ogre0403/Distributed-GPU-TensorFlow-on-K8S/blob/e8d615942d82a071d67462e8f9032ae68c817e4a/lab04/worker0-gpu.yml#L22) in yaml. 
```bash
# kubectl create -f ps0.yml
# kubectl create -f worker0-gpu.yml
# kubectl create -f worker1-gpu.yml
```


```bash
# kubectl get pod --show-all
NAME                   READY     STATUS      RESTARTS   AGE
ps0-3586931332-7zh2x   1/1       Running     0          3m
worker0-vrmmm          0/1       Completed   0          3m
worker1-gpjkf          0/1       Completed   0          3m
```

Let's check output of each Pod, and we can see only one available GPU in each Pod.
```bash
# kubectl logs worker0-vrmmm
...
I tensorflow/core/common_runtime/gpu/gpu_device.cc:885] Found device 0 with properties:
name: Tesla M60
major: 5 minor: 2 memoryClockRate (GHz) 1.1775
pciBusID 0000:05:00.0
Total memory: 7.93GiB
Free memory: 7.86GiB
I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0
I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla M60, pci bus id: 0000:05:00.0)
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:200] Initialize GrpcChannelCache for job ps -> {0 -> ps0.default.svc.cluster.local:2222}
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:200] Initialize GrpcChannelCache for job worker -> {0 -> localhost:2222, 1 -> worker1.default.svc.cluster.local:2222}
I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:221] Started server with target: grpc://localhost:2222
I tensorflow/core/distributed_runtime/master_session.cc:1012] Start master session adbd2a3ea1bd85fe with config:
...
步驟: 36399, loss: 70.5243148804
步驟: 36499, loss: 70.4399795532
步驟: 36599, loss: 70.3558349609
步驟: 36699, loss: 70.2718963623
步驟: 36799, loss: 70.1881408691
步驟: 36899, loss: 70.1045303345
步驟: 36999, loss: 70.021156311
步驟: 37099, loss: 69.9379501343

# kubectl logs worker1-gpjkf
...
I tensorflow/core/common_runtime/gpu/gpu_device.cc:885] Found device 0 with properties:
name: Tesla M60
major: 5 minor: 2 memoryClockRate (GHz) 1.1775
pciBusID 0000:04:00.0
Total memory: 7.93GiB
Free memory: 7.86GiB
I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0
I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla M60, pci bus id: 0000:04:00.0)
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:200] Initialize GrpcChannelCache for job ps -> {0 -> ps0.default.svc.cluster.local:2222}
I tensorflow/core/distributed_runtime/rpc/grpc_channel.cc:200] Initialize GrpcChannelCache for job worker -> {0 -> worker0.default.svc.cluster.local:2222, 1 -> localhost:2222}
I tensorflow/core/distributed_runtime/rpc/grpc_server_lib.cc:221] Started server with target: grpc://localhost:2222
I tensorflow/core/distributed_runtime/master_session.cc:1012] Start master session 5b265512d1eb5ddf with config:

I tensorflow/core/distributed_runtime/master_session.cc:1012] Start master session 9117b7c86b667bdd with config:
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
# kubectl delete -f ps0.yml
# kubectl delete -f worker0.yml
# kubectl delete -f worker1.yml
```