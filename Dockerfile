FROM arm32v7/alpine:latest

LABEL Name=pifancontrol Version=0.0.1

ENV LANG=C.UTF-8 \
    PYTHONIOENCODING=UTF-8

RUN apk add --no-cache python3 py3-pip

COPY runFan.py .

CMD sh
