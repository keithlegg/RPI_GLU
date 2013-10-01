import socket
import select
import sys



################################


#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '10.0.1.14'
print ('#host address is '+ host)
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()                # Close the connection


"""

port = 1000
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

"""

################################


