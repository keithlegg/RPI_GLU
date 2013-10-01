#!/usr/bin/env python
# -*- coding: latin-1 -*-


import serial
import string
import time

test=serial.Serial("/dev/ttyAMA0",9600)
test.open()

print 'stop motor'
test.write('x')
print 'wait 5 seconds'
time.sleep(1)
print '4'
time.sleep(1)
print '3'
time.sleep(1)
print '2'
time.sleep(1)
print '1'
time.sleep(1)


print 'begin ...'
test.write('z')
time.sleep(5)

try:
    while True:
        #print ("stopping motor 5 seconds..")
        #test.write('x') 
        #time.sleep(5)              
        #foo = test.read(1)
        #test.write(foo)
        #print ("read char "+foo) 
             
       
        print ('speed up') 
        test.write("b")
        time.sleep(5)   
        print ('now speed up')
        test.write("b")
        time.sleep(5)
        print ('now speed up')
        test.write("b")
        time.sleep(5)
        print ('now speed up')
        test.write("b")
        time.sleep(5)

        print ('press a key to go even faster') 
        raw_input()
     
except KeyboardInterrupt:
     pass # do cleanup here

test.close()


