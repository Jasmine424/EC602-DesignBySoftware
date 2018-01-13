#Copyright 2017 Simin Zhai siminz@bu.edu

import numpy as np

X = input()
Y = input()
X = X.split()
Y = Y.split()

for a in range(len(X)):
	X[a] = float (X[a])

for b in range(len(Y)):
	Y[b] = float (Y[b])


S = np.convolve(X,Y)

output = [];
for i in range(len(S)):
	output.append(S[i].item())

print(" ".join(str(i) for i in output))