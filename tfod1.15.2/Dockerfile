FROM tensorflow/tensorflow:1.15.2-gpu-py3

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

# Install apt dependencies
RUN apt-get update -y \
    && apt-get install -y \
    git \
    gpg-agent \
    python3-cairocffi \
    protobuf-compiler \
    python3-pil \
    python3-lxml \
    python3-tk \
    python3.6-dev \
    wget

# # Add new user to avoid running as root
# RUN useradd -ms /bin/bash tensorflow
# USER tensorflow
# WORKDIR /home/tensorflow

# # Copy this version of of the model garden into the image
# COPY --chown=tensorflow ./models /home/tensorflow/models
 COPY ./models /home/tensorflow/models

# use tsinghua mirror
# RUN python -m pip install --user -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple
# RUN python -m pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install cmake cython -i https://pypi.tuna.tsinghua.edu.cn/simple

# for the fucking pycocotools
COPY ./cocoapi /home/tmp/cocoapi

WORKDIR /home/tmp/cocoapi/PythonAPI

RUN make \
    && cp -r pycocotools/ /home/tensorflow/models/research/

# Compile protobuf configs
WORKDIR /home/tensorflow/models/research/
RUN protoc object_detection/protos/*.proto --python_out=.

RUN cp object_detection/packages/tf1/setup.py ./
ENV PATH="/home/tensorflow/.local/bin:${PATH}"

RUN pip install . --use-feature=2020-resolver -i https://pypi.tuna.tsinghua.edu.cn/simple

ENV TF_CPP_MIN_LOG_LEVEL 3

# # Test the installation.
# python object_detection/builders/model_builder_tf1_test.py
