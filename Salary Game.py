# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:24:56 2019

@author: 王一晨
"""
import numpy as np
import random
n    = 1000   #students number 
m    = 10     #money
dm   = 3      #paid
k    = 1000   #game times
stop = False  #whether drop when money is 0 
a    = list(range(0,n))
students = np.zeros(n)+m
def select():
    random.shuffle(a)
    p1ayer = a[:2]
    return p1ayer
for i in range(0,k):
    player = select()
    if stop :
        while students[player[0]]<= 0 or students[player[1]]<=0:
            player = select()
    
    result = np.random.randint(3) #猜拳
    if   result == 0:
        students[player[0]]+=dm
        students[player[1]]-=dm
    elif result == 1:
        students[player[0]]-=dm
        students[player[1]]+=dm
        
import matplotlib.pyplot as plt
plt.hist(students)
plt.show()



