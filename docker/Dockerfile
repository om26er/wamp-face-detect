FROM ubuntu

USER root

WORKDIR /workspace

RUN    apt update \
    && apt install python3-setuptools git ca-certificates gcc python3-dev libglib2.0-0 libsm6 libxrender1 -y \
    && easy_install3 pip \
    && git clone https://github.com/om26er/wamp-face-detect.git \
    && pip3 install -r wamp-face-detect/requirements.txt \
    && apt clean \
    && rm -rf /var/lib/apt/lists/

WORKDIR /workspace/wamp-face-detect

CMD ["crossbar", "start"]
