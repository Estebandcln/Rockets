# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 05:11:51 2023

@author: DECLINE
"""

import numpy as np

# The engine uses LOX/LH2. It is used for an upper stage.
# What is the nozzle expansion ratio in order to have an average
# pressure at the nozzle exit equal to 4 kPa ?
# What is the associated theoretical specific impulse?
# What are the corresponding LOX and LH2 mass flow rates?

F = 250e3 # Thrust (N)
g0 = 9.81 # m/s²
Pc = 5e6 # Pa
Pe = 4e3 # Pa
MR = 6.5 # Mixture ratio
Cstar = 2264 # m/s
eta_Cstar = 0.98 # Efficiency
eta_ISP = 0.96 # Efficiency
Cd = 1/(eta_Cstar*Cstar)

# Using a LOX/LH2 performance table

sigma = 75+(100-75)*(0.0516-0.04)/(0.0516-0.0355) # Nozzle expansion ratio
ISP = 461.3+(466.2-461.3)*(0.0516-0.04)/(0.0516-0.0355)

ISP_th = ISP/eta_ISP # Theoretical ISP
q_cc = F/(g0*ISP) # Combustion chamber mass flow rate (kg/s)
At = q_cc/(Pc*Cd) # Throat area (m²)
Ae = sigma*At # Exit area (m²)
Re = np.sqrt(Ae/np.pi) # Nozzle exit radius (m)
q_LH2 = q_cc/(MR+1)
q_LOX = q_cc-q_LH2

print('Nozzle expansion ratio: '+str(chr(963))+' =',round(sigma,3))
print('Theoretical specific impulse: ISP_th =',round(ISP_th,3),'s')
print('Actual specific impulse: ISP =',round(ISP,3),'s')
print('LOX mass flow rate: q_LOX =',round(q_LOX,3),'kg/s')
print('LH2 mass flow rate: q_LH2 =',round(q_LH2,3),'kg/s')
