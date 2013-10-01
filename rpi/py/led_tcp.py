import kl_i2c_multiplexer
import kl_rpi_tcp_joyserver

import time

vdel = .5 


TCP = kl_rpi_tcp_joyserver.joystick_tcp_server

def turn_right(inp):
   print 'TURNNN RIGHTT!'

TCP.turn_right = turn_right
TCP.listen()




##########################

foobar = kl_i2c_multiplexer.led_display()
count=0;
while True:
  foobar.set_digit(count)
  foobar.set_number(0)
  time.sleep(vdel)
  foobar.set_number(1)
  time.sleep(vdel)
  foobar.set_number(2)
  time.sleep(vdel)
  foobar.set_number(3)
  time.sleep(vdel)
  foobar.set_number(4)
  time.sleep(vdel)
  foobar.set_number(5)
  time.sleep(vdel)
  foobar.set_number(6)
  time.sleep(vdel)
  foobar.set_number(7)  
  time.sleep(vdel)
  foobar.set_number(8) 
  time.sleep(vdel)
  foobar.set_number(9)   
  time.sleep(vdel)
  foobar.set_number(99)  
  time.sleep(vdel)
  if (count<4):
      count=count+1
  if (count==4):
     count = 0

##########################





