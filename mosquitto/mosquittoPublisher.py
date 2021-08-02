#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:08:20 2021

@author: ruben
"""
import sys

import paho.mqtt.client as paho
import random
import time

def on_message(client, userdata, message):
	print('------------------------------')
	print('topic: %s' % message.topic)
	print('payload: %s' % message.payload)
	print('qos: %d' % message.qos)

def main():
    broker='10.152.183.231'
    port=1883
    topic='casa/cocina/nevera'

    client1= paho.Client('control1')                           #create client object
    client1.on_publish = on_publish                          #assign function to callback
    client1.connect(broker,port)                                 #establish connection
    for numero in range(100):
        valor  = random.randrange(10000)
        ret= client1.publish(topic, valor)                   #publish
        time.sleep(0.5) # Sleep for 3 secondsun lugar

def on_publish(client,userdata,result):             #create function for callback
    print('data published \n')
    pass

if __name__ == '__main__':
	main()

sys.exit(0)






