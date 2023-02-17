# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 14:53:22 2022

@author: DECLINE
"""

import numpy as np
from math import *

mu=398600

a=1
e=1
i=1
omega=1
startv=1
stopv=1
stepv=1
t0=1
w0=1
lw=1
alpha_dot=360/86164
la=[]
ti=[]
l0=[]
ls=[]
NEIN_NEIN_NEIN_NEIN=[]
scheisse=[]
man=[]
ean=[]
tan=np.arange(int(startv),int(stopv),int(stepv))

tp=t0-sqrt(a**3/mu)*(asin(sqrt(1-e**2)*sin(-w0)/(1+e*cos(-w0)))-e*(sqrt(1-e**2)*sin(-w0))/(1+e*cos(-w0)))

vc=acos(-e)
if -vc<=-w0 and vc>=-w0:
    corr=asin(sqrt(1-e**2)*sin(-w0)/(1+e*cos(-w0)))
if vc<=-w0 and 2*pi-vc>=-w0:
    corr=pi-asin(sqrt(1-e**2)*sin(-w0)/(1+e*cos(-w0)))
if 2*pi-vc<=-w0:
    corr=2*pi+asin(sqrt(1-e**2)*sin(-w0)/(1+e*cos(-w0)))
if -2*pi+vc<=-w0 and -vc>=-w0:
    corr=-pi-asin(sqrt(1-e**2)*sin(-w0)/(1+e*cos(-w0)))
if -w0<=-2*pi+vc:
    corr=-2*pi+asin(sqrt(1-e**2)*sin(-w0)/(1+e*cos(-w0)))


for i in tan:
    t=tp+sqrt(a**3/mu)*(corr-e*(sqrt(1-e**2)*sin(i))/(1+e*cos(i)))
    ti.append(t)




for k in tan:
    la.append((180/pi)*asin(sin(i)*sin(w*k)))

for l in la:
        if -w-90<=k and k<=-w+90:
            l0.append(asin(tan(l)/(tan(l)/tan(i))))
        if k<=-w-90:
            l0.append(-180-asin(tan(l)/(tan(l)/tan(i))))
        if -w+90<=k and k<=-w+90:
            l0.append(180-asin(tan(l)/(tan(l)/tan(i))))
        

for i in l0:
    for j in tp:
        ls.append(lw+i-alpha_dot*(j-t0))


print('la :',la)
print('ls :',ls)
print('l0 :',l0)
print('ti :',ti)






