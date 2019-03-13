# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:25:33 2019

@author: Laura Simonsen Leal
"""

#%% Packages

from sympy import Symbol,Poly
from sympy.polys.polytools import poly_from_expr
from scipy.optimize import newton
import numpy as np

#%% a: Getting the coefficients exactly

x = Symbol('x')
W = 1
for i in range(1, 21):
    W = W * (x-i)

print(W.expand())

#%% b: store coefficients as floats

P,d = poly_from_expr(W.expand())
print(P)

coeffs = P.all_coeffs()
coeffs = np.asarray(coeffs).astype('float64')

r00t = np.max(np.roots(coeffs)) # max root = 19.999853724604495
r00t2 = newton(P,21) # we reach a RuntimeError after 50 iterations. Value is 20.0000123414111

#%% c: change a_20 from 1 to 1+delta for different values of delta

for i in range(-8,0,2):
    coeffs[0] = 1 + 10**i
    r00t = np.max(np.roots(coeffs)) # max root = 19.999853724604495
    print('Max root obtained using np.roots: ' + str(r00t))
    try:
        x = Symbol('x')
        P1 = Poly.from_list(coeffs.tolist(), gens=x)
        r00t2 = newton(P1,21) 
        print('Root obtained using Newton-Raphson method: ' + str(r00t2))
    except Exception as e:
        print(str(e))


# Largest root grows as we increase delta for the first method,
# but the root we find decreases for the Newton-Raphson method.
    
#%% d: change a_19 from -210 to -210-2^(-23). What happens to roots 16 and 17?
    
coeffs[0] = 1
coeffs[1] = -210.0 - 2**(-23)
    
r00ts = np.roots(coeffs)

print(r00ts)

# Roots 16 and 17 are now complex conjugates! 

# and so are roots 19 and 18! and 14 and 15! and 13 and 12! and 11 and 10!
# the others probably are too, but their imaginary part is too close to 0.

#%% e-ii: evaluate condition numbers for roots r=14,16,17,20

# finding the derivative of the polynomial
coeffs = P.all_coeffs()
p_ = np.poly1d(coeffs)
p2 = np.polyder(p_)

# roots to be evaluated
roots_w = [1,14,16,17,20]

cond_nums = []

for r in roots_w:
    kappa = 0
    for l in range(20):
        num = np.abs(coeffs[l]*(r**(l-1))) ## is this correct?
        den = np.abs(p2(r))
        kappa += num/den
    cond_nums.append(kappa)
    
print(cond_nums)

# large condition numbers correspond to ill-conditioned problems
# large roots have, in this problem, large condition numbers,
# meaning that they are very sensitive to changes in the coefficients


#%%


































