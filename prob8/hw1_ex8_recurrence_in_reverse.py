# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 09:29:22 2019

@author: Laura Simonsen Leal
"""

#%%
import numpy as np
from scipy.integrate import quad
from math import factorial

#%% c: find N needed to achieve the error in y_20

k = 20
eps = np.finfo(float).eps
goal = factorial(k)/eps

N = 21
while factorial(N) <= goal:
    N += 1

print(N) # minimum value of N needed to achieve the target relative error in y_k
    
# N = 32

#%% d: Find value of y_20 using N=32

y = 0

for i in range(N,20,-1):  
    y = (np.exp(1) - y) / i
    
print(y) # 0.12380383076256993

#%% Values for comparison:

# Wolfram Alpha value: 0.123803830762570
    
# scipy
func = lambda x:np.exp(x)*x**20
quad(func,0,1) # = 0.12380383076256998

# values seem pretty close!