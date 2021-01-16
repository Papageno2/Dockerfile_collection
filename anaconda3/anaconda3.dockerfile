# FROM nvidia/cuda:11.1.1-devel-ubuntu20.04
FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04
MAINTAINER Papageno

ENV TZ=Asia/Shanghai
ENV DEBIAN_FRONTEND="noninteractive"

# for py3
RUN set -x; \
    buildDeps1='python3-pip python3-dev vim libsm6 libxext6 libxrender-dev'; \
    buildDeps2='libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6'; \
    buildDeps3='libllvm-9-ocaml-dev libllvm9 llvm-9 llvm-9-dev llvm-9-doc llvm-9-examples llvm-9-runtime' \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends $buildDeps1 \
    && apt-get install -y --no-install-recommends $buildDeps2 \
    && apt-get install -y --no-install-recommends $buildDeps3 \
    && apt-get install -y --no-install-recommends tzdata cython build-essential \
    && export LLVM_CONFIG='/usr/bin/llvm-config-9' \
    && rm -rf /var/lib/apt/lists/* 

# gcc gfortran
RUN set -x; apt-get update -y \
    && apt-get install -y --no-install-recommends wget unzip git \
    && apt-get install -y --no-install-recommends gcc gfortran gdb make 

# for BLAS and LAPACK

RUN  rm /var/lib/apt/lists/lock \
    && apt-get update -y \
    && apt-get install -y libblas-dev liblapack-dev

RUN rm -rf /var/lib/apt/lists/*  \
    && apt-get purge -y --auto-remove

COPY Anaconda3-2020.11-Linux-x86_64.sh /home/Anaconda3-2020.11-Linux-x86_64.sh

WORKDIR  /home/
# https://docs.anaconda.com/anaconda/install/silent-mode/
RUN set -e; \
    # install in silent mode
    bash Anaconda3-2020.11-Linux-x86_64.sh -b -p  $HOME/anaconda3 \
    && rm Anaconda3-2020.11-Linux-x86_64.sh

RUN set -e; \
    echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.bashrc \
    && /bin/bash -c "source ~/.bashrc"

ENTRYPOINT ["/bin/bash"]