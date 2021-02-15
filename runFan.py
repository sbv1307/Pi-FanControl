'''
Created on 29. dec. 2017

@author: sbv

runFan.py is build to controle GPIO pin 18 (BCM numbering), where a CPU cooling fan can be connected.
Depending on the CPU temperature, the fan will be tunned ON or OFF

CPU temperature above [maxTMP] will turn the fan ON
CPU temperature below [minTMP] will turn the fan OFF

in version 1.0.0 the temperature tresholds are defined as:
maxTMP = 75
minTMP = 65



Version history
1.0.0 - Initial commit 

'''
DEBUG = False

SCRIPT_VERSION = 'Run fan - check temperature and activate / de-activate cooling fan. Version V1.0.0'

import os
from time import sleep
import datetime
import signal
import sys
import RPi.GPIO as GPIO

LOG_FILE = '/tmp/runFan.log'

pin = 18 # The pin ID, edit here to change it
maxTMP = 75 # The maximum temperature in Celsius after which we trigger the fan
minTMP = 65 # The minimum temperature in Celsius after which we stop the fan

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT)
    return()

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    return temp

def fanON():
    setPin(True)
    return()

def fanOFF():
    setPin(False)
    return()

def getTEMP():
    global maxTMP
    global minTMP
    CPU_temp = float(getCPUtemperature())

    fanStatus = "No change."
    if CPU_temp > maxTMP:
        fanON()
        fanStatus = "turned ON."
    elif CPU_temp < minTMP:
        fanOFF()
        fanStatus = "turned OFF."
    linje = "\nCurrent CPU temperature: " + str(CPU_temp) + ". Cooling fan " + fanStatus
    logFile.write( linje)
    if (DEBUG):
        print linje

    return()

def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()

logFile = open( LOG_FILE, 'w')
dt = datetime.datetime.now()
linje = SCRIPT_VERSION + "\nStart at: " + dt.strftime('%d/%m/%y %H:%M %S')
logFile.write( linje)

linje = "\nMinimum temperature: " + str(minTMP) + "\nMaximum temperature: " + str(maxTMP) 
logFile.write( linje)
if (DEBUG):
    print linje
setup()
getTEMP()    


linje = "\nEnded successful at: " + dt.strftime('%d/%m/%y %H:%M %S') + "\n"
logFile.write( linje)
logFile.close()
