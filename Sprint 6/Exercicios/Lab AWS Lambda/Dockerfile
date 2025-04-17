FROM amazonlinux:2.0.20200602.0

RUN yum update -y && \
    yum install -y \
    python3 \
    python3-pip \
    zip && \
    yum -y clean all

RUN python3 -m pip install --upgrade pip
