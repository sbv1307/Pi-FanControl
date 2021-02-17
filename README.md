# Raspberry Pi fan control

Controles GPIO pin 18 (BCM numbering) depending on the CPU temperature

### Program outline

runFan.py is build to controle GPIO pin 18 (BCM numbering), where a CPU cooling fan can be connected.
Depending on the CPU temperature, the fan will be tunned ON or OFF

CPU temperature above [maxTMP] will turn the fan ON
CPU temperature below [minTMP] will turn the fan OFF

in version 1.0.0 the temperature tresholds are defined as:
maxTMP = 75
minTMP = 65

Linux cron(8) runs runFan.py every 5 minutes.

### Dependensies

- Written in Python
- Build for Raspbian Pi 3 Model B V1.2
- Host os: Raspberry Pi (32-bit). A port of Debian with the Raspberry Pi Desktop.
- Docker containerraised: From arm32v7/python:3.7-slim-buster


### Installation

- Install docker https://dev.to/rohansawant/installing-docker-and-docker-compose-on-the-raspberry-pi-in-5-simple-steps-3mgl
- Copy content of docker-compose.yml to local docker-compose.yml and run: docker-compose up -d
- To verify successful install attac to docker container: 
    docker ps
    docker attack <container>
- check cron.log and runFan.log at /var/log. 



## NOTES

- Remember to verify that the file runFan_cron is saved with "End of line sequence" = LF only!


#### Version history
1.0.0 - Initial commit

## Wiring diagram

![](/wiringDiagrame.jpg)

