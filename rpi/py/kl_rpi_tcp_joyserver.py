#!/usr/bin/python

import socket
import select
import sys
#import time



class joystick_tcp_server:
     def __init__(self,hostnam,portnum):
        self.host = hostnam #'10.0.1.14'
        self.port = portnum #12349
        self.setup()
        self.listen()
        self.sockets = null

     ####################################
     def setup(self):
	serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1024)
	serverSocket.bind(('',self.port))

        #CLOSE IF ALREADY OPEN 
        #serverSocket.close() 

	serverSocket.listen(5)
        self.sockets=[serverSocket]
        print 'Server is started on port' , self.port,'\n'

     ####################################
     def acceptConn():
	  newsock, addr = serverSocket.accept()
	  sockets.append(newsock)
	  newsock.send('You are now connected to the server\n')
	  msg = 'Client joined: %s:%d\n' % addr
	  broadcast(msg, newsock)
     ####################################
     def broadcast(msg, sourceSocket):
	    for s in sockets:
		if (s != serverSocket and s != sourceSocket):
		    s.send(msg)
	    sys.stdout.write(msg)
	    sys.stdout.flush()

     ####################################
     #PUT OTHER CODE HERE 

     def turn_right(inp):
       #print 'RIGHT TURN!'
       pass

     def turn_left(inp):
       #print 'LEFT TURN!'
       pass

     def move_backward(inp):
       #print 'BACKUP!'
       pass

     def move_forward(inp):
        #print 'MARCH FORWARD!'
        pass

     def stop():
       #print 'STAHP !!!!'
       pass

     ####################################
     def listen(self):
	while True:
	    (sread, swrite, sexec)=select.select(self.sockets,[],[])
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
		        msg = 'Client left: %s:%d\n' % (self.host,self.port)
		        broadcast(msg,s)
		        s.close()
		        sockets.remove(s)
		        del s
		    else:
		        self.host,self.port=s.getpeername()
		        broadcast(msg,s)
		        continue


################################



