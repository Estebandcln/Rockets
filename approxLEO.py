# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 22:40:07 2024

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt

# deltaR = k*deltaV

r_T = 6378 # km
mu = 398600 # km

h = np.linspace(200, 2000, 100)
r_list = []

for i in h:
    r_list.append(i+r_T)
    
v_list = []
k_list = []

for i in range(len(h)):
    v_list.append(np.sqrt(mu/(r_T+h[i])))
   
for i in range(len(h)):
    k_list.append(4/1000*r_list[i]/v_list[i])
    

plt.plot(h, k_list)