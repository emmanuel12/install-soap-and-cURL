#!/usr/bin env python

import os   
import subprocess
import sys

def install():
    global install 
    try:
        subprocess.check_output("curl -V",shell=True)
        print "cURL already installed"
    
    except:
        a = raw_input("install cURL, yes or no? ")
        if a == "yes":
           cc = raw_input("install cURL from source or from the library, 's' for source and 'l' for library?")
           if cc == "s":
               tt = raw_input("install cURL from source directory, or download latest one? If from source directory, then enter directory path, leave blank if you just want to download the latest one.")
               if tt == '':
                   print "installing cURL..."
                   os.system("mkdir cURL")    
                   if len(c) == 1:
                      os.system("cd cURL;wget 'http://curl.haxx.se/download/curl-7.31.0.tar.gz'")
                    
                   da = subprocess.check_output("ls cURL",shell=True)
                   os.system("tar -xvf cURL/%s;cd cURL;./configure;make;sudo make install"%da.split('\n')[0])
                   print "cURL installed"
                             
           
           elif cc == "l":
                print "installing cURL"
                os.system("yum install curl")
                print "cURL installed"
                      
              
             
    aa = raw_input("install php-soap, yes or no? ")         
    if aa == "yes":
       os.system("yum install php-soap")
        
                     
              
if __name__ == '__main__':
    install()
                 
