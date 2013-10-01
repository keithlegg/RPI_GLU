# -*- coding: utf-8 -*-
import kl_rpi_base
import kl_rpi_render_webpage
import kl_rpi_fileIO
import kl_rpi_postgis


"""

not a tool per se , but a quick way to build and test tools.

"""



#####################################################

class rpi_terminal:
   def __init__(self):
      self.SERIAL       = kl_rpi_base.kl_rpi_api()
      self.CONFIG       = kl_rpi_base.kl_rpi_config()
      self.DATABASE     = kl_rpi_postgis.pg_datalink()
      self.WORKDIR      = '' #active directory for data
      self.WEBRENDER    = kl_rpi_render_webpage.render_html()
      #####
      self.CONFIG.read_cfg()
      self.uart_enable  = self.CONFIG.ATTR_UART_ENABLE 

 
   #########################
   #OUTPUT (or print)
   def cpr(self,text):
      print text
   ##########################
   #MACROS 



   #########################
   #INTERACTIVE CLI
   def CLI(self):
     command = ''
     split = []
     while command !='quit':
        if command != 'help' :
          print('\n\n')
        self.cpr('########### GIS_BOT : ENTER COMMAND ##################')
        lastcommand = command
        command = str(raw_input() )
        split   = command.split(" ")
        #####################################################
        if command == 'show_cfg' :
            self.SERIAL.show_cfg()
        #####################################################
        if command == 'show_latlon' :
            self.SERIAL.show_latlon()        
        #####################################################
        if command == 'read_uart' :
            self.SERIAL.read_uart()  
       
        #####################################################
        if command == 'pgtest' :
            self.DATABASE.connect()
            #self.DATABASE.show_env()
             
        #####################################################
        #TEST of NMEA to lat lon
        #reads in GPS data from UART , processes and builds a webmap 
        if command == 'renderwebpage' :
           self.WORKDIR = self.SERIAL.CONFIG.ATTR_WORKDIR  #DEBUG -READ FROM CONFIG
           #STANDARD MODE   
           if (self.uart_enable=='true'): 
               self.SERIAL.getXY() #read from serial port
               self.SERIAL.process_to_tmpfile(self.WORKDIR+'/gps_serialized.txt',self.WORKDIR+'/gps_latlon.txt')
           #OFFLINE MODE - use local data file  
           if (self.uart_enable=='false'): 
               print ('#UART IS DISABLED READING FROM '+ (self.WORKDIR+'/samples/gps_serialized.txt' ) )  
               self.SERIAL.process_to_tmpfile( (self.WORKDIR+'/samples/gps_serialized.txt' )   ,self.WORKDIR+'/gps_latlon.txt')  
           ##
           self.SERIAL.internal_nmea_to_dd() #assumes LAT/LON is loaded 
           ######################################## 
           self.WEBRENDER.set_latlon(self.SERIAL.LATDD,self.SERIAL.LONDD)
           self.WEBRENDER.render()
           print (self.WEBRENDER.file_buffer)
           print [self.SERIAL.LATDD,self.SERIAL.LONDD]


        #####################################################
        #TEST of NMEA to lat lon
        if command == 'read_nmea' :
           self.WORKDIR = self.SERIAL.CONFIG.ATTR_WORKDIR  #DEBUG -READ FROM CONFIG
           #STANDARD MODE 
           if (self.uart_enable=='true'):
             print '#CACHING FROM UART DATA' 
             self.SERIAL.getXY() 
             self.SERIAL.process_to_tmpfile(self.WORKDIR+'/gps_serialized.txt',self.WORKDIR+'/gps_latlon.txt')
           #OFFLINE MODE  
           if (self.uart_enable=='false'):
             print ('#UART IS DISABLED READING FROM '+ (self.WORKDIR+'/samples/gps_serialized.txt' ) ) 
             self.SERIAL.process_to_tmpfile( (self.WORKDIR+'/samples/gps_serialized.txt' ) ,self.WORKDIR+'/gps_latlon.txt')
           ##
           print '#created cache file '+ (self.WORKDIR+'/gps_serialized.txt') 
           #GO FIX THE NUMBERS CONVERT NMEA TO DECIMAL DEGREE 
           self.SERIAL.internal_nmea_to_dd()
           print [self.SERIAL.LATDD,self.SERIAL.LONDD]
        #
        #####################################################
        if command == 'about' :
           print '#created Aug 10,2013 Keith Legg'

        if command == 'help' :
           print '## ## ##  ## ## ##  ## ## ##  ## ## ##    '
           print 'show_cfg       : show config internals    '
           print 'show_latlon    : show latlon internals    '           
           print 'read_nmea      : show GPS uart data       '
           print 'read_uart      : dump UART data if active '
           print 'renderwebpage  : render webpage           '   
           
           print 'save_postgis   : render webpage           '   
           print 'save_postgis   : render webpage           '   
           
           #print 'getxy       : get gps lat lon' 
           #print 'updatepg    : gps lat lon -> postGIS' 
           #print 'rendermap   : render static webmap from textfiles' 
      
           #print 'getalt      : get gps altitude'
           #print 'gettime     : get gps universal time'
           #print 'getlocks    : get # of satelitte locks'


           print '## ## ##  ## ## ##  ## ## ##  ## ## ##  '

        #####################################################
        if command == 'exit' or command == 'ex' :
          break
        if split[0] == 'exit' or split[0] == 'ex' :
          break
          
        #####################################################



##############################
foo = rpi_terminal()
foo.CLI()



