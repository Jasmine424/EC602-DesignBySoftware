#Copyright 2017 Simin Zhai siminz@bu.edu
class Polynomial():
    def __init__(self, seq=None):
        self.poly = dict()
        if seq != None :
            inc = 0
            for c in reversed(seq):
                self[inc] = c
                inc = inc + 1
            
    def __getitem__(self,x):
        if x in self.poly:
            return self.poly[x]
        else:
            return 0
    
    def __setitem__(self,j,k):
        if k==0:
            try:
                del self.poly[j]
            except KeyError:
                pass
        else:
            self.poly[j]=k

    def __str__(self):
        return str(self.poly)
    
    def __add__(self,other):
        p=Polynomial()
        for m in self.poly:
            p[m]=self[m]
        for n in other.poly:
            p[n]=p[n]+other[n]
        return p;
    
    def __sub__(self,other):
        p=Polynomial()
        for m in self.poly:
            p[m]=self[m]
        for n in other.poly:
            p[n]=p[n]-other[n]
        return p;
    
    def __mul__(self,other):
        p=Polynomial()
        for m in self.poly:
            for n in other.poly:
               p[n+m]=p[n+m]+self[m]*other[n]
        return p;
    
    
    def __eq__(self,other):
        return self.poly == other.poly

    def eval(self,other):
        result=0
        for i in self.poly:
            result = result+self[i]*(other**i)
        return result

    def deriv(self):
        p=Polynomial()
        for i in self.poly:
            p[i-1] = self[i]*i
        return p
    __repr__ = __str__

def main():
    pass


if __name__=="__main__":
    main()