#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:29:00 2017

@author: ec602
"""

class Polynomial():

#initiate class polynomial with the use of dictionary
      
    def __init__(self, coefficient):
        self.coefficient = coefficient
        self.poly = {}
        
        for i in range(len(coefficient)):
            if coefficient[i] == 0:
                pass
            else:
                self.poly[len(coefficient)-i-1] = coefficient[i]
        

    #get specific polynomial coefficient   
   
    def __getitem__(self,key):
        try:
            return self.poly[key]
        except:
            IndexError
            return 0
            
            
    #set specific polynomial coeffient   
    
    def __setitem__(self,key, value):
        try:
            if value == 0:
                   del self.poly[key]
            else:
                  self.poly[key] = value
        except:
            KeyError
            pass
                
    #get dictionary keys 
    
    def keys(self):
        return self.poly.keys()
    
    #get dictionary items
    
    def items(self):
        return self.poly.items()
      
    # get polynomial dectionary printing    
    def __str__(self):
        return str(self.poly)
    
    # get the evaluation of a polynomial 
    def eval(self,x):
        y = 0
        for i in self.poly.keys():
            y += self.poly[i]*x**i
        return y
    
    
    # return the derivative of the polynomial 
    def deriv(self):
        dx = Polynomial([])
        for i in list(self.poly.keys()):
            if i == 0:
                pass
            else:
                dx[i-1] = self.poly[i]*i
        return dx

        
    # addition
    
    def __add__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            if i in list(B.keys()):
                c[i] = B[i]+self[i]
            else:
                c[i] = self[i]
        for j in list(B.keys()):
            if j in list(self.keys()):
                c[j] = self[j] + B[j]
            else:
                c[j] = B[j]
        return c
            
    
    # Method for subtracting two Polynomials using -
    
    def __sub__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            if i in list(B.keys()):
                c[i] = B[i]-self[i]
            else:
                c[i] = self[i]
        for j in list(B.keys()):
            if j in list(self.keys()):
                c[j] = self[j] - B[j]
            else:
                c[j] = -B[j]
        return c
            
            
    #multiplication
    
    def __mul__(self,B):
        c = Polynomial([])
        for i in list(self.keys()):
            for j in list(B.keys()):
                    if c[i+j] != None:
                        c[i+j] += self[i]*B[j]
                    else:
                        c[i+j] = self[i]*B[j]
        return c
    
    #equality
    
    def __eq__(self,other):
        if self.poly == other.poly:
            return True
        else:
            return False