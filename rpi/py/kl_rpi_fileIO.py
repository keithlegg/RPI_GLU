import os
import sys
#import sys_kernel


def readArrayFile_py (fileName):
   foo=file_io_three()
   foo.readfilelines(fileName)
   return foo.filecontents
##........................#..###........................#..###........................#..###

def readFile_py (fileName):
   foo=file_io_three()
   foo.readfilelines(fileName)
   return str(foo.filecontents)
   
##........................#..###........................#..###........................#..###

def saveArrayFile_py (filename,text):
   foo=file_io_three()
   print '#writing '+str(filename)+' \n'
   foo.writefile_listlines(filename,text)

###############################################################

##................................................................................
##................................................................................


#def sort_based_on_filesize(folder,extention,MODE):
#    pass
   

###..
#def returnDirectoryInfo():
# pass
###..


# get file information using os.stat()
# tested with Python24 vegsaeat 25sep2006
import os
#import stat # index constants for os.stat() #WTF ???

import time
import os, sys
#from stat import *

#statinfo = os.stat('somefile.txt')
#statinfo()
#statinfo.st_size()



#########################

def getFileSize(file_name):
    statinfo = os.stat(file_name)
    return statinfo.st_size


########################
##DEBUG

def getFileInfo(file_name):
    # pick a file you have ...
    #file_name = 'C:/stateplane.prj'
    statinfo = os.stat(file_name)


    ####
    # islink
    # ismount
    #os.path.join(path1[, path2[, ...]]
    # dirname
    #split
    ##
    DAT_FNAME  = ''# DEBUG "s" % file_info
    DAT_FSIZE  = statinfo.st_size #()''# "file size = %(fsize)s bytes" % file_info
    DAT_FLMOD  = ''# "last modified = %(f_lm)s" % file_info
    DAT_FLACC  = ''# "last accessed = %(f_la)s" % file_info
    DAT_FCREAT = ''# "creation time = %(f_ct)s" % file_info

    #DAT_ISFOLD = statinfo.IS_ISDIR
    
    ######
    out=[]
    out.append(DAT_FNAME)
    #out.append(DAT_ISFOLD)
    out.append(DAT_FSIZE)
    out.append(DAT_FLMOD)
    out.append(DAT_FLACC)
    out.append(DAT_FCREAT)
    ######
    
    print out
    raw_input

    return out
    

##................................................................................
def appendMultiFromList(filelist):
   fhandler = file_io_three()
   files = fhandler.readfile(filelist)
   
   print files
   
   
   
##................................................................................
##................................................................................
##................................................................................
##................................................................................

