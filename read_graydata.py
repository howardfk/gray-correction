#!/usr/bin/env python
import os
import sys
import numpy as np

#creat path to read file
def make_path():
   script_dir = os.path.abspath(__file__)
   script_dir = os.path.dirname(script_dir) #gives you back this files abs path to dir - filename
   return script_dir
   #I will temperatly store my graydata to be anlyise here

def pathtofile(file_name=""):
    print(make_path())

#read in line by line


#Store times into array

#Store power spectra into array

#Combine arrays

#check the data


#runing code

def main():
   pathtofile()

if __name__ == "__main__":
   main()
