#!/usr/bin/env python
# -*- coding: utf-8 -*-


import serial
import time
import kl_rpi_fileIO
import kl_rpi_postgis

import random

#import psycopg2

#import string

####################################

"""
 "FME" for GPS DATA from textfiles or datastreams

 ############## 
 #BASIC PACAKGE REQUIRES:
 pyserial
 pyscopg2

 ############## 
 #WEBSERVER MODULE
 postgis
 apache
 wsgi
 openlayers
 php
 proj4js
 ############## 
 extjs ?

"""

####################################
#DEBUG ADD PINAMPS 
####################################

class kl_rpi_config:
    def __init__(self):
         #self.config             = '/home/pi/rpi_config.conf'
         self.config             = '/home/keith/rpi_config.conf'
         self.BUFFERSIZE         = 256
         self.fileio             = kl_rpi_fileIO.file_io_three()
         self.ATTR_MACID         = '' #machine id
         self.ATTR_PORT          = '' #serial port on machine
         self.ATTR_UART_ENABLE   = '' #run offline
         self.ATTR_WORKDIR       = '' #terminal working directory 
         self.ATTR_HTDOCS        = '' #web server path 
         self.ATTR_WEBPAGE       = '' #web page name 
         ######################################
         self.ATTR_PGDB_USER     =''  #databse user
         self.ATTR_PGDB_DBNAME   =''  #databse name
         self.ATTR_PGDB_TBNAME   =''  #database table name 
         self.ATTR_PGDB_PASSWD   =''  #?


    #######################################
    def read_cfg(self):
         self.fileio.readfilelines(self.config)
         for line in  self.fileio.filecontents_list:
           linesplit = line.split(' ')
           count = 0
           for x in linesplit:
              if (x=='CFG_MACID'):
                self.ATTR_MACID =  linesplit[count+1]
              if (x=='CFG_UART_ENABLE'):
                self.ATTR_UART_ENABLE =  linesplit[count+1]

              if (x=='CFG_PORT'):
                self.ATTR_PORT=  linesplit[count+1]
              if (x=='CFG_WORKDIR'):
                self.ATTR_WORKDIR=  linesplit[count+1]
              if (x=='CFG_HTDOCS'):
                self.ATTR_HTDOCS=  linesplit[count+1]
              if (x=='CFG_WEBMAP'):
                self.ATTR_WEBPAGE=  linesplit[count+1]
              #########################################
              #DB STUFF  
              if (x=='CFG_PGDB_DBNAME'):
                self.ATTR_PGDB_DBNAME=  linesplit[count+1]              
              if (x=='CFG_PGDB_TBNAME'):
                self.ATTR_PGDB_TBNAME=  linesplit[count+1]
              if (x=='CFG_PGDB_USER'):
                self.ATTR_PGDB_USER=  linesplit[count+1]
              if (x=='CFG_PGDB_PASSWD'):
                self.ATTR_PGDB_PASSWD=  linesplit[count+1]
 
              count = count+1

    #######################################
    def show_cfg(self):
        self.read_cfg()
        print ('config is         : '+ self.config); 
        #print '##  ## ## ## ## ## ## ## ## ## ## ## ## ##';
        print ('MACHINE NAME      : '+self.ATTR_MACID)
        print ('SERIAL PORT       : '+self.ATTR_PORT)
        print ('UART ENABLE       : '+self.ATTR_UART_ENABLE)
        print ('WORKING DIRECTORY : '+self.ATTR_WORKDIR)
        print ('WEB DIRECTORY     : '+self.ATTR_HTDOCS)
        print ('WEB NAME          : '+self.ATTR_WEBPAGE)
        print ('DB  NAME          : '+self.ATTR_PGDB_DBNAME)
        print ('TABLE NAME        : '+self.ATTR_PGDB_TBNAME)
        print ('DB PASSWORD       : '+self.ATTR_PGDB_PASSWD)



