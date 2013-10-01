#!/usr/bin/env python
# -*- coding: latin-1 -*-


import serial
import string
import time

test=serial.Serial("/dev/ttyAMA0",9600)
test.open()

try:
    while True:
        print ("recieving ..") 
              
        foo = test.read(250)
        print ("read char "+foo) 
        time.sleep(1) 
        #test.write("b")
        #time.sleep(1)   
        #test.write("c")
        #time.sleep(1)
        #test.write("d")
        #time.sleep(1)

     
except KeyboardInterrupt:
     pass # do cleanup here

test.close()


