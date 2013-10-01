
"""
  //long duration, inches, cm;
  long duration;

  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);
  delay(100);
  return duration;
"""

import adf_mpc230x 
import time
#import robot

mcp = adf_mpc230x.Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)

def pulseIn(pin):
   c = 0
   x = 0
   #while x!=1 or c>.01:
   while c<.01: 
     x = mcp.input(pin)
     if (x==1):
       return c
     c=c+.0001
   return c


def get_pinger(ping_pin=0):
   out = 0
   mcp.config(ping_pin,adf_mpc230x.OUTPUT)
   mcp.output(ping_pin,0)
   time.sleep(.002)
   mcp.output(ping_pin,1)
   time.sleep(.005)
   mcp.output(ping_pin,0)
   #read data
   
   mcp.pullup(ping_pin, 0)
   mcp.config(ping_pin,adf_mpc230x.INPUT)
   out =  mcp.input(ping_pin)
   #out = pulseIn(ping_pin)
   time.sleep(.01)
   return out


def run():
   for x in (range(5)):
     print (get_pinger() )

run()




