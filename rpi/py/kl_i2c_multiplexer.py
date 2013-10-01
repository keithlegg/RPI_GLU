#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
#TO RUN DO THIS FIRST:

 sudo modprobe i2c-bcm2708

"""


#  self.CONFIG       = kl_rpi_base.kl_rpi_config()
#import kl_rpi_base

import smbus
import sys
import getopt
import time 


"""
def set_led(data,bank):
  if bank == 1:
   bus.write_byte_data(address,0x12,data)
  else:
   bus.write_byte_data(address,0x13,data)
  return
"""

# Handle the command line arguments
def main():
   a = 0
delay = 0.1   




########################

class led_display:
    def __init__(self):
        self.led_common_pins = 'anode' #'anode' or 'cathode' #if anode then invert output
        self.vdelay = .01
        self.dra   =  0x01 #DIGIT   register address 
        self.sra   =  0x00 #SEGMENT register address 
        self.setup()
    ###   
    def setup(self):
        self.bus = smbus.SMBus(0)
	self.address = 0x20 # I2C address of MCP23017
	self.bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
	self.bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 
    ###          
    def send_i2c(self,data,bank):
      if bank == 1:
        self.bus.write_byte_data(self.address,0x12,data)
      else:
        self.bus.write_byte_data(self.address,0x13,data)
      time.sleep(self.vdelay)  
    ###    
    #auto compensate for vathode/anode and add a delay 
    def flash(self,data,bank):
      if bank == 1:
	if (self.led_common_pins=='cathode'): 
          self.bus.write_byte_data(self.address,0x12,data)
	if (self.led_common_pins=='anode'): 
          self.bus.write_byte_data(self.address,0x12,~data)          
      else:
	if (self.led_common_pins=='cathode'):	
          self.bus.write_byte_data(self.address,0x13,data)
	if (self.led_common_pins=='anode'):	
          self.bus.write_byte_data(self.address,0x13,~data)
      #time.sleep(self.vdelay)
         
    ###           
    def clear_all(self):
       if (self.led_common_mode=='anode'):
          set_led(self.dra,0) 
          set_led(self.sra,1) #if anode then set high ? 
          
       if (self.led_common_mode=='cathode'):
          set_led(self.dra,0) #?
          set_led(self.sra,1) #? 
    ###     
    #def set_pinmap(self):
    #    pass 
    
    ###  
    #DONT THINK THIS WORKS!
    #transpose register (11100110 = 01100111)  
    def mirror_bits(self,n,bits):
      N = 1<<bits     # find N: shift left 1 by the number of bits
      nrev = n  
      for i in range(bits) :
          n >>= 1
          nrev <<= 1
          nrev |= n & 1   # give LSB of n to nrev
      nrev &= N-1    # clear all bits more significant than N-1
      return nrev
    #DONT THINK THIS WORKS!
      
    ###     
    def set_digit(self,digitnum):
        if (digitnum==0):
           self.send_i2c(0x01,1) #digit 1
        if (digitnum==1):
           self.send_i2c(0x02,1) #digit 2
        if (digitnum==2):
           self.send_i2c(0x04,1) #digit 3
        if (digitnum==3):
           self.send_i2c(0x08,1) #digit 4           
  
    ###       
    #set 1-8 (a,b,c,d,e,f,g,dp)
    def set_segment(self,segnum):
         if (segnum==0):
           self.flash(0x01,0) 
         if (segnum==1):           
           self.flash(0x02,0) 
         if (segnum==2):           
           self.flash(0x04,0) 
         if (segnum==3):           
           self.flash(0x08,0) 
         if (segnum==4):           
           self.flash(0x10,0) 
         if (segnum==5):           
           self.flash(0x20,0) 
         if (segnum==6):           
           self.flash(0x40,0) 
         if (segnum==7):           
           self.flash(0x80,0) 
    ### 
    def set_number(self,num):
         if (num==0):
           self.flash(0x03f,0) 
         if (num==1):           
           self.flash(0x06,0) 
         if (num==2):           
           self.flash(0x5b,0) 
         if (num==3):           
           self.flash(0x4f,0) 
         if (num==4):           
           self.flash(0x66,0) 
         if (num==5):           
           self.flash(0x6d,0) 
         if (num==6):           
           self.flash(0x7d,0) 
         if (num==7):           
           self.flash(0x07,0) #wow! 7 is 7!
         if (num==8):           
           self.flash(0x7f,0) 
         if (num==9):           
           self.flash(0x67,0)            
         if (num==99): #decimal          
           self.flash(0x80,0)    
    ###
    #MULTIPLEX 4 DIGITS 
    def set_by_four(self,ar):
         for x in range(4):
	     self.set_number(ar[x])
	     self.set_digit(x)       

#################


   
   
#################


"""   
foobar = led_display()
count = 0
incr  = 0
steps = 30 #sub count 
while True:
  foobar.set_by_four([incr+3,incr+2,incr+1,incr])
  if (count==steps):
     incr=incr+1
  if (count==steps*2):
     incr=incr+1
  if (count==steps*3):
     incr=incr+1
  if (count==steps*4):
     incr=incr+1    
  if (count==steps*5):
     incr=incr+1   
  if (count==steps*6):
     incr=incr+1        
  if (count==steps*7):
     count=0
     incr=0
  count=count+1
"""

#################

"""      
foobar = led_display()
count=0;
while True:
  foobar.set_digit(count)
  foobar.set_number(0)
  foobar.set_number(1)
  foobar.set_number(2)
  foobar.set_number(3)
  foobar.set_number(4)
  foobar.set_number(5)
  foobar.set_number(6)
  foobar.set_number(7)  
  foobar.set_number(8) 
  foobar.set_number(9)   
  foobar.set_number(99)  
  if (count<4):
      count=count+1
  if (count==4):
     count = 0
"""

#################

""" 
# Move led right 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,1)
     time.sleep(delay)
   set_led(0,1)
 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,0)
     time.sleep(delay)
   set_led(0,0)
"""   
  
if __name__ == "__main__":
   main()
