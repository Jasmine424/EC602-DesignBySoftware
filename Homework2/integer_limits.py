# Copyright 2017 Simin Zhai siminz@bu.edu

import math
def bigum1(n):
	a=2**(n*8)-1
	return a

def bigum2(n):
	a=-2**(n*8-1)
	return a

def bigum3(n):
	a=2**(n*8-1)-1
	return a

Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for n in range(1,9):
	a=bigum1(n);
	b=bigum2(n);
	c=bigum3(n);
	print(Table.format(n,a,b,c))