class file_io_three (object):


 def __init__(self):
   self.filecontents         = '' #data for read/write
   self.filecontents_list    = [] #data for read/write
   self.dir_contents_list    = [] #FOLDER DATA
   self.fileexists           = 0

 ##.........
 def clearall(self):
   self.filecontents         = '' #data for read/write
   self.filecontents_list    = [] #data for read/write
   self.dir_contents_list    = [] #FOLDER DATA
 
 ##............
 def shiftList(self,direction,filepath):
    shifted = []
    #..
    if direction == 'up':
     #listvar = ['a','b','c','d','e','f']
      self.readfilelines(filepath)
      listvar = self.filecontents_list
      shifted = listvar[1:]
      #return shifted
      self.writefile_list(filepath,shifted)
    #..
    if direction == 'down':
      pass
    #
    #print shifted
 ##.........................


 def appendList(self,filepath,data):
   file_object = open (filepath,"a")
   
   for line in data:
     file_object.writelines ('\n'+line)
   file_object.close()
  
 ##.........................
 """
 check for folder to see if it has other folders
 """
 #def checkfolderForfolders (self,filename):
 
 ##.........................
 
 def checkexists (self,filename):
  if os.path.lexists(filename):
    #print "sma_file_io_two::checkexists ", filename ," exists "
    self.fileexists = 1
  else :
    print "sma_file_io_two::checkexists ", filename ," does not exist "
 ##.........................
 #this returns full path names of folders in a folder
 def get_fullpath_dirs_dir (self,foldervar):
  output = []
  if os.path.lexists(foldervar)==0:
    print 'get_directories_dir does not exist'
  if os.path.lexists(foldervar):
    folders = os.listdir(foldervar)
    for folder in folders:
     iterator = (foldervar+'/'+folder)
     #print iterator
     if os.path.isdir(iterator):
       output.append(iterator)
    return output
  else :
    print "get_fullpath_dirs_dir failed "
 ##.........................
 ##.........................
 """
  #NON RECURSIVE SEARCH OF FOLDERS
  #this returns only folder names in a folder (not full path)
  retunrs full path names
 """
 
 def get_directories_dir (self,foldervar):
  output = []
  print 'DEBUG DIR IS '
  print foldervar

  if os.path.lexists(foldervar)==0:
    print 'get_directories_dir "'+foldervar+'" does not exist'
  if os.path.lexists(foldervar):
    folders = os.listdir(foldervar)
    for folder in folders:
     iterator = (foldervar+'/'+folder)
     #print iterator
     if os.path.isdir(iterator):
       output.append(folder)
    return output
  else :
    print "get_directories_dir failed "
 ##.........................
 """
  #RECURSIVE SEARCH OF FOLDERS
  #build a list of folders in a folder
  #this returns only folder names in a folder (not full path)
  
 """
 def recurse_directories_dir (self,foldervar):
    self.dir_contents_list.append(foldervar) #store folder tree in .self (member var)
    if len(foldervar) !=0:
     CONTENTS = self.get_fullpath_dirs_dir(foldervar)
     if CONTENTS!=None:
        for FOLDER in CONTENTS:
            self.recurse_directories_dir(FOLDER)
    else :
      print "get_directories_dir failed "
 ##.........................
 def getcontentsdir (self,folder):
  if os.path.lexists(folder):
     self.dir_contents_list = [] #debug
     for filel in os.listdir(folder):
       self.dir_contents_list.append(filel)

  else :
    print "does not exist "
  #return  self.dir_contents_list
 ##..........
 #same as getcontentsdir_filter without the full path names
 def getcontentsdir_filter_nofp (self,folder,filterstr):
  if os.path.lexists(folder):
     dir_cnts_list = []
     for filel in os.listdir(folder):
       lensfx = len(filterstr)
       lenpfx = len(filel)-lensfx
       prefix = filel[0:lenpfx]
       suffix = filel[lenpfx:]

       if suffix == filterstr:
         if filel !='':
           dir_cnts_list.append( filel )
           #print '#debug# getcontentsdir_filter MATCH FOUND '+prefix[:-1] +'\n'
     #self.dir_contents_list = dir_cnts_list #DEBUG
     return dir_cnts_list
     
 ##..........
 """
 #returns all files of a given extention
 non recursive, returns the names of files in a folder ONLY if they match the filterstring arg
 returns full path names
 """
 def getcontentsdir_filter (self,folder,filterstr):      
  if os.path.lexists(folder):
     dir_cnts_list = []
     for filel in os.listdir(folder):
       lensfx = len(filterstr)
       lenpfx = len(filel)-lensfx
       prefix = filel[0:lenpfx]
       suffix = filel[lenpfx:]
       if suffix == filterstr:
         if filel !='':
           dir_cnts_list.append( (folder+'/'+filel) )
           #print '#debug# getcontentsdir_filter MATCH FOUND '+prefix[:-1] +'\n'
     #self.dir_contents_list = dir_cnts_list #DEBUG
     return dir_cnts_list
     
  ##

  else :
    print "does not exist "
 ##..........
 """
 return ALL files of extention recusrively
 """
 def recurse_contentsdir_filter (self,folder,filterstr):
   self.clearall() #debug this may cause trouble ??
   self.recurse_directories_dir(folder)
   FOLDERS = self.dir_contents_list
   RECUROUT =[] #output of the function
   #DEBUG
   if folder==None:
     return RECUROUT
   #DEBUG
   for folder in FOLDERS:
     temp = self.getcontentsdir_filter(folder,filterstr)
     if temp==None:
        return RECUROUT
     #RECUROUT.append( temp )
     #print 'DEBUG '
     #print temp
     for item in temp:
       RECUROUT.append(item)

   return RECUROUT
 ##..........
 def readfile (self,path):
   if os.path.lexists(path)==0:
      print (path, " DOES NOT EXIST !! " )
   if os.path.lexists(path):
    if len(path) ==0:
      print ("sma_file_io_two::readfile INFILENAME NOT DEFINED")
    else:
      print 'reading...'
      f = open( path,"r")
      self.filecontents = f.readlines() 
 ##..........

 def readfilelines (self,path):
   if os.path.lexists(path)==0:
      print (path, " DOES NOT EXIST !! " )
   if os.path.lexists(path):
    if len(path) ==0:
      print ("sma_file_io_two::readfile INFILENAME NOT DEFINED")
    else:
      f = open( path,"r")
      self.filecontents = f.readlines() 
      for x in self.filecontents :
        #lines = x.split(" ")
        nonewline = x.split('\n')
        self.filecontents_list.append(nonewline[0])
 ##..........
 def serialize(self):
     temp = ''
     for x in self.filecontents_list:
        temp = temp+x
     return temp

 ##..........
 ## USE {  }  
 def readfile_split_lines (self,path):
   nonewlines =[]
   if os.path.lexists(path)==0:
      print (path, " DOES NOT EXIST !! " )
   if os.path.lexists(path):
    if len(path) ==0:
      print ("sma_file_io_two::readfile INFILENAME NOT DEFINED")
    else:
      f = open( path,"r")
      self.filecontents = f.readlines() 
      for x in self.filecontents :
        lines = x.split(" ")
        for y in lines :
          if y!='\n':
           self.nonewlines.append( y )
        #print 'LINES ',lines

      block = []

    for x in self.nonewlines :
       if x =="{" :
         print "BLOCK IN "
       if x =="}" :
         print "BLOCK OUT "
       print "x is ",x


 ##...................##

 def writefile_str (self,path,text):
  file_object = open (path,"w")
  file_object.write (text)
  file_object.close()

 ##...................##

 def writefile_list (self,path,listvar):
  file_object = open (path,"w")
  file_object.writelines (listvar)
  file_object.close()

 ##...................##

 def writefile_listlines (self,path,listvar):
  file_object = open (path,"w")
  #file_object.writelines (listvar)
  for line in listvar:
      if line != '\n' and line !='':
        #file_object.write(line+'\n')
        if len(line):
          file_object.write('\n'+str(line))
  file_object.close()


