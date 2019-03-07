# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#SI unit
h = 6.62*10**-34 #Planck constant
c = 3*10**8      #speed of light
k = 1.38*10**-23 #Boltzmann Constant JK^-1

v = np.linspace(10**0, 10**15, 1000, endpoint=True)
#print(v)

T=float(input("Input temperature:"))
B=2*h*v**3/c**2/(math.e**(h*v/k/T)-1)
db = np.random.normal(1,10**-9,len(v)) 
B+=db

plt.plot(v,B,"-")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity Watts/Hz/m^2")

plt.show()                
