#!/usr/bin/env python

#take in some 2-D matrix and look for the 10khz signal

#FFT samples = N-bins (call by core)
#FFT bins = N-bins/2 
#find the singal  FreqRez = Fsample / FFT samples    TimeRez = (FFTs/Fs)*averages


#find_signal
def find_signal(ffts, freqs, signal = 100000, binindex ="")
   if binindex =="":
      freqrez = freqs/ffts
      #write something to check for the correct bin
      #for now we can hard code it
      return binindex
   else:
      return binindex 

#flatten corrects for a signal that shoudl be fixed at a power (for south pole vlf power = 100 mv)
def flatten(corection, spec_inx):
   #loop data over one spectra
   #2dmatri[i][j]=2dmatrix[i][j]+correction
   #not sure if spec_inx will be collom or row



#optamize
