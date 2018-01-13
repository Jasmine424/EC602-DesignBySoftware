# Copyright 2017 Simin Zhai siminz@bu.edu
# Copyright 2017 Zulin Liu liuzulin@bu.edu
# Copyright 2017 James Fallacara jafallac@bu.edu
from __future__  import division
import numpy
from numpy import pi,cos,sin,linspace,ones_like,zeros_like

def loudest_band(music,frame_rate,bandwidth):
    freq_music=numpy.fft.fft(music)
    freq_music_abs=numpy.float32(numpy.abs(freq_music))
#    print(freq_music_abs)
#    print(freq_music_abs[30])
    n=len(freq_music_abs)
#    print(n)
    freq=numpy.float32(numpy.fft.fftfreq(n,1/frame_rate))
#    print(freq)
    freq_step=freq[1]-freq[0]
#    print(freq_step)
    num=int(bandwidth//freq_step)+1
#    print(num)
    sum_band=numpy.float64(0)
    max_sum_band=0
    low_index=0
    high_index=0
    low=0
    high=0
#    print(freq_music_abs[25:36])
#    print(sum(freq_music_abs[0:1]))
    for i in range(num):
        sum_band += freq_music_abs[i]**2
    
#    print(sum_band)
#    print(freq_music_abs[0:num])
#    print(freq_music_abs[2:12])
#    print(sum_band)
    max_sum_band=sum_band
    high=freq[num-1]
    high_index=num-1
    for i in range(1, ((n-1)//2+ 1-num+1) ):
        sum_band -=freq_music_abs[i-1]**2
        sum_band +=freq_music_abs[i+num-1]**2
#        if(i==30):
#            print(sum_band)
#            print(freq_music_abs[30])
#            print(max_sum_band)
#            print(low,high)
        if sum_band>=max_sum_band:
            max_sum_band=sum_band
            low=freq[i]
            low_index=i
            high=freq[i+num-1]
            high_index=i+num-1
#            print(freq_music_abs[low_index:high_index+1])
#            print(low,high)
#            print(sum_band)
    if low_index>0 and high_index<(n-1)//2:
        freq_music[0:low_index]=0
        freq_music[-low_index+1:]=0
        freq_music[high_index+1:(n-1)//2+1]=0
        freq_music[(n-1)//2+1:n-1-high_index+1]=0   
    elif low_index==0:
        freq_music[high_index+1:(n-1)//2+1]=0
        freq_music[(n-1)//2+1:n-1-high_index+1]=0
    elif high_index==(n-1)//2:
        freq_music[0:low_index]=0
        freq_music[-low_index+1:n]
    loudest=numpy.fft.ifft(freq_music)
    return low, high, loudest

#if __name__ == '__main__':
##    x = numpy.linspace(0, 0.5 * numpy.pi, 100) 
##    wave = numpy.cos(x)
##    low ,high , loudest =loudest_band(wave,100,30)
#    frame_rate,T,ftest,bandwidth = 10000,1,100,10
#    t = linspace(0,T,T*frame_rate,endpoint=False)
#    m = zeros_like(t)
#    for a,f in [(1,10),(1,11),(1,12),(2,30)]:
#        m += a*cos(2*pi*f*t)
#    low,high,loudest = loudest_band(m,frame_rate,bandwidth)
#    print(low)
#    print(high)
#    print(loudest)
            