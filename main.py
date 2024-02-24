import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *
from uat import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "hoanghao2208"
AIO_KEY = "aio_Gqaj68YWoIfsFDY4dXmKoSamBAql"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + ", feed id:" + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
sensor_type = 0
couter_ai = 5
ai_result = ""
prev_result = ""

while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     #todo
    #     # print("Random data is publising...")
    #     if sensor_type == 0:
    #         print("Temperature data is publising...")
    #         temp = random.randint(5, 40)
    #         client.publish("cambien1", temp)
    #         sensor_type = 1
    #     elif sensor_type == 1:
    #         print("Humidity data is publising...")
    #         humi = random.randint(50, 70)
    #         client.publish("cambien2", humi)
    #         sensor_type = 2
    #     elif sensor_type == 2:
    #         print("Light data is publising...")
    #         light = random.randint(100, 500)
    #         client.publish("cambien3", light)
    #         sensor_type = 0
            
    couter_ai = couter_ai - 1
    if couter_ai <= 0:
        couter_ai = 5
        prev_result = ai_result
        ai_result = image_detector()
        print("AI Output:", ai_result)
        if prev_result != ai_result:
            client.publish("ai", ai_result)
        
    readSerial(client)
    time.sleep(1)