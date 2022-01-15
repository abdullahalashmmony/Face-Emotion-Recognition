FROM python:3.8-slim-buster
ENV TERM=xterm
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    libopencv-dev \
    python3-opencv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
ADD . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app


CMD ["python", "main.py"]
