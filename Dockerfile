# Dockerfile for Jenkins-like environment
FROM jenkins/jenkins:lts

USER root

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    docker.io

# Install Python dependencies (assuming a requirements.txt file)
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

USER jenkins
