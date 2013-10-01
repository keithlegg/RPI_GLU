#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C
import smbus
import time

import socket
import select
import sys

port = 11223
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1024)
serverSocket.bind(('',port))
serverSocket.listen(5)

sockets=[serverSocket]
print 'Server is started on port' , port,'\n'

def acceptConn():
    newsock, addr = serverSocket.accept()
    sockets.append(newsock)
    newsock.send('You are now connected to the chat server\n')
    msg = 'Client joined: %s:%d\n' % addr
    broadcast(msg, newsock)

def broadcast(msg, sourceSocket):
    for s in sockets:
        if (s != serverSocket and s != sourceSocket):
            s.send(msg)
    sys.stdout.write(msg)
    sys.stdout.flush()


####################################




MCP23008_IODIRA = 0x00

MCP23017_IODIRA = 0x00
MCP23017_IODIRB = 0x01
MCP23017_GPIOA = 0x12
MCP23017_GPIOB = 0x13
MCP23017_GPPUA = 0x0C
MCP23017_GPPUB = 0x0D
MCP23017_OLATA = 0x14
MCP23017_OLATB = 0x15

OUTPUT = 0
INPUT = 1
    
class Adafruit_MCP230XX(object):

    def __init__(self, busnum, address, num_gpios):
        assert num_gpios >= 0 and num_gpios <= 16, "Number of GPIOs must be between 0 and 16"
        self.i2c = Adafruit_I2C(address, smbus.SMBus(busnum))
        self.address = address
        self.num_gpios = num_gpios

        # set defaults

        if num_gpios <= 8:
            self.i2c.write8(MCP23008_IODIRA, 0xFF)  # all inputs on port A
            self.direction = self.i2c.readU8(MCP23008_IODIRA)
            self.i2c.write8(MCP23008_GPPU, 0x00)
        elif num_gpios > 8 and num_gpios <= 16:
            self.i2c.write8(MCP23017_IODIRA, 0xFF)  # all inputs on port A
            self.i2c.write8(MCP23017_IODIRB, 0xFF)  # all inputs on port B
            self.direction = self.i2c.readU8(MCP23017_IODIRA)
            self.direction |= self.i2c.readU8(MCP23017_IODIRB) << 8
            self.i2c.write8(MCP23017_GPPUA, 0x00)
            self.i2c.write8(MCP23017_GPPUB, 0x00)
    
    def _changebit(self, bitmap, bit, value):
        assert value == 1 or value == 0, "Value is %s must be 1 or 0" % value
        if value == 0:
            return bitmap & ~(1 << bit)
        elif value == 1:
            return bitmap | (1 << bit)

    def _readandchangepin(self, port, pin, value, currvalue = None):
        assert pin >= 0 and pin < self.num_gpios, "Pin number %s is invalid, only 0-%s are valid" % (pin, self.num_gpios)
        #assert self.direction & (1 << pin) == 0, "Pin %s not set to output" % pin
        if not currvalue:
             currvalue = self.i2c.readU8(port)
        newvalue = self._changebit(currvalue, pin, value)
        self.i2c.write8(port, newvalue)
        return newvalue


    def pullup(self, pin, value):
        if self.num_gpios <= 8:
            return self._readandchangepin(MCP23008_GPPU, pin, value)
        if self.num_gpios <= 16:
            if (pin < 8):
                return self._readandchangepin(MCP23017_GPPUA, pin, value)
            else:
                return self._readandchangepin(MCP23017_GPPUB, pin-8, value)

    # Set pin to either input or output mode
    def config(self, pin, mode):        
        if self.num_gpios <= 8:
            self.direction = self._readandchangepin(MCP23008_IODIR, pin, mode)
        if self.num_gpios <= 16:
            if (pin < 8):
                self.direction = self._readandchangepin(MCP23017_IODIRA, pin, mode)
            else:
                self.direction = self._readandchangepin(MCP23017_IODIRB, pin-8, mode)

        return self.direction

    def output(self, pin, value):
        # assert self.direction & (1 << pin) == 0, "Pin %s not set to output" % pin
        if self.num_gpios <= 8:
            self.outputvalue = self._readandchangepin(MCP23008_GPIO, pin, value. self.i2c.readU8(MCP23008_OLAT))
        if self.num_gpios <= 16:
            if (pin < 8):
                self.outputvalue = self._readandchangepin(MCP23017_GPIOA, pin, value, self.i2c.readU8(MCP23017_OLATA))
            else:
                self.outputvalue = self._readandchangepin(MCP23017_GPIOB, pin-8, value, self.i2c.readU8(MCP23017_OLATB))

        return self.outputvalue


        self.outputvalue = self._readandchangepin(MCP23017_IODIRA, pin, value, self.outputvalue)
        return self.outputvalue
        
    def input(self, pin):
        assert pin >= 0 and pin < self.num_gpios, "Pin number %s is invalid, only 0-%s are valid" % (pin, self.num_gpios)
        assert self.direction & (1 << pin) != 0, "Pin %s not set to input" % pin
        if self.num_gpios <= 8:
            value = self.i2c.readU8(MCP23008_GPIO)
        elif self.num_gpios > 8 and self.num_gpios <= 16:
            value = self.i2c.readU16(MCP23017_GPIOA)
            temp = value >> 8
            value <<= 8
            value |= temp
        return value & (1 << pin)

        

