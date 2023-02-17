# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:02:57 2022

@author: DECLINE
"""

import math as m

h=800
mu=398600.5
re=6378

vr=m.sqrt(mu/re+h)


precision=1e-3
pas=0.1
k=[0.15,0.25]
isp=[260,340]
b2=3
omega=[]
a=[]
b=[]
g=9.81

def f(b1):
    for i in range(len(k)):
        omega.append(k[i]/(1+k[i+1]))
    v=g*isp[0]*m.ln(b1)+g*isp[1]*m.ln(b2)
    b1=(1/omega[0])*(1-(isp[1]/isp[0])*(1-omega[1]*b2))
    print(v)
    print(b1)
    b.append(b1)
    if v<vr:
        f(b1+pas)
    if v>vr:
        f(b1-pas)
        
    StopAsyncIteration
    
    for i in range(len(k)):
        a.append((1+k[i])/b[i]-k[i])

