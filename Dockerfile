FROM python:3.7

WORKDIR /usr/src/app

RUN apt-get -y update && \
    apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python-pip \
    python3 \
    python3-pip \
    python3-opencv \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN python -m venv venv
RUN . venv/bin/activate \
        && pip install --upgrade pip


# Install DLIB
RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.20' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

RUN cd ~ && \
    pip3 install flask flask-cors

# Install Face-Recognition Python Library
RUN cd ~ && \
    mkdir -p face_recognition && \
    git clone https://github.com/ageitgey/face_recognition.git face_recognition/ && \
    cd face_recognition/ && \
    pip3 install -r requirements.txt && \
    python3 setup.py install


# Copy web service script
COPY . /usr/src/app/

#RUN python3 main.py
CMD ["python3","main.py"]

