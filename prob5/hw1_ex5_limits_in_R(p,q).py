# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:01:29 2019

@author: Laura Simonsen Leal
"""

#%%
  
e1 = 0 
n = 1
e = (1 + 1/n)**n
i = 0

tb = [e]

while abs(e - e1) > 1e-12:
    e1 = e
    i += 1
    n = 10**i
    e = (1 + 1/n)**n
    tb.append(e)
    print('i: ' + str(i))

print('Value of n_stop: ' + str(n))
print('Value to which we converged: ' + str(e))
print('Table of intermediate values: ' + str(tb))

#Value of n_stop: 100000000000000
#Value to which we converged: 2.716110034087023
#Table of intermediate values: [2.0, 2.5937424601000023, 
#2.7048138294215285, 2.7169239322355936, 2.7181459268249255, 
#2.7182682371922975, 2.7182804690957534, 2.7182816941320818, 
#2.7182817983473577, 2.7182820520115603, 2.7182820532347876, 
#2.71828205335711, 2.7185234960372378, 2.716110034086901, 2.716110034087023]

# The code converged to this value because for larger values of 'n'
# 1/n is rounded down to zero, hence 'e' will evaluate to (1+0)**n = 1.0
     
    

    