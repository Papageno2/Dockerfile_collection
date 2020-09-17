#  -*- coding: utf-8 -*-

"""


"""
import os
import time
import argparse
import numpy as np
import json
# import tensorflow as tf
from flask import Flask, request, Response
import base64
import cv2

import pycuda.autoinit  # This is needed for initializing CUDA driver
from utils.yolo_classes import get_cls_dict
from utils.visualization import BBoxVisualization
from utils.yolo_with_plugins import TrtYOLO

from utils.yolo_class import dictMap_EN #, dictMap_CN

app = Flask(__name__)

def base64toImageArray(img_base64):
    img_data = base64.b64decode(img_base64)
    image_np = np.frombuffer(img_data, np.uint8)
    image_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    return image_np

def post_process(boxes, confs, clss, score_thres):
    """
    Note:
    """
    items =[]   
    cnt = 0
    for box, score, cls_ in zip(boxes, confs, clss):
        if (score>score_thres):
            item = {"box": box.tolist(),
                    "score": str(score),
                    "class": dictMap_EN[int(cls_)]
                   }
            items.append(item)
            cnt+=1

    result = {"Nums":cnt,
              "Items":items}    
    return result
    
@app.route("/detect", methods=['POST'])
def detect():
    start = time.time()
    base64_from_post = request.json.get("IMG_BASE64")
    score_thres = request.json.get("SCORE_THRES", 0.3)

    if base64_from_post is not None:
        try:
            img_raw = base64toImageArray(base64_from_post) 
            # pdb.set_trace()
            boxes, confs, clss = trt_yolo.detect(img_raw, score_thres)
            results = post_process(boxes, confs, clss, score_thres)

            results.update({"Errors":0})
            ret = {"predictions": results}
            print("Time spent handling the request: %f" % (time.time() - start))
            return Response(json.dumps(ret, ensure_ascii=False),
                                mimetype='application/json')
        except Exception as e:
            results = str(e)
            ret = {"Errors": results}
            return Response(json.dumps(ret, ensure_ascii=False),
                                mimetype='application/json')
    else:
        ret={"Errors": "Inputs cannot be empty!"}
        return Response(json.dumps(ret, ensure_ascii=False),
                        mimetype='application/json')

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
        '-i', '--input', type=str,help=('input image path'))
    args = parser.parse_args()
    return args

# CUDA_VISIBLE_DEVICES=5 python3 xxx.py -m yolov4-512
if __name__ == "__main__":
    import pdb
    import os
    # os.environ['CUDA_VISIBLE_DEVICES'] = "5"
    args = parse_args()
    
    cls_dict = get_cls_dict(args.category_num)
    # load model
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

    trt_yolo = TrtYOLO(args.model, (h, w), args.category_num, cuda_ctx=pycuda.autoinit.context)
    # trt_yolo = TrtYOLO(args.model, (h, w), args.category_num)
    # ---------------------------------------------------------------------
    
    conf_th=0.3
    vis = BBoxVisualization(cls_dict)

    # print('Starting the API')
    app.run(debug=True, host='0.0.0.0')
