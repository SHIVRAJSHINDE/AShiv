# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:38:55 2019

@author: HP
"""

def fib1(n):
    a,b =0,1
    while b<n:
        print(b, end=' ')
        a,b=b, a+b
    print()    
    
def fib2(n):
    result = []
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b, a+b
    return result    