FROM ubuntu:18.04

LABEL "MAINTAINER"=emanuel.afanador@koombea.com

ENV DEBIAN_FRONTEND noninteractive

# System packages
RUN apt-get update && apt-get install -y --no-install-recommends nginx curl
RUN apt-get -y install gcc mono-mcs gettext-base && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda
RUN apt-get update

# Python packages from conda
RUN conda install -c anaconda -y python=3.7.7

# Copy src
COPY . /home/digits_recognizer_app

# Install requirements.txt
RUN pip install -r /home/digits_recognizer_app/config/requirements.txt
RUN pip install torch==1.7.0+cpu torchvision==0.8.1+cpu \
    -f https://download.pytorch.org/whl/torch_stable.html
# Copy nginx config
COPY config/nginx.conf /opt/ml/input/config/nginx.conf.temp

# Path
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/home/digits_recognizer_app:${PATH}"

# Set work dir
WORKDIR /home/digits_recognizer_app
# ENV PORT=80

CMD serve
