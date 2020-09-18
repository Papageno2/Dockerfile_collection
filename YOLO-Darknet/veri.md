[papageno@localhost YOLO-Darknet]$ docker build -t darknet:v0 -f Dockerfile .
Sending build context to Docker daemon  27.41MB
Step 1/8 : FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04
 ---> b4879c167fc1
Step 2/8 : ENV DEBIAN_FRONTEND=noninteractive
 ---> Using cache
 ---> 4035c897e96a
Step 3/8 : RUN set -x; apt update -y     && apt install -y --no-install-recommends         python3-pip         python3-dev         pkg-config         build-essential         libopencv-dev     && apt-get install -y  --no-install-recommends         cython         wget         unzip         ffmpeg         git         vim     && rm -rf /var/lib/apt/lists/*
 ---> Using cache
 ---> 26fa8845fed9
Step 4/8 : RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple      && pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple     && pip3 install cmake  -i https://pypi.tuna.tsinghua.edu.cn/simple     && pip3 install scikit-build -i https://pypi.tuna.tsinghua.edu.cn/simple     && pip3 install requests  -i https://pypi.tuna.tsinghua.edu.cn/simple     && pip3 install flask  -i https://pypi.tuna.tsinghua.edu.cn/simple     && pip3 install imutils  -i https://pypi.tuna.tsinghua.edu.cn/simple     && pip3 install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple     && pip3 install pycuda  -i https://pypi.tuna.tsinghua.edu.cn/simple
 ---> Using cache
 ---> c323da5aa912
Step 5/8 : COPY ./darknet-master /home/darknet
 ---> Using cache
 ---> d939b9541338
Step 6/8 : WORKDIR  /home/darknet
 ---> Using cache
 ---> 2b4d72f3c7e9
Step 7/8 : RUN make OPENCV=1 GPU=1 AVX=1 LIBSO=1 OPENMP=1 CUDNN=1 CUDNN_HALF=1 OPENMP=1 -j $(nproc)
 ---> Using cache
 ---> 7a5171acb6e5
Step 8/8 : RUN chmod +x darknet
 ---> Using cache
 ---> fc83bda6c9c6
Successfully built fc83bda6c9c6
Successfully tagged darknet:v0