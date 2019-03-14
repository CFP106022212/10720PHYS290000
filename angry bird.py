# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from math import sin,cos,pi
import matplotlib.pyplot as plt
x = np.random.random(2)
x *= 50
x += 25
#circle1 = plt.Circle((x[0],x[1]),2, color='blue')
#fig, ax = plt.subplots()
#ax.add_artist(circle1)
#plt.show()    
g = 9.8
while True:
    a = input('theta：')
    if a == 'n' or a=='N':
        break
    else:
        theta = float(a)/180*pi
        
    a = input('velosity：')
    if a == 'n' or a=='N':
        break
    else:
        v = float(a)
    vx = v*cos(theta)
    vy = v*sin(theta)
    t = 2*vy/g
    mt = np.linspace(0,t,1000)
    mx = mt*vx
    my = vy*mt-0.5*g*mt**2
    circle1 = plt.Circle((x[0], x[1]),2,color='blue')
    fig, ax = plt.subplots()
    ax.add_artist(circle1)
    ax.plot(mx,my)
    ax.set_xlim((0, 75))
    ax.set_ylim((0, 75))
    plt.show()
    ax.cla()
    mdis = np.sqrt((mx-x[0])**2+(my-x[1])**2)
    if min(mdis)<2:
        print('you win')
        break
    else:
        print('try again')
        print(min(mdis))
    
