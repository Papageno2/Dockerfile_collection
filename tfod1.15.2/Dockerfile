FROM tensorflow/tensorflow:1.15.2-gpu-py3

ARG DEBIAN_FRONTEND=noninteractive

# Install apt dependencies
RUN apt-get update && apt-get install -y \
    git \
    gpg-agent \
    python3-cairocffi \
    protobuf-compiler \
    python3-pil \
    python3-lxml \
    python3-tk \
    wget

# Add new user to avoid running as root
RUN useradd -ms /bin/bash tensorflow
USER tensorflow
WORKDIR /home/tensorflow

# Copy this version of of the model garden into the image
COPY --chown=tensorflow ./models /home/tensorflow/models

# download tfod repo.
# RUN set -x \
#     && mkdir /home/tmp \
#     && cd /home/tmp \ 
#     && git clone https://github.com/tensorflow/models.git

# Compile protobuf configs
RUN (cd /home/tensorflow/models/research/ && protoc object_detection/protos/*.proto --python_out=.)
WORKDIR /home/tensorflow/models/research/

RUN cp object_detection/packages/tf1/setup.py ./
ENV PATH="/home/tensorflow/.local/bin:${PATH}"

# use tsinghua mirror
RUN python -m pip install --user -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN set -x; python -m pip install --user . -i https://pypi.tuna.tsinghua.edu.cn/simple

ENV TF_CPP_MIN_LOG_LEVEL 3