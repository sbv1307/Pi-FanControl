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

### Dependensies

- Written in Python
- Build for Raspbian Pi 3 Model B V1.2
- Host os: Raspberry Pi (32-bit). A port of Debian with the Raspberry Pi Desktop.
- Docker containerraised: From arm32v7/python:3.7-slim-buster


#### Version history
1.0.0 - Initial commit

## Wiring diagram

![](/wiringDiagrame.jpg)

