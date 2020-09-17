"""trt_yolo.py

This script demonstrates how to do real-time object detection with
TensorRT optimized YOLO engine.
"""


import os
import time
import argparse

import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver

from utils.yolo_classes import get_cls_dict
from utils.visualization import BBoxVisualization

from utils.yolo_with_plugins import TrtYOLO


def parse_args():
    """Parse input arguments."""
    desc = ('Capture and display live camera video, while doing '
            'real-time object detection with TensorRT optimized '
            'YOLO model on Jetson')
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        '-c', '--category_num', type=int, default=80,
        help='number of object categories [80]')
    parser.add_argument(
        '-m', '--model', type=str, required=True,
        help=('yolov4-'
              '[{dimension}], where dimension could be a single '
              'number (e.g. 416,512,608) or WxH (e.g. 416x256)'))

    parser.add_argument(
        '-i', '--input', type=str, required=True,help=('input image path'))
    args = parser.parse_args()
    return args


def detect_image(trt_yolo, conf_th, vis):
    boxes, confs, clss = trt_yolo.detect(img, conf_th)
    img = vis.draw_bboxes(img, boxes, confs, clss)
    cv2.imshow('thisis_test.jpg', img)


def load_trt_model():

    return yolo_model

def main2():
    args = parse_args()

    cls_dict = get_cls_dict(args.category_num)

    yolo_dim = args.model.split('-')[-1]
    if 'x' in yolo_dim:
        dim_split = yolo_dim.split('x')
        if len(dim_split) != 2:
            raise SystemExit('ERROR: bad yolo_dim (%s)!' % yolo_dim)
        w, h = int(dim_split[0]), int(dim_split[1])
    else:
        h = w = int(yolo_dim)
    if h % 32 != 0 or w % 32 != 0:
        raise SystemExit('ERROR: bad yolo_dim (%s)!' % yolo_dim)

    trt_yolo = TrtYOLO(args.model, (h, w), args.category_num)

    print(args.category_num)
    # print(h,w)
    # print(cls_dict)
    
    conf_th=0.3
    vis = BBoxVisualization(cls_dict)

    pdb.set_trace()

    for i in range(10):
        t0 = time.time()
        img = cv2.imread(args.input)
        boxes, confs, clss = trt_yolo.detect(img, conf_th)
        print(boxes, confs, clss)
        t1 = time.time()
        print(t1-t0)

    img = vis.draw_bboxes(img, boxes, confs, clss)
    cv2.imwrite('thisis_test_.jpg', img)



if __name__ == '__main__':
    import pdb
    # main()
    main2()
