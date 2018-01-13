#!/usr/bin/env python
#Copyright 2017 Zulin liuzulin@bu.edu
#Copyright 2017 Simin siminz@bu.edu
#Copyright 2017 James Fallacara jafallac@bu.edu
import math
import sys
import numpy
input_ball = sys.stdin.read()
a = input_ball.splitlines() 
b=[[i for i in ii.split(',')] for ii in a]
temp=[[i for i in ii.split(',')] for ii in a]
t = sys.argv
#print (t)
del t[0]
if(len(t)==0):
    sys.exit(2)
for i in range(0,len(t)):
    try:
        float(t[i])
    except:
        sys.exit(2)
for i in range(0,len(t)):
    if float(t[i]) <= 0:
        sys.exit(2)
        continue
for i in range(0,len(a)):
    alen = len(a[i].split())
    if alen != 5:
        sys.exit(1)
for i in range(0,len(a)):
    for j in range(1,5):
        try:
            float(a[i].split()[j])
        except:
            sys.exit(1)
for i in range(0,len(a)):
        list1 = a[i].split()
        b[i]=list1
for i in range(0,len(a)):
        list1 = a[i].split()
        temp[i]=list1
for i in range(len(a)):
    for j in range(1,5):
        b[i][j] = float(b[i][j])
for i in range(len(a)):
    for j in range(1,5):
        temp[i][j] = float(temp[i][j])
##########################################################################################
timeinput = []
t_total=0
tlist = []
tlist1 = []
answerlist = []
subanswerlist = []
for i in range(0,len(t)):
    m = float(t[i])
    timeinput.extend([m])
timeinput.sort()
#print(timeinput)
#t_total = timeinput[0]
for q in range(0,len(t)):
    for i in range(len(a)):
        for j in range(1,5):
            b[i][j] = 0
    for i in range(len(a)):
        for j in range(1,5):
            b[i][j] = temp[i][j]
    #print(temp)
    #b = temp
    #print("###############",t_total,tlist,tlist1,answerlist,subanswerlist)
    while t_total < timeinput[q]:
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                #print(b[i])
                #print(b[j])
                #if b[i] == b[j]:
                    #break
                m = (b[i][3]-b[j][3])**2+(b[i][4]-b[j][4])**2
                #print(m)
                n = 2*((b[i][1]-b[j][1])*(b[i][3]-b[j][3])+(b[i][2]-b[j][2])*(b[i][4]-b[j][4]))
                #print(n)
                c = (b[i][1]-b[j][1])**2+(b[i][2]-b[j][2])**2-100
                #print(c)
                d = (n**2)-(4*m*c)
                #print(d)
                if m == 0:
                    break
                if d >= 0:
                    t1=(-n-math.sqrt(d))/(2*m)
                    #print(t1)
                    t2=(-n+math.sqrt(d))/(2*m)
                    subanswerlist = [t1,i,j]
                    answerlist.append(subanswerlist)
                    tlist.extend([t1,t2])
        #print("liuzulin",answerlist)
        #print(tlist)
        #print(answerlist)
        for item in tlist:
            if item > 4e-16:
                tlist1.append(item)
        #print(tlist1)
        if tlist1 != []:
            #print("collision")
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
                        #print(updatei,updatej)
                        mag = math.sqrt((b[updatei][1] - b[updatej][1])**2 + (b[updatei][2] - b[updatej][2])**2)
                        temp1 = b[updatei][3]-((b[updatei][3]-b[updatej][3])*(b[updatei][1]-b[updatej][1])/mag + (b[updatei][4]-b[updatej][4]) * (b[updatei][2]-b[updatej][2])/mag)*(b[updatei][1]-b[updatej][1])/mag
                        temp2 = b[updatei][4]-((b[updatei][3]-b[updatej][3])*(b[updatei][1]-b[updatej][1])/mag + (b[updatei][4]-b[updatej][4]) * (b[updatei][2]-b[updatej][2])/mag)*(b[updatei][2]-b[updatej][2])/mag
                        temp3 = b[updatej][3]-((b[updatej][3]-b[updatei][3])*(b[updatej][1]-b[updatei][1])/mag + (b[updatej][4]-b[updatei][4]) * (b[updatej][2]-b[updatei][2])/mag)*(b[updatej][1]-b[updatei][1])/mag
                        temp4 = b[updatej][4]-((b[updatej][3]-b[updatei][3])*(b[updatej][1]-b[updatei][1])/mag + (b[updatej][4]-b[updatei][4]) * (b[updatej][2]-b[updatei][2])/mag)*(b[updatej][2]-b[updatei][2])/mag
                        b[updatei][3]= temp1
                        b[updatei][4]= temp2
                        b[updatej][3]= temp3
                        b[updatej][4]= temp4
                        # print(temp1)
                        # print(temp2)
                        # print(temp3)
                        # print(temp4)
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
    t_total = 0
    tlist =[]
    tlist1 =[]
    subanswerlist = []
    answerlist =[]