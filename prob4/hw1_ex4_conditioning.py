# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:45:11 2019

@author: Laura Simonsen Leal
"""

#%% Packages

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
#from scipy.optimize import fsolve

#%% c

x = np.linspace(0,1,100)

def cond_f(x):
    res = np.abs(x/(np.exp(x)-1))
    return res

def cond_A(x):
    res = np.abs((2-np.exp(x))/x)
    return res

fig, ax = plt.subplots(figsize=(6,2.5))
ax.plot(x,cond_f(x))
ax.plot(x,cond_A(x))
ax.legend(('cond_f','cond_A'))

# The root cause of the poor conditioning is the subtraction from 1.
# Since np.exp(x) is very close to 1 for small values of x, we will have 
# a huge error magnification. 

#%% d: find x for given bits


xs = []

for b in range(1,5):


    func = lambda x: 1 - np.exp(-x) - 2**(-b) 
    
    x_initial_guess = 0.4
    x_solution = least_squares(func, x_initial_guess, bounds = (0, 1))
    x_solution = float(x_solution.x)

# Alternative way:    
#     Use the numerical solver to find the roots
#    x_solution = float(fsolve(func, x_initial_guess))  
    
#    if x_solution > 1.0:
#        x_solution = 1.0
#    if x_solution < 0:
#        x_solution = 0
        
    print("The solution is x = %f" % x_solution)
    print("at which the value of the expression is %f" % func(x_solution))
      
    xs.append(x_solution)
    
print(xs)

#%% d: alternative (more straightforward) way

xs2 = []
for b in range(1,5):
    x = - np.log(1-2**(-b))
    xs2.append(x)

print(xs2)

#%% e: find bits for given x

def upper_bound_rel_err_output(x):
    up_bnd = cond_f(x) * (cond_A(x) - np.finfo(np.float64).eps)  
    return list(up_bnd )
   
up_bnd = upper_bound_rel_err_output(xs2)

#%% f: alternative algorithm (see written solutions)

