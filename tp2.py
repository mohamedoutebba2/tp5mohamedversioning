# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 19:51:31 2025

@author: moham
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x) - 1

x = np.arange(1, 6.01, 0.05)  #avec unpas égal à 0,05
y = f(x)

plt.plot(x, y, label="f(x) = ln(x) - 1")
plt.xlabel("x")  #nom de l axe horizontal x
plt.ylabel("f(x)")  #nom de l axe vertical y
plt.title("Représentation de f(x)") #titre du graphique
plt.grid()#fait la grille
plt.axhline(0, color="red", linestyle="--")
plt.show()# pour montrer le graph




x=np.arange(1,6,0.05)
plt.plot(x,np.log(x)-1,"b")
plt.plot(x,0*x,"m")
plt.grid()#fait la grille

import matplotlib.pyplot as plt
import numpy

f=lambda x:np.log(x)-1
f_prime=lambda x:1/x

a,b=1,6

while abs(b-a)>=1E-6:
    c=(a+b)/2
    if f(a)*f(c)<=0:
        b=c
    else:
        a=c
    print(a,c,b)
