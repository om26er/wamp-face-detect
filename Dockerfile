FROM ubuntu:artful

USER root

WORKDIR /workspace

RUN    apt update \
    && apt install python3-pip unzip wget git libsm6 libxrender1 -y \
    && wget https://github.com/om26er/wamp-face-detect/archive/master.zip \
    && unzip master.zip \
    && pip3 install -r wamp-face-detect-master/app/requirements.txt \
    && apt clean \
    && apt purge unzip git wget -y \
    && apt autoremove -y \
    && rm -rf ~/.cache/pip \
    && rm -rf /var/lib/apt/lists/

WORKDIR /workspace/wamp-face-detect-master

CMD ["python3", "-u", "app/server.py"]
