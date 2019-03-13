# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 06:38:51 2019

@author: Laura Simonsen Leal
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,num=1001,dtype='float64')
y = np.linspace(0,1,num=1001,dtype='float64')

N = 50
#z = np.log(x)/np.log(np.exp(2**N))

# Square-roots
for i in range(N+1):
    x = np.sqrt(x)

# Squares
for j in range(N+1):
    x = x**2
    
#for i in range(len(y)):
#    if y[i] - x[i] < 0.001:
#        print(y[i])

# Plot
f, ax = plt.subplots(figsize=(6, 6))
ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
ax.plot(y,x)
ax.set_title('Machine epsilon rounding problem on square-root/square')

# the problem is overflow error
# in the numbers on the diagonal, there is no error, the approximation is exact. why?

