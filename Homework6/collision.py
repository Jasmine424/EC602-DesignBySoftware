
import math
import sys
import numpy
input1_ball = sys.stdin.read()
a = input_ball.splitlines()
b=[[i for i in ii.split(',')] for ii in a]
t = sys.argv
del t[0]
    if(len(t)==0):
        return 2
    for i in range (0, len(t)):
        try:
            t[i] = float(sys.argv[i])
        except:
            return 2
    for i in range (0, len(a)):
        try:
            a[i] = a[i].split()
        if(len(a)!= 5):
           return 1
        for j in range(1,5):
            try: 
                a[i][j] = float(a[i][j])
                print(a[i][j])
            except:
                return 1
##########################################################################################
timeinput = []
t_total=0
tlist = []
tlist1 = []
answerlist = []
t.sort()
for i in range(0,len(t)):
    m = float(t[i])
    timeinput.extend([m])
for q in range(0,len(t)):
    while t_total < timeinput[q]:
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if b[i] == b[j]:
                    break
                m = (b[i][3]-b[j][3])**2+(b[i][4]-b[j][4])**2
                n = 2*((b[i][1]-b[j][1])*(b[i][3]-b[j][3])+(b[i][2]-b[j][2])*(b[i][4]-b[j][4]))
                c = (b[i][1]-b[j][1])**2+(b[i][4]-b[j][4])**2-100
                d = (n**2)-(4*m*c)
                if m == 0:
                    break
                if d >= 0:
                    t1=(-n-math.sqrt(d))/(2*m)
                    t2=(-n+math.sqrt(d))/(2*m)
                # if t1 > 0 and t2 > 0:
                #     if t1 > t2:
                #         t = t2
                #     elif t1 < t2:
                #         t = t1
                #     else:
                #         t = t1
                # else: 
                #     break
                    subanswerlist = [t1,i,j]
                    answerlist.append(subanswerlist)
                    tlist.extend([t1,t2])
        #print(tlist)
        for item in tlist:
            if item > 0:
                tlist1.append(item)
        #print(tlist1)
        if tlist1 != []:
            min_t = min(tlist1)
            tlist =[]
            tlist1 =[]
            #print(min_t)
            t_total = t_total + min_t
            #print(t_total)
            if t_total <= timeinput[q]:
                for i in range(0,len(a)):
                    b[i][1]= b[i][1] + b[i][3]*min_t
                    b[i][2]= b[i][2] + b[i][4]*min_t
                for i in range(0,len(answerlist)):
                    if min_t == answerlist[i][0]:
                        updatei = answerlist[i][1]
                        updatej = answerlist[i][2]
                mag = math.sqrt((b[updatei][1] - b[updatej][1])**2 + (b[updatei][2] - b[updatej][2])**2)
                temp1 = b[updatei][3]-((b[updatei][3]-b[updatej][3])*(b[updatei][1]-b[updatej][1])/mag + (b[updatei][4]-b[updatej][4]) * (b[updatei][2]-b[updatej][2])/mag)*(b[updatei][1]-b[updatej][1])/mag
                temp2 = b[updatei][4]-((b[updatei][3]-b[updatej][3])*(b[updatei][1]-b[updatej][1])/mag + (b[updatei][4]-b[updatej][4]) * (b[updatei][2]-b[updatej][2])/mag)*(b[updatei][2]-b[updatej][2])/mag
                temp3 = b[updatej][3]-((b[updatej][3]-b[updatei][3])*(b[updatej][1]-b[updatei][1])/mag + (b[updatej][4]-b[updatei][4]) * (b[updatej][2]-b[updatei][2])/mag)*(b[updatej][1]-b[updatei][1])/mag
                temp4 = b[updatej][4]-((b[updatej][3]-b[updatei][3])*(b[updatej][1]-b[updatei][1])/mag + (b[updatej][4]-b[updatei][4]) * (b[updatej][2]-b[updatei][2])/mag)*(b[updatej][2]-b[updatei][2])/mag
                b[updatei][3]= temp1
                b[updatei][4]= temp2
                b[updatej][3]= temp3
                b[updatej][4]= temp4
        else:
            for i in range(0,len(a)):
                # print(i)
                # print(b[i][3])
                # print(timeinput[q]-t_total)
                b[i][1]= b[i][1] + b[i][3]*(timeinput[q]-t_total)
                b[i][2]= b[i][2] + b[i][4]*(timeinput[q]-t_total)
                # print(b[i])
            t_total = timeinput[q]
    if t_total == timeinput[q]:
        str(timeinput[q])
        print(timeinput[q])
        for i in range(0,len(a)):
            print(b[i][0]+' '+str(b[i][1])+' '+str(b[i][2])+' '+str(b[i][3])+' '+str(b[i][4]))
    if t_total > timeinput[q]:
        str(timeinput[q])
        print(timeinput[q])
        t_total = t_total - min_t
        for i in range(0,len(a)):
            b[i][1]= b[i][1] + b[i][3]*(timeinput[q]-t_total)
            b[i][2]= b[i][2] + b[i][4]*(timeinput[q]-t_total)
            print(b[i][0]+' '+str(b[i][1])+' '+str(b[i][2])+' '+str(b[i][3])+' '+str(b[i][4]))
