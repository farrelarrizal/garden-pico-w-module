import config as c
import module_utils as utils
import machine
from machine import Pin, Timer
import time
import config
import requests
import network
import socket
import gc


# Setup Config
config = c.get_config()

#setup wifi
utils.connect_wifi()

led = Pin('LED', Pin.OUT)

while True:
    led.on()
    time.sleep(2)
    utils.send_data("on")
    
    led.off()
    time.sleep(1)
    utils.send_data("off")
    gc.collect()