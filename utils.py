import config as c
import network
import socket
import time
import machine
from time import sleep
import gc
import urequests as requests 
import json

#setup config
config = c.get_config()


def connect_wifi():
    try:
        #Connect to WLAN
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(config['ssid'], config['password'])
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f'Connected on {ip}')
        return ip
    except Exception as e:
        print(str(e))
        print('Error connecting to wifi.. resetting device..')
        machine.reset()
        

def check_connection():
    wlan = network.WLAN(network.STA_IF)
    return wlan.isconnected()
    
def send_data(status):
    print('Sending data to server')
    #  convert time to date time format
    today_date = time.time()

    # Header Requests
    headers = {
        'Content-Type': 'application/json'
    }

    # Body Requests
    data = {
        'deviceId': config['device_id'],
        'status': status,
        'createdAt': today_date
    }
    

    # Send Requests
    try:
        response = requests.post(config['endpoint_url'], json=data)
        print(response.status_code)
        
        
    except Exception as e:
        print(str(e))
        print('Error sending data to server')
        



