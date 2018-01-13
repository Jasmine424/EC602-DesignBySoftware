# Copyright 2017 Zulin Liu liuzulin@bu.edu
# Copyright 2017 James Fallacara jafallac@bu.edu
# Copyright 2017 Simin Zhai siminz@bu.edu
import numpy as np
import scipy.io.wavfile as wavfile
def dialer(file_name,frame_rate,phone,tone_time):
    tonesig =[]
    #some para I want: fs , f, npoint, t, tone
    t = np.linspace(0,tone_time,tone_time*frame_rate)
    toneeach = {'0':[941,1336],'1':[697,1209],'2':[697,1336],'3':[697,1477],'4':[770,1209],'5':[770,1336],'6':[770,1477],'7':[852,1209],'8':[852,1336],'9':[852,1477]}
    for tone in phone:
        f = toneeach[tone]
        tonesig.extend(10000*np.sin(2*np.pi*f[0]*t)+10000*np.sin(2*np.pi*f[1]*t))
    tonesig = np.array(tonesig)
    print(tonesig)
    print(type(frame_rate), type(file_name), type(tonesig[0]))
    wavfile.write(file_name, frame_rate, tonesig.astype(np.int16))
def main():
    dialer('papapa',8000,'6178007843',1)
if __name__ == '__main__':
    main()