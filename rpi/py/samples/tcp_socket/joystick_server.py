#!/usr/bin/python

import socket
import select
import sys
#import time


host = '10.0.1.14'
port = 12348

####################################
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1024)
serverSocket.bind(('',port))
serverSocket.listen(5)

sockets=[serverSocket]
print 'Server is started on port' , port,'\n'

def acceptConn():
    newsock, addr = serverSocket.accept()
    sockets.append(newsock)
    newsock.send('You are now connected to the server\n')
    msg = 'Client joined: %s:%d\n' % addr
    broadcast(msg, newsock)

def broadcast(msg, sourceSocket):
    for s in sockets:
        if (s != serverSocket and s != sourceSocket):
            s.send(msg)
    sys.stdout.write(msg)
    sys.stdout.flush()


####################################
  #PUT OTHER CODE HERE 

def turn_right(inp):
   print 'RIGHT TURN!'

def turn_left(inp):
   print 'LEFT TURN!'

def move_backward(inp):
   print 'BACKUP!'

def move_forward(inp):
   print 'MARCH FORWARD!'

def stop():
   print 'STAHP !!!!'

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


################################



