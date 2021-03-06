# docker build -t $YOURTAGNAME -f $DockerfilePATH .

FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ENV TZ=Asia/Shanghai
ENV DEBIAN_FRONTEND="noninteractive"

# libllvm for llvmlite for numba
RUN set -x; \
    buildDeps1='python3-pip python3-dev vim libsm6 libxext6 libxrender-dev'; \
    buildDeps2='libllvm-9-ocaml-dev libllvm9 llvm-9 llvm-9-dev llvm-9-doc llvm-9-examples llvm-9-runtime' \
    && apt-get update -y \
    && DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends $buildDeps1 \
    && apt-get install -y --no-install-recommends cython build-essential libopencv-dev \
    && apt-get install -y --no-install-recommends tzdata \
    && apt-get install -y --no-install-recommends $buildDeps2 \
    && export LLVM_CONFIG='/usr/bin/llvm-config-9' \
#     && apt-get purge -y --auto-remove $buildDeps1 
#     && apt-get purge -y --auto-remove $buildDeps2 \
    && rm -rf /var/lib/apt/lists/* 
    
    

RUN set -x \
    && apt-get update -y \  
    && apt-get install -y wget unzip ffmpeg git


# install python packages
RUN set -x \
    && pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple  \
    && pip3 install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install cmake  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install scikit-build -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install requests  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install flask  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install imutils  -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && LLVM_CONFIG=/usr/bin/llvm-config-9 pip3 install llvmlite numba -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install pycuda  -i https://pypi.tuna.tsinghua.edu.cn/simple
    
    
# Install TRT-6.0
# YOU SHOULD HAVE THE TENSORRT INSTALLMENT FILES AT SPECIFIC PATH.

COPY ./TensorRT-6.0.1.5  /root/TensorRT-6.0.1.5

RUN set -x && \
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/root/TensorRT-6.0.1.5/lib  \
    && ls -ahl /root/ && pwd \
    && pip3 install /root/TensorRT-6.0.1.5/python/tensorrt-6.0.1.5-cp36-none-linux_x86_64.whl \
    && pip3 install /root/TensorRT-6.0.1.5/graphsurgeon/graphsurgeon-0.4.1-py2.py3-none-any.whl

RUN rm -rf /var/lib/apt/lists/*  \
    && apt-get purge -y --auto-remove


WORKDIR /root/

RUN set -x \
    && cp TensorRT-6.0.1.5/targets/x86_64-linux-gnu/lib/libnvinfer.so.6  /usr/lib/ \
    && cp TensorRT-6.0.1.5/targets/x86_64-linux-gnu/lib/libnvonnxparser.so.6 /usr/lib/  \
    && cp TensorRT-6.0.1.5/targets/x86_64-linux-gnu/lib/libnvonnxparser_runtime.so.6  /usr/lib/ \
    && cp TensorRT-6.0.1.5/targets/x86_64-linux-gnu/lib/libnvparsers.so.6  /usr/lib/  \
    && cp TensorRT-6.0.1.5/targets/x86_64-linux-gnu/lib/libnvinfer_plugin.so.6  /usr/lib/ 

    


