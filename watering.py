import config as c
import utils
import machine
from machine import Pin, Timer
import time
import config
import requests
import network
import socket
import gc
import random


# Setup Config
config = c.get_config()

# setup wifi
utils.connect_wifi()

# setup pin
LDR_IN_PIN = 1
MOISTURE_IN_PIN = 7
POWER_FOR_MOISTURE = 4
POWER_FOR_LDR = 18
POWER_FOR_PUMP = 10

led = Pin('LED', Pin.OUT)
power_for_moisture = Pin(POWER_FOR_MOISTURE, Pin.OUT)
power_for_ldr = Pin(POWER_FOR_LDR, Pin.OUT)
ldr_sensor = Pin(LDR_IN_PIN, mode=Pin.IN)
moisture_sensor = Pin(MOISTURE_IN_PIN, mode=Pin.IN)
power_for_pump = Pin(POWER_FOR_PUMP, mode=Pin.OUT)

power_for_moisture.on()
power_for_ldr.on()
power_for_pump.off()
led.off()

while True:
    is_there_light = ldr_sensor.value();
    is_there_moisture = moisture_sensor.value();
    
    #is_there_light = random.randint(0, 1);
    #is_there_moisture = random.randint(0, 1);
    
    previous_pump_state = power_for_pump.value();
    print("ldr: ", is_there_light , " moist: " , is_there_moisture) 
    
    if (is_there_light == 1 and is_there_moisture == 0):
        power_for_pump.on()
        led.on()
        utils.send_data("on")
    else:
        if previous_pump_state == 1:
            power_for_pump.off()
            led.off()
            utils.send_data("off")
    
        
    print("previous_state: ", previous_pump_state)
    time.sleep(2)
    gc.collect()
