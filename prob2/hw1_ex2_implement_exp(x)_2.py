# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:12:59 2019

@author: Laura Simonsen Leal
"""
#%%

import numpy as np

#%% a/b: approximate exp(5.5) while working with only 5 decimal digits in the mantissa (left to right)

def exponential_left_right(x):
    num = 1
    den = 1
    expon = 1
    terms = [1.0]
    #print('The partial sums for the Taylor expansion of exp({}) are: '.format(x))
    for i in range(1,31):
        num = float('%.5g'%(num*x))
        den = float('%.5g'%(den*i)) 
        ratio = float('%.5g'%(num/den))
        terms.append(ratio)
        #print('{}-th term: '.format(i) + str(ratio))
        if ratio != 0:
            expon = float('%.5g'%(expon + ratio))
        else:
            #print('Finished convergence at step {}'.format(i-1))
            break
    #print('Left to right: exp({}) = '.format(x) + str(expon))
    return expon, terms



#%% c: approximate exp(5.5) while working with only 5 decimal digits in the mantissa (right to left)

def exponential_right_left(x):
    _,terms = exponential_left_right(x)
    terms_rev = terms[::-1]
    expon = 0
    for i in range(0,30):
        expon = float('%.5g'%(expon + terms_rev[i]))
    expon = float('%.5g'%(expon + 1.0))
    #print('Right to left: exp({}) = '.format(x) + str(expon))
    return expon
        

    

#%% 

x = 5.5
true = np.exp(x) # exp(5.5) = 244.69193226422038
  
# a/b  
approx,_ = exponential_left_right(x) 
print(approx) # exp(5.5) = 244.71
# Converges using all the iterations. After this, we stop updating the value.
# This result represents a 5 sig-fig truncation of the value computed directly 
# in double-precision
# The magnitude of the relative error is:  7.383870654188337e-05.
print('rel_error = ' + str(np.abs((true - approx)/true)))

# c 
approx_2 = exponential_right_left(x) # exp(5.5) = 244.71
print(approx_2)
# Now we only converge at the last step.
# It is now 1 more than the value that it should be.
# The magnitude of the relative error is the same r: 7.383870654188337e-05
print('rel_error = ' + str(np.abs((true - approx_2)/true)))


#%% d - iii

def exponential_left_right_pos_neg(x):
    _,terms = exponential_left_right(x)
    neg_terms = terms[1::2]
    pos_terms = terms[::2]
    
    neg_expon = 0
    pos_expon = 0
    
    for i in range(len(neg_terms)):
        neg_expon = float('%.5g'%(neg_expon + neg_terms[i]))

    for i in range(len(pos_terms)):
        pos_expon = float('%.5g'%(pos_expon + pos_terms[i]))
                
    expon = float('%.5g'%(neg_expon + pos_expon))
        
    #print('Right to left, pos-neg divide: exp({}) = '.format(x) + str(expon))
    return expon, neg_terms, pos_terms
    
  
#%% d - iv

def exponential_right_left_pos_neg(x):
    _,neg_terms,pos_terms = exponential_left_right_pos_neg(x)   
    
    neg_terms_rev = neg_terms[::-1]
    pos_terms_rev = pos_terms[::-1]
    
    neg_expon = 0
    pos_expon = 0
    
    for i in range(len(neg_terms_rev)):
        neg_expon = float('%.5g'%(neg_expon + neg_terms_rev[i]))

    for i in range(len(pos_terms_rev)):
        pos_expon = float('%.5g'%(pos_expon + pos_terms_rev[i]))
                
    expon = float('%.5g'%(neg_expon + pos_expon))
        
    #print('Right to left, pos-neg divide: exp({}) = '.format(x) + str(expon))
    return expon


#%%
x = -5.5
true = np.exp(x)
print(true) # = 0.004086771438464067


# i
approx,_ = exponential_left_right(x) # exp(-5.5) = 0.0038363
print(approx)
print('rel_error = ' + str(np.abs((true - approx)/true))) # rel_error = 0.06128834025477125
# %timeit exponential_left_right(x)
# 121 µs ± 2.74 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# Compared to when the argument was positive, the error is now much larger

# ii
approx_2 = exponential_right_left(x) # exp(-5.5) = 0.004
print(approx_2)
print('rel_error = ' + str(np.abs((true - approx_2)/true))) # rel_error = 0.021232270943118334
# %timeit exponential_right_left(x)
# 150 µs ± 3.41 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# Compared to when the argument was positive, the error is now much larger

# iii
approx_3,_,_ = exponential_left_right_pos_neg(x) # exp(-5.5) = 0.0
print(approx_3)
print('rel_error = ' + str(np.abs((true - approx_3)/true))) # rel_error = 1.0
# %timeit exponential_left_right_pos_neg(x)
# 145 µs ± 2.36 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
 
# iv
approx_4 = exponential_right_left_pos_neg(x)
print(approx_4)
print('rel_error = ' + str(np.abs((true - approx_4)/true))) # rel_error = 1.4469193226422041
# %timeit exponential_right_left_pos_neg(x)
# 181 µs ± 4.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
 
 
# Note: all methods seem to be equally quick, with exponential_left_right(x) being slightly quicker.
# The lowest error can be seen on the exponential_right_left(x) method.
# Compared to when the argument of the exponential was positive, the relative
# error is now much larger. However, still smaller than other methods.

#%% e: alternative method to calculate exp(-5.5):
# I propose to calculate e^(5.5) and then take the multiplicative inverse, since
# e^(-5.5) = 1/e^(5.5) 

def alt_exp(x):
    alt_exp = 1/np.exp(np.abs(x))
    return alt_exp

alt_exp(5.5)


#%%



