####################################
class kl_rpi_api:
    def __init__(self):
        self.fileio       = kl_rpi_fileIO.file_io_three()
        self.pg_link      = kl_rpi_postgis.pg_datalink()
        self.CONFIG       = kl_rpi_config()
        
        self.RANDOMIZE    = 1 #THIS WILL RANDOMIZE THE GPS COORDINATES A LITTLE - DEFAULT OFF
        ##FROM NMEA - (a bit FUNKY)
         
        #BETTER TO STORE THESE AS FLOAT AND CONVERT TO STRING WHEN USED 
        self.LAT          = 0 #latitude
        self.LON          = 0 #longitude
        ##CONVERTED TO DECIMAL DEGREES
        self.LATDD        = 0 #latitude
        self.LONDD        = 0 #longitude
        self.ALT          = 0 #altitude
        self.TIME         = 0 #universal standard time
        ##file buffer 
        self.FIO_BUFFER   = []
        self.RX_BUFFER    = ''
        self.GPS_TMP_FILE = 'gps_serialized.txt' 
        ######
        self.CONFIG.read_cfg() 
        if (self.CONFIG.ATTR_UART_ENABLE=='true'):
          self.PORT         = self.CONFIG.ATTR_PORT  #'/dev/ttyAMA0'   #DEBUG READ FROM CONFIG
          self.BAUD         = 9600
          self.UART         = serial.Serial(self.PORT,self.BAUD)


    #######################################
    def show_cfg(self):
         self.CONFIG.show_cfg() 
    #######################################
    #fer debugging
    def show_latlon(self):
         print 'NMEA LAT '+str(self.LAT)
         print 'NMEA LON '+str(self.LON)
         print 'DDLAT    '+str(self.LATDD)
         print 'DDLON    '+str(self.LONDD)
         
         
    #######################################
    def init_uart(self):
      self.UART.open()

    def shutoff_uart(self):
      self.UART.close()


    #######################################
     #mockup of a read uart function - MUCH TO DO - DEBUG!
     #TODO access from terminal - send or recieve a byte 

    def rx(self): #,uart,baud):
        self.init_uart()
        self.RX_BUFFER = ( self.UART.read( self.CONFIG.BUFFERSIZE ) )

    #######################################
    #def rx_gps(self): #,uart,baud):
    #    self.init_uart()
    #    self.RX_BUFFER = ( self.UART.read(1024) )

    #######################################
    #recieve one character (uartnum,baudrate)
       #debug 
    #######################################
    #transmit one character (uartnum,baudrate, data)
    def tx(self,uart,baud,char):
      pass
    #######################################
    def trunc(self,f, n):
       slen = len('%.*f' % (n, f))
       return str(f)[:slen]

    #######################################
    #	    NMEA	      Decimal
    #lat    0302.78469	03  + (02.78469/60) = 3.046412
    #lon    10141.82531	101 + 41.82531/60)  = 101.6971
    #       NOTES :
    # if WEST  of prime meridian than its negative for longitude ?
    # if SOUTH of prime meridian than its negative for latitude  ?


    def nmea_to_decdegree(self,degrees,minutes):
         outdegrees = 0.0
         outdegrees = degrees + (minutes/60) 
         return outdegrees
    #######################################
     #fer debugging 
    def read_uart(self):
       if (self.CONFIG.ATTR_UART_ENABLE=='true'):
         self.rx()
         print self.RX_BUFFER
       else:
         print '#UART IS DISABLED - CHECK RPI_CONFIG'  
    #######################################
    #['4402.4876', '12257.6856']

    def internal_nmea_to_dd(self):
        numchar_lat = 2 #HOW MANY TO STRIP OFF (44)
        numchar_lon = 3 #HOW MANY TO STRIP OFF (-122) 
        numtrunc    = 5 #PRECISION (# TO TRUNCATE  )

        len_lat = 0 
        tmp_lat = str(self.LAT)
        len_lat = len(tmp_lat)

        #assume first two numbers are degree (west coast USA) 
        deg_str=tmp_lat[0:numchar_lat]
        min_str=tmp_lat[len_lat-(len_lat-numchar_lat):]
        #if (type(deg_str) =='str'):
        self.LATDD  = (float(deg_str) + (float(min_str)/60) ) #convert to decimal degree
        self.LATDD=self.trunc(self.LATDD,numtrunc)

        #negate the value if west of prime meridian? 
        #self.LATDD=-self.LATDD

        ######
        len_lon = 0 
        tmp_lon = str(self.LON)
        len_lon = len(tmp_lon)
        #assume first three numbers are degree (north west USA) 
        deg_str=tmp_lon[0:numchar_lon]
        min_str=tmp_lon[len_lon-(len_lon-numchar_lon):]
        self.LONDD  = (float(deg_str) + (float(min_str)/60) ) #convert to decimal degree
        #negate the value if west of prime meridian? 
        self.LONDD=-self.LONDD        
        self.LONDD=self.trunc(self.LONDD,numtrunc)
        
        if (self.RANDOMIZE):
	   self.LATDD=float(self.LATDD)+random.uniform(.05,.001)
	   self.LONDD=float(self.LONDD)+random.uniform(.05,.001) 
	
	  
        print ('#input     NMEA: '+str(self.LAT)  +' '+str(self.LON)   )
        print ('#output lat/lon: '+str(self.LATDD)+' '+str(self.LONDD) )

        
    #######################################
    #THIS IS DEGREES , MINUTES , SECONDS - TODO - CONVERT TO DECIMAL DEGREES
    def extract_lat_lon(self,char_array):
      count = 0
      numlinesfound = 0

      #foo = char_array.split('@')
      foo = char_array.split('$')
      for a in foo:
        #if (a[0:6]=='$GPGGA'):
        if (a[0:5]=='GPGGA'):
            b= a.split(',')
            for c in b:
                if c=='N': 
                  self.LAT= b[count-1] #N data
                if c=='W': 
                  self.LON= b[count-1] #W data
                #print('DATA IS '+c) #USE TO DEBUG 
                ##
                count=count+1
        numlinesfound=numlinesfound+1
        count = 0
      print('# processed '+str(numlinesfound)+ ' lines of gps data ($GPGGA) ')  #debug
      print('# extracted '+str(self.LAT)+' '+str(self.LON) ) 
    #######################################
    def getXY(self):
      self.rx()
      print ('creating cache '+(self.CONFIG.ATTR_WORKDIR+'/'+self.GPS_TMP_FILE) )
      self.fileio.writefile_list( (self.CONFIG.ATTR_WORKDIR+'/'+self.GPS_TMP_FILE) ,self.RX_BUFFER);
 
      #return [self.LAT,self.LON]
 
    #######################################
    #read from a file
    def read_textfile(self,fname):
       self.fileio.readfilelines(fname) 
       return( self.fileio.serialize() )
    #######################################
    #just an example of how to hook all the methods together
    def process_to_tmpfile(self,infname,outfname):
       rawtxt = self.read_textfile(infname)
       self.extract_lat_lon( rawtxt ) #read from a file for now
       self.FIO_BUFFER.append(str(self.LAT)+' '+str(self.LON))
       self.fileio.writefile_list(outfname,self.FIO_BUFFER)

    #######################################
    #CALCULATE A DISTANCE/BEARING - not totally unrelated 
    def arc_to_degree(self,NS,degrees,minutes,seconds,EW):
	  outdegrees = 0.0
	  if NS =='n':
	    outdegrees = degrees
	    outdegrees = outdegrees + (minutes*.0166667) #1/60
	    outdegrees = outdegrees + (seconds*.0166667*.0166667) #1/60

	  if NS =='s':
	    outdegrees = 180.0
	    outdegrees = outdegrees + degrees
	    outdegrees = outdegrees + (minutes*.0166667) #1/60
	    outdegrees = outdegrees + (seconds*.0166667*.0166667) #1/60

	  if EW =='w' and NS =='s':
	     outdegrees = outdegrees * -1

	  ###?
	  if EW =='e' and NS =='n':
	     outdegrees = outdegrees * -1
	     

	  return outdegrees


    #######################################
    #######################################
    #dump data to postgis
    def dump_postgis(self,fname):      
       self.extract_lat_lon(self.read_gps_textfile(self.CONFIG.ATTR_WORKDIR+'/sample_data.txt') ) #read from a file for now
       self.FIO_BUFFER.append(self.LAT+' '+self.LON)
       #self.fileio.writefile_list(fname,self.FIO_BUFFER) 
       #dump_postgis
    #######################################
    #######################################










