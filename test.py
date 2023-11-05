import gc
import machine
from machine import Pin, Timer
import time

LDR_IN_PIN = 1
MOISTURE_IN_PIN = 7
POWER_FOR_MOISTURE = 4
POWER_FOR_LDR = 2


led = Pin('LED', Pin.OUT)
power_for_moisture = Pin(POWER_FOR_MOISTURE, Pin.OUT)
power_for_ldr = Pin(POWER_FOR_LDR, Pin.OUT)
ldr_sensor = Pin(LDR_IN_PIN, mode=Pin.IN)
moisture_sensor = Pin(MOISTURE_IN_PIN, mode=Pin.IN)

power_for_moisture.on()
power_for_ldr.on()

while True:
    print("ldr: ", ldr_sensor.value() , " moist: " , moisture_sensor.value()) 
    time.sleep(0.5)
    gc.collect()
