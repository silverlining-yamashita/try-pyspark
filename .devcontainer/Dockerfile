FROM mcr.microsoft.com/devcontainers/base:debian
# FROM quay.io/jupyter/scipy-notebook
# FROM quay.io/jupyter/pyspark-notebook

ARG WORKDIR=/workspace

RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}

RUN sudo apt-get -y update && apt-get -y upgrade && \
    sudo apt-get install -y default-jdk && \
    sudo apt-get install -y git tar python3 python3-dev python3-pip python3-venv python3-wheel python3-xyzservices build-essential libpq-dev clang && \
    # sudo apt -y -qq install tesseract-ocr libtesseract-dev && \
    # sudo apt-get -y -qq install poppler-utils && \
    pip3 install -U pip --break-system-packages --no-cache-dir
RUN sudo chmod -R 777 ${WORKDIR}