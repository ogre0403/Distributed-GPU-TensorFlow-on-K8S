## Enable GPU in Pod
```bash
$ kubectl create -f gpu.yml
$ kubectl logs tensorflow-gpu
...

pciBusID 0000:05:00.0
Total memory: 7.93GiB
Free memory: 7.86GiB
2017-08-29 08:32:46.838978: I tensorflow/core/common_runtime/gpu/gpu_device.cc:976] DMA: 0 1
2017-08-29 08:32:46.839001: I tensorflow/core/common_runtime/gpu/gpu_device.cc:986] 0:   Y Y
2017-08-29 08:32:46.839011: I tensorflow/core/common_runtime/gpu/gpu_device.cc:986] 1:   Y Y
2017-08-29 08:32:46.839032: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla M60, pci bus id: 0000:04:00.0)
2017-08-29 08:32:46.839044: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1045] Creating TensorFlow device (/gpu:1) -> (device: 1, name: Tesla M60, pci bus id: 0000:05:00.0)
[name: "/cpu:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 7186035892311233748
, name: "/gpu:0"
device_type: "GPU"
memory_limit: 8017303962
locality {
  bus_id: 1
}
incarnation: 7078516362132344256
physical_device_desc: "device: 0, name: Tesla M60, pci bus id: 0000:04:00.0"
, name: "/gpu:1"
device_type: "GPU"
memory_limit: 8017303962
locality {
  bus_id: 1
}
incarnation: 5439146824451313017
physical_device_desc: "device: 1, name: Tesla M60, pci bus id: 0000:05:00.0"
]

$ kubectl delete -f gpu.yml
```