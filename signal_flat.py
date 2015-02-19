#!/usr/bin/env python

#take in some 2-D matrix and look for the 10khz signal

#FFT samples = N-bins (call by core)
#FFT bins = N-bins/2 
#find the singal  FreqRez = Fsample / FFT samples    TimeRez = (FFTs/Fs)*averages


#find_signal
def find_signal(ffts, freqs, signal = 100000, binindex =""):
   if binindex =="":
      freqrez = freqs/ffts
      #write something to check for the correct bin
      #for now we can hard code it
      return binindex
   else:
      return binindex 

def power_lvl(datamatrix,time_ind,bin1,bin2="" ):
   if bin2 =="":
      return 100 - datamatrix[time_ind][bin1]
   else:
      power = 100 - (datamatrix[time_ind][bin1] + datamatrix[time_ind][bin2])/2

#flatten corrects for a signal that shoudl be fixed at a power (for south pole vlf power = 100 mv)
def flatten(datamatrix, time_ind, spec_inx):
   power = power_var(datamatrix, time_ind, spec_inx)
   return 100 - power   #add this value to all values in this spectra at time time_ind
