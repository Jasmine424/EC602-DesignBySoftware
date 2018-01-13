# Copyright 2017 Simin Zhai siminz@bu.edu
import math
weight_earth = 5.972e27;
pandn = weight_earth*6.022e23;
elec1 = 0.5;
elec2 = 0.4;
elec3 = 1;

a = pandn*elec1;
b = pandn*elec2;
c = pandn*elec3;

ETB = a / pow(2,43);
LTB = b / pow(2,43);
UTB = c / pow(2,43);

print (ETB)
print (LTB)
print (UTB)

	
