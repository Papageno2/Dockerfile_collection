# Dockerfile_collection
collection of Dockerfile.



- [x]  cuda10.1-cudnn7-tenorrt6.0.1.5
- [x] Yolov4-trt-deployment
- [x] YOLOv4-darknet: `train/detect`
  - For YOLOv4-darknet model training
  - For YOLOv4-darknet model deploy
- [x] tfod-train-1.15.2
  - TensorFlow1.15.2 object detection training image.
- [ ] ...



### YOLO-Darknet

from [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)

### YOLOv4-trt-deployment usage
> Thanks for the nice repo. from [jkjung-avt](https://github.com/jkjung-avt/tensorrt_demos), where almost all `*.py` codes borrown from.


default starting the container effctively behave as
```shell
docker run -itd -p 11221:5000 --name yolotrt512 --gpus '"device=5"' yolov4/deploy:trt -m yolov4-512
```

You can simply change the `CMD` in the `CLI` as:

```shell
docker run -itd -p 11221:5000 --name yolotrt512 --gpus '"device=5"' yolov4/deploy:trt -m yolov4-416
```

or using `yolov4-608`.

### TFOD1.15.2

build the image like (see [veri.md](tfod1.15.2/veri.md)):

```shell
docker build -t tfod:1.15.2 -f Dockerfile .
```

other tfod details, please refer to [tensorflow/models](https://github.com/tensorflow/models/tree/master/research/object_detection)

- https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1.md

when finish the image building process,  test the installation in a container,

```python
# Test the installation.
python object_detection/builders/model_builder_tf1_test.py
```

```shell
root@246c6b10349f:/home/tensorflow/models/research# python object_detection/builders/model_builder_tf1_test.py
Running tests under Python 3.6.9: /usr/local/bin/python
[ RUN      ] ModelBuilderTF1Test.test_create_context_rcnn_from_config_with_params(True)
[       OK ] ModelBuilderTF1Test.test_create_context_rcnn_from_config_with_params(True)
[ RUN      ] ModelBuilderTF1Test.test_create_context_rcnn_from_config_with_params(False)
[       OK ] ModelBuilderTF1Test.test_create_context_rcnn_from_config_with_params(False)
[ RUN      ] ModelBuilderTF1Test.test_create_experimental_model
[       OK ] ModelBuilderTF1Test.test_create_experimental_model
[ RUN      ] ModelBuilderTF1Test.test_create_faster_rcnn_from_config_with_crop_feature(True)
[       OK ] ModelBuilderTF1Test.test_create_faster_rcnn_from_config_with_crop_feature(True)
[ RUN      ] ModelBuilderTF1Test.test_create_faster_rcnn_from_config_with_crop_feature(False)
[       OK ] ModelBuilderTF1Test.test_create_faster_rcnn_from_config_with_crop_feature(False)
[ RUN      ] ModelBuilderTF1Test.test_create_faster_rcnn_model_from_config_with_example_miner
[       OK ] ModelBuilderTF1Test.test_create_faster_rcnn_model_from_config_with_example_miner
[ RUN      ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_faster_rcnn_with_matmul
[       OK ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_faster_rcnn_with_matmul
[ RUN      ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_faster_rcnn_without_matmul
[       OK ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_faster_rcnn_without_matmul
[ RUN      ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_mask_rcnn_with_matmul
[       OK ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_mask_rcnn_with_matmul
[ RUN      ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_mask_rcnn_without_matmul
[       OK ] ModelBuilderTF1Test.test_create_faster_rcnn_models_from_config_mask_rcnn_without_matmul
[ RUN      ] ModelBuilderTF1Test.test_create_rfcn_model_from_config
[       OK ] ModelBuilderTF1Test.test_create_rfcn_model_from_config
[ RUN      ] ModelBuilderTF1Test.test_create_ssd_fpn_model_from_config
[       OK ] ModelBuilderTF1Test.test_create_ssd_fpn_model_from_config
[ RUN      ] ModelBuilderTF1Test.test_create_ssd_models_from_config
[       OK ] ModelBuilderTF1Test.test_create_ssd_models_from_config
[ RUN      ] ModelBuilderTF1Test.test_invalid_faster_rcnn_batchnorm_update
[       OK ] ModelBuilderTF1Test.test_invalid_faster_rcnn_batchnorm_update
[ RUN      ] ModelBuilderTF1Test.test_invalid_first_stage_nms_iou_threshold
[       OK ] ModelBuilderTF1Test.test_invalid_first_stage_nms_iou_threshold
[ RUN      ] ModelBuilderTF1Test.test_invalid_model_config_proto
[       OK ] ModelBuilderTF1Test.test_invalid_model_config_proto
[ RUN      ] ModelBuilderTF1Test.test_invalid_second_stage_batch_size
[       OK ] ModelBuilderTF1Test.test_invalid_second_stage_batch_size
[ RUN      ] ModelBuilderTF1Test.test_session
[  SKIPPED ] ModelBuilderTF1Test.test_session
[ RUN      ] ModelBuilderTF1Test.test_unknown_faster_rcnn_feature_extractor
[       OK ] ModelBuilderTF1Test.test_unknown_faster_rcnn_feature_extractor
[ RUN      ] ModelBuilderTF1Test.test_unknown_meta_architecture
[       OK ] ModelBuilderTF1Test.test_unknown_meta_architecture
[ RUN      ] ModelBuilderTF1Test.test_unknown_ssd_feature_extractor
[       OK ] ModelBuilderTF1Test.test_unknown_ssd_feature_extractor
----------------------------------------------------------------------
Ran 21 tests in 0.293s

OK (skipped=1)
```



