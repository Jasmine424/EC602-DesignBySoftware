import wave
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show
import numpy as np
import os


f = wave.open('bach10sec.wav','rb')
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
strData = f.readframes(nframes)
waveData = np.fromstring(strData,dtype=np.int16)
waveData = waveData*1.0/(max(abs(waveData)))
# waveData = np.reshape(waveData,[nframes,nchannels]).T
# f.close()
# plot the wave
time = np.arange(0,nframes)*(1.0 / framerate)

xf = np.fft.fft(waveData)  
# print np.all(np.abs(np.fft.ifft(xf) - waveData) < 10 ** -9)
plot(xf)

show()
# xf_abs = np.fft.fftshift(abs(xf))  
# axis_xf = np.linspace(-N/2,N/2-1,num=N)  
# plt.specgram(waveData[0],Fs = framerate, scale_by_freq = True, sides = 'default')
# pl.subplot(223)  
# pl.title()  
# pl.plot(waveData,xf)  
# # pl.axis('tight')  
  


# plt.plot(time,waveData)
# plt.xlabel("Time(s)")
# plt.ylabel("Amplitude")
# plt.title("Single channel wavedata")
# plt.grid('on')
# plt.specgram(waveData[0],Fs = framerate, scale_by_freq = True, sides = 'default')
# plt.ylabel('Frequency(Hz)')
# plt.xlabel('Time(s)')
# plt.show()

# import numpy as np
# from scipy.integrate import quad,dblquad,nquad
# import wave
# filename = 'bach10sec.wav'  
# wavefile = wave.open(filename, 'r')
# p = pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
# channels=wf.getnchannels(),
# rate=wf.getframerate(),
# output=True)
# nframes = wf.getnframes()
# framerate = wf.getframerate()

# framerate = wavefile.getframerate()


# DFT = numpy.fft.fft()
# print(DFT)
# def loudest_band(music,frame_rate,bandwidth)
# y = quad(abs(s[t])**s[t])

# return low,high,loudest


# def main():



# if __name__ == "__main__":
#     main()