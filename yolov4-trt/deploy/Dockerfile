FROM mydl/nvidia:cuda10.1-cudnn7-ubuntu18.04-trt6
# MAINTAINER  papageno

# COPY all model files 
COPY ./deploy-standalone /home/deploy-standalone

WORKDIR  /home/deploy-standalone

ENTRYPOINT ["python3", "deploy_flaskAPI.py" ]
# default run yolov4-512
CMD ["-m", "yolov4-512"] 