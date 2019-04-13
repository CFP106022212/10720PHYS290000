# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:35:07 2019

@author: 王一晨
"""
import string
import collections
import numpy as np
f = open('Alice.txt','r', encoding='utf8')
a = []
b= []
for line in f.readlines():
    res = line.replace('\n', '')
    for c in string.punctuation:
        res = res.replace(c,'')
    a.append(res)
for item in a:
    list1 = item.split() 
    b = b+list1
result = collections.Counter(b)
del a,b
time = []
for item in result.items():
    time.append(item[1])
del item,list1,line,res,c
time.sort()
time.reverse()
a = list(range(1,3849))
from scipy import optimize
import matplotlib.pyplot as plt
def power_func(x,amp,alpha):
    return amp*x**alpha
ra,rb = optimize.curve_fit(power_func,a,time)
plt.plot(a,power_func(a,ra[0],ra[1]),'*r')
plt.plot(a,time)
plt.show()
print('amp: %.3f  alpha: %.3f  covariance: %.3f'% (ra[0],ra[1],np.sqrt(rb[0,0])))


