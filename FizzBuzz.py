# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 15:37:04 2021

@author: Guilherme
"""

def fizzBuzz(num):
    if ((num/2-num//2)==0):
        return print ('fizz')
    elif (((num/5-num//5)==0)and((num/3-num//3)==0)):
        return print ('fizzbuzz')
    elif ((num/5-num//5)==0):
        return print ('buzz')
    return (num)
    
while(True):
    fizzBuzz(int(input())