class MCP230XX_GPIO(object):
    OUT = 0
    IN = 1
    BCM = 0
    BOARD = 0
    def __init__(self, busnum, address, num_gpios):
        self.chip = Adafruit_MCP230XX(busnum, address, num_gpios)
    def setmode(self, mode):
        # do nothing
        pass
    def setup(self, pin, mode):
        self.chip.config(pin, mode)
    def input(self, pin):
        return self.chip.input(pin)
    def output(self, pin, value):
        self.chip.output(pin, value)
    def pullup(self, pin, value):
        self.chip.pullup(pin, value)
        

if __name__ == '__main__':
    # Use busnum = 0 for older Raspberry Pi's (pre 512MB)
    mcp = Adafruit_MCP230XX(busnum = 0, address = 0x20, num_gpios = 16)


    def set_pins_output(numpins):
       for pin in (range(numpins)):
          mcp.config(pin ,OUTPUT)

	


    def stop(timearg=.5):
       mcp.output(0,0)
       mcp.output(1,0)
       mcp.output(2,0)
       mcp.output(3,0)
       time.sleep(timearg)

    def turn_right(timearg):
       mcp.output(0,1)
       mcp.output(1,0)
       mcp.output(2,0)
       mcp.output(3,0)
       time.sleep(timearg)

    def turn_left(timearg):
       mcp.output(0,0)
       mcp.output(1,0)
       mcp.output(2,1)
       mcp.output(3,0)
       time.sleep(timearg)
 
    def move_backward(timearg):
       mcp.output(0 ,1)
       mcp.output(1 ,0)
       mcp.output(2 ,1)
       mcp.output(3 ,0)
       time.sleep(timearg)

    def move_forward(timearg):
       mcp.output(0,0)
       mcp.output(1,1)
       mcp.output(2,0)
       mcp.output(3,1)
       time.sleep(timearg)


    def test_ports(stopat,delay,numtimes=1):
      for b in (range(numtimes)):  
         for a in (range(stopat)):
           print a 
           mcp.output(a,1)
           time.sleep(delay)
           mcp.output(a,0)

     
    def test_drive():    
      move_forward(1)
      stop()
      turn_right(1)
      stop()
      move_backward(1)
      stop()
      turn_left(1)
      stop()
    



    #set 0-8 output
    #set_pins_output(8) #0- num
    #test_ports(8,.3,3) #num , delay








####################################
while True:
    (sread, swrite, sexec)=select.select(sockets,[],[])
    for s in sread:
        if s == serverSocket:
            acceptConn()
        else:
            msg=s.recv(100)
            if msg.rstrip() == "left":
                 turn_right(1)
                 stop()
            if msg.rstrip() == "right":
                 turn_left(1)
                 stop()
            if msg.rstrip() == "forward":
                 move_backward(1)
                 stop()
            if msg.rstrip() == "backward":
                 move_forward(1)
                 stop()

            if not msg or msg.rstrip() == "quit":
                host,port=s.getpeername()
                msg = 'Client left: %s:%d\n' % (host,port)
                broadcast(msg,s)
                s.close()
                sockets.remove(s)
                del s
            else:
                host,port=s.getpeername()
                broadcast(msg,s)
                continue




