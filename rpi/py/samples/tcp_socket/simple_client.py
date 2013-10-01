import socket                # Import socket module
import sys

#NETWORK SOCKET CODE
s = socket.socket()          # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '10.0.1.14'
port = 12345                  # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done



