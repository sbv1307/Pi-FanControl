FROM arm32v7/python:3.7-slim-buster



LABEL Name=pifancontrol Version=0.0.1

ENV PATH="${PATH}:/opt/vc/bin"

RUN apt-get update && \
    apt-get install build-essential -y
RUN pip install RPi.GPIO

COPY runFan.py /app/


WORKDIR /app/

CMD sh

#  docker run -it --privileged --device=/dev/vchiq -e LD_LIBRARY_PATH=/opt/vc/lib -v /opt/vc:/opt/vc:ro sbv1307/pi-fan-control:py