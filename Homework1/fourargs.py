# Copyright year Simin Zhai siminz@bu.edu

import sys 

#sys.stdout = open('stdout', 'w')
#sys.stderr = open('stderr', 'w')

ot = 0

if len(sys.argv) > 5: 
	ot = 5
else:
	ot = len(sys.argv)

for i in range(1,ot):
	sys.stdout.write(sys.argv[i]+ '\n')


for i in range(5,len(sys.argv)):
	sys.stderr.write(sys.argv[i]+ '\n')
