# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:24:56 2019

@author: 王一晨
"""
import numpy as np
n    = 1000   #students number 
m    = 10     #money
dm   = 2      #paid
k    = 1000   #game times
stop = False  #whether drop when money is 0 

students = np.zeros(n)+m
def select():
    p1ayer = np.random.randint(n,size = 2)
    while p1ayer[0]== p1ayer[1]:
        p1ayer[1] = np.random.randint(n)
    return p1ayer

for i in range(0,k):
    player = select()
    if stop :
        while students[player[0]]== 0 or students[player[1]]==0:
            player = select()
    while True:
        result = np.random.randint(3)
        if   result == 0:
            students[player[0]]+=dm
            students[player[1]]-=dm
            break
        elif result == 1:
            students[player[0]]-=dm
            students[player[1]]+=dm
            break
import matplotlib.pyplot as plt
plt.hist(students)
plt.show()

