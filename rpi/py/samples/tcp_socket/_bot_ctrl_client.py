#!/usr/bin/python           # This is client.py file
# -*- coding: latin-1 -*-

#http://docs.python.org/2/library/socket.html
#http://www.tutorialspoint.com/python/python_networking.htm
#http://hackshark.com/?p=147#axzz2dgVBQCeB



import socket                # Import socket module
import sys

#NETWORK SOCKET CODE
s = socket.socket()          # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '10.0.1.27'
port = 1000                  # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)



#http://hackshark.com/?p=147#axzz2C9PuSHTi
#READ JOYSTICK CODE
pipe = open('/dev/input/js0','r')
action = []
spacing = 0
while 1:
        for character in pipe.read(1):
                #action += [character]
                action += ['%02X' % ord(character)]
                if len(action) == 8:
                        for byte in action:
                                #sys.stdout.write('%02X ' % ord(byte))
                                #print ('%02X ' % ord(byte))
                                #print action 

                                if action[4]=='FF':
                                   if action[5]=='7F':
                                     if action[6]=='02':
                                       if action[7]=='00':
                                         print 'joyjoy right '
                                         s.send('right \n')
                                         break
                                       if action[7]=='01':
                                         print 'joyjoy down '
                                         s.send('backward \n')
                                         break 

                                if action[4]=='01':
                                   if action[5]=='80':
                                     if action[6]=='02':
                                       if action[7]=='00':
                                         print 'joyjoy left' 
                                         s.send('left \n')
                                         break           
                                       if action[7]=='01':
                                         print 'joyjoy up'
                                         s.send('forward \n')
                                         break           
 
                                if action[6]=='01':
                                    if action[7]=='00':
                                      print 'button 1'
                                      s.send('button1 \n')
                                      break
                                    if action[7]=='01':
                                      print 'button 2'
                                      s.send('button2 \n')
                                      break
 
                                    #if action[7]=='03':


                                ###

                        #spacing += 1
                        #if spacing == 2:
                        #        sys.stdout.write('\n')
                        #        spacing = 0
                        sys.stdout.write('\n')
                        sys.stdout.flush()
                        action = []





s.close                     # Close the socket when done




######################################

######################################
"""
#SCAN HARDWARE VIA PIPES
######################################
# cat /dev/input/js0
######################################
import sys
pipe = open('/dev/input/js0','r')
while 1:
        for character in pipe.read(1):
                sys.stdout.write(repr(character))
                sys.stdout.flush()
"""

######################################
"""
#ADDS PRETTY SPACING BY 8 VALUES
import sys
pipe = open('/dev/input/js0','r')
action = []
spacing = 0
while 1:
        for character in pipe.read(1):
                action += [character]
                if len(action) == 8:
                        for byte in action:
                                sys.stdout.write('%02X ' % ord(byte))
                        spacing += 1
                        if spacing == 2:
                                sys.stdout.write('\n')
                                spacing = 0
                        sys.stdout.write('\n')
                        sys.stdout.flush()
                        action = []


"""

######################################

"""
#TCP SERVER 
#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 11219               # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)

s.send('f off server! from client!')

s.close                     # Close the socket when done


"""
######################################


######################################



