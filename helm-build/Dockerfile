FROM alpine/helm:3.0.3

RUN apk add curl python
RUN curl -O https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py
RUN pip install awscli
