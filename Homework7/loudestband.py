# Copyright 2017 Simin Zhai siminz@bu.edu
# Copyright 2017 Zulin Liu liuzulin@bu.edu
# Copyright 2017 James Fallacara jafallac@bu.edu

import numpy


def loudest_band(music,frame_rate,bandwidth):
    freq_music=numpy.fft.fft(music)
    freq_music_abs=numpy.float32(numpy.abs(freq_music))
    n=len(freq_music_abs)
    freq=numpy.float32(numpy.fft.fftfreq(n,1/frame_rate))
    freq_step=freq[1]-freq[0]
    num=int(bandwidth//freq_step+1)
    sum_band=0
    max_sum_band=0
    low_index=0
    high_index=0
    low=0
    high=0
    for i in range((n-1)//2-num+1 ):
        sum_band -=freq_music_abs[i-1]
        sum_band +=freq_music_abs[i+num-1]
        
        if(sum_band>max_sum_band):
            max_sum_band=sum_band
            low=freq[i]
            low_index=i
            high=freq[i+num-1]
            high_index=i+num-1
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

# if __name__ == '__main__':
#     x = numpy.linspace(0, 0.5 * numpy.pi, 100) 
#     wave = numpy.cos(x)
#     low ,high , loudest =loudest_band(wave,100,30)
#    print(low)
#    print(high)
#    print(loudest)
            