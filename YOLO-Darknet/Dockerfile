FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN set -x; apt update -y \
    && apt install -y --no-install-recommends \
        python3-pip \
        python3-dev \
        pkg-config \
        build-essential \
        libopencv-dev \
    && apt-get install -y  --no-install-recommends \
        cython \
        wget \
        unzip \
        ffmpeg \
        git \
        vim \
    && rm -rf /var/lib/apt/lists/* 


RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple  \
    && pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install cmake  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install scikit-build -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install requests  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install flask  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install imutils  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install pycuda  -i https://pypi.tuna.tsinghua.edu.cn/simple

# build darknet
COPY ./darknet-master /home/darknet

WORKDIR  /home/darknet

RUN make OPENCV=1 GPU=1 AVX=1 LIBSO=1 OPENMP=1 CUDNN=1 CUDNN_HALF=1 OPENMP=1 -j $(nproc)
RUN chmod +x darknet

# ENTRYPOINT ["darknet"]