FROM arm32v7/python:3.7-slim-buster

LABEL maintainer="sbv1307@gmail.com"
LABEL Name="pi-fan-control" \
      Version="0.0.1"

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get -y install cron
RUN pip install RPi.GPIO

COPY runFan.py /app/

# Copy cron file file to the cron.d directory
COPY runFan_cron /etc/cron.d/

# Give execution rights on the cron job
RUN chmod 0744 /etc/cron.d/runFan_cron

# Apply cron job
RUN crontab /etc/cron.d/runFan_cron

WORKDIR /app/

# Run cron at container startup
CMD cron && sh

# Docker-compose will run the container like:
#   docker run -it --privileged --device=/dev/vchiq -e LD_LIBRARY_PATH=/opt/vc/lib:/opt/vc/bin -v /opt/vc:/opt/vc:ro sbv1307/pi-fan-control:py