# Copyright year Simin Zhai siminz@bu.edu

import sys 

#sys.stdout = open('stdout', 'w')
#sys.stderr = open('stderr', 'w')

class A():
	def __init__(self, ot):
		self.ot = ot

	def hello(self):
		print ('hello ' + str(self.ot))

class B():
	def __init__(self, ot):
		self.ot = ot

	def hello(self):
		print ('hello 2 ' + str(self.ot) )


ot = 0

a = A(124124124)
a.hello()

b = B(123)
b.hello()

a = A(12)
a.hello()

if len(sys.argv) > 5: 
	ot = 5
else:
	ot = len(sys.argv)

for i in range(1,ot):
	sys.stdout.write(sys.argv[i]+ '\n')


for i in range(5,len(sys.argv)):
	sys.stderr.write(sys.argv[i]+ '\n')
