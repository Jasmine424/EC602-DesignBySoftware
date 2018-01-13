# Copyright 2017 James Fallacara jafallac@bu.edu
# Copyright 2017 Zulin Liu liuzulin@bu.edu
# Copyright 2017 Simin Zhai siminz@bu.edu
from numpy import zeros, exp, array, pi
def DFT(x):
    if type(x) is tuple:
        for i in range(len(x)):
            if type(x[i]) is str:
                raise ValueError()
    if type(x) is str or type(x) is int or type(x) is dict:
        raise ValueError()
    if hasattr(x,'__len__'):
        arr = zeros(len(x), dtype = complex)
        N = len(x)
        for k in range(0,N):
            for n in range(0,N):
                y = x[n]*exp(-2*pi*1j*n*k/N)
                print(y)
                arr[k] += y
        return arr
    else:
        raise ValueError()
        return 1
def main():
    list1 = [1,1]
    in_1 = array(list1)
    out_1 = DFT(in_1)
    return 0
if __name__ == '__main__':
    main()