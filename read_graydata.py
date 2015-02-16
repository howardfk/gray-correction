#!/usr/bin/env python
import os
import sys
import numpy as np

#creat path to read file
def make_path(file_name):
   script_dir = os.path.abspath(__file__)
   script_dir = os.path.dirname(script_dir) #gives you back this files abs path to dir - filename
   script_dir = os.path.join(script_dir,data/file_name)
   return script_dir
   #I will temperatly store my graydata to be anlyise here

def pathtofile(file_name=""):
    return make_path(file_name)

#length of entire file
def howlongisfile(file_in):
   with open(file_in, r) as f:
      for i in enumerate(f,1):
         pass
      else:
         return i[0]

#read in line by line
def filetoarray(file_in):
   filelength = howlongisfile(file_in)
   data_array[0]*filelength

#Store times into array

#Store power spectra into array

#Combine arrays


#check the data


#runing code

def main():
   pathtofile("20140611-223001-SPS.data.2.5MHz.data.021925.avg4096.graydata")

if __name__ == "__main__":
   main()
