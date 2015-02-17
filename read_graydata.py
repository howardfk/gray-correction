#!/usr/bin/env python
import os
import sys
import numpy as np

#creat path to read file
def make_path(file_name):
   script_dir = os.path.abspath(__file__)
   script_dir = os.path.dirname(script_dir) #gives you back this files abs path to dir - filename
   script_dir = os.path.join(script_dir,'data', file_name)
   return script_dir
   #I will temperatly store my graydata to be anlyise here

def pathtodata(file_name=''):
   return make_path(file_name)

#length of entire file
def howlongisfile(file_in):
   with open(file_in, 'r') as f:
      for i in enumerate(f,1):
         pass
      else:
         return i[0]

#read in graydata line by line
def datatoarray(pathToData, sampleFreq, binNum, fftAvg):
   filelength = howlongisfile(pathToData)
   data_array = np.zeros(filelength)
   with open(pathToData,'r') as f:
      data_array = f.readlines()
   return data_array

def converttomatrix(pathToData, sampleFreq, binNum, fftAvg):
   data_array = datatoarray(pathToData, sampleFreq, binNum, fftAvg)
   num_spectra = np.size(data_array)*2/binNum
   print "number of spectra",num_spectra
   power_matrix = np.zeros(num_spectra)
   return data_array

#Store times into array
#Store power spectra into array
#Combine arrays
#check the data


#runing code
def main():
   sampleFreq = raw_input("Sampiling Freuancy:")
   sampleFreq = int(sampleFreq)
   binNum = raw_input("Number of Bins for the FFT: ")
   binNum = int(binNum)
   fftAvg = raw_input("Number of averging for FFT: ")
   fftAvg = int(fftAvg)
   cwd=pathtodata("20140611-223001-SPS.data.2.5MHz.data.021925.avg4096.graydata")
   data_array = converttomatrix(cwd, sampleFreq, binNum, fftAvg)
   #data_array = datatoarray(cwd, sampleFreq, binNum, fftAvg)
   i=0
   for i in range(0,5):
      print data_array[i]

if __name__ == "__main__":
   main()
