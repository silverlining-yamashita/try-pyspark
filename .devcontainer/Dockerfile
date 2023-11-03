FROM mcr.microsoft.com/devcontainers/base:debian
# FROM quay.io/jupyter/scipy-notebook
# FROM quay.io/jupyter/pyspark-notebook

ARG WORKDIR=/workspace

RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

RUN sudo apt-get -y update && apt-get -y upgrade && \
    sudo apt-get install -y default-jdk && \
    sudo apt-get install -y git tar python3 python3-pip python3-xyzservices && \
    pip3 install -U pip --break-system-packages --no-cache-dir && \
    pip3 install pre-commit --break-system-packages --no-cache-dir && \
    # Install pyspark and more
    pip3 install pyspark --break-system-packages --no-cache-dir && \
    pip3 install delta-spark --break-system-packages --no-cache-dir && \
    pip3 install pytest --break-system-packages --no-cache-dir && \
    pip3 install ipykernel --break-system-packages --no-cache-dir && \
    pip3 install pyarrow --break-system-packages --no-cache-dir && \
    pip3 install DBUtils --break-system-packages --no-cache-dir && \
    sudo chmod -R 777 ./