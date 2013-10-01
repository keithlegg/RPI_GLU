#!/usr/bin/python           # This is client.py file
# -*- coding: latin-1 -*-

import socket               # Import socket module
import sys

#host = socket.gethostname() # Get local machine name

s = socket.socket()         # Create a socket object
host = '10.0.1.14'
port = 12348               # Reserve a port for your service.


####################################

s.connect((host, port))
print s.recv(1024)

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
####################################
s.close  # Close the socket when done

