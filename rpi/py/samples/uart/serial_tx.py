#!/usr/bin/env python
# -*- coding: latin-1 -*-


import serial
import string
import time

rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

test=serial.Serial("/dev/ttyAMA0",4800)
test.open()

try:
    while True:
        print ("transmitting ..") 
              
        #foo = test.read(1)
        #test.write(foo)
        #print ("read char "+foo) 

        test.write("a")
        time.sleep(1) 
        test.write("b")
        time.sleep(1)   
        test.write("c")
        time.sleep(1)
        test.write("d")
        time.sleep(1)

     
except KeyboardInterrupt:
     pass # do cleanup here

test.close()


