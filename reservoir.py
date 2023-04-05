# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 23:40:15 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt


e = 5e-3 # Thickness (m) (what if we always have e = 0.1Re?)
rho = 2710 #kg/m^3
n = 21 # Maximum number of reservoirs

######################### Given the mass #########################

mtot = 1 #kg
nb=np.arange(int(1), int(n)) # Number of reservoirs for the same material mass
rlist=[] # Reservoirs inner radius (m)
vlist=[] # Reservoirs inner volume (m^3)
mlist = [] # Total mass of the reservoirs (kg)

for i in range(1, len(nb)+1):
    m = mtot/i
    V = m/rho # Thickness volume (m^3)
    x = np.roots([1, e, (e**2/3)-V/(4*e*np.pi)]) # Inner radius of a shell(Ri,e,Re)
    mlist.append(mtot)
    for j in x:
        if j > 0:
            x = j
    rlist.append(x)
    vlist.append(1e6*(4/3)*np.pi*rlist[int(i-1)]**3) # cm^3

fig, ax1=plt.subplots()

plt.xticks(range(1, n))
ax1.plot(nb,vlist)
ax1.set_xlabel('Number of reservoirs')
ax1.set_ylabel('Volume of the reservoirs ($cm^3$)')
plt.grid()
plt.title(label='Total volume of identical reservoirs with the same mass')
ax2=ax1.twinx()
ax2.plot(nb, mlist, color='tab:red', label='Total mass')
ax2.set_ylabel('Mass (kg)')
plt.legend()

######################## Given the volume ########################

Vtot = 1 #m^3
vlist = [] # Reservoirs inner volume (m^3)
mlist = [] # Total mass of the reservoirs (kg)
rlist=[] # Reservoirs inner radius (m)
nb=np.arange(1, n) # Number of reservoirs for the same total inner volume

for i in range(1, len(nb)+1):
    Vi = Vtot/i # Inner volume of 1 reservoir (m^3)
    Ri = (3*Vi/(4*np.pi))**(1/3)
    Re = Ri + e
    V = (4/3)*np.pi*(Re**3-Ri**3) #m^3
    ms = V*rho # Mass of 1 reservoir (kg)
    vlist.append(Vtot)
    rlist.append(Ri)
    mlist.append(ms)


# Just a little function to get a nice y-scaling.
def scale(x,y):
    ml = [x, y]
    al = []
    for i in ml:
        a = 0
        b = 0
        if i>10:
            while i>10:
                b+=1
                i=i/10
        if b==0:
            if i>5:
                a = int(5)
            else:
                a = int(0)
        else:
            if i>5:
                a = int(i*10**b+5)
            else:
                a = int(10**b)
        al.append(a)
        
    return al[0], al[1]

fig, ax1 = plt.subplots()
x, y = scale(mlist[n-2], mlist[0])
plt.xticks(range(1, n))
plt.yticks(range(x, y, 5))

ax1.plot(nb, mlist)
ax1.set_xlabel('Number of reservoirs')
ax1.set_ylabel('Mass of the reservoirs ($kg$)')
plt.grid()
plt.title(label='Mass of identical reservoirs for the same total volume')
ax2=ax1.twinx()
ax2.plot(nb, vlist, color='tab:red', label='Total volume')
ax2.set_ylabel('Volume ($m^3$)')
plt.legend()