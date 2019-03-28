# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from time import sleep
import string
import collections
import matplotlib.pyplot as plt
f = open(r'C:\Users\user\Desktop\Alice.txt','r', encoding='utf8')
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
plt.loglog(time)
