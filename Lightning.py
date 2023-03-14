# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:31:09 2021

@author: DECLINE
"""

import os
import csv
import cantera as ct
import matplotlib.pyplot as plt
import numpy as np

# Propellant reservoir hit by lightning

time = 0.0
n_steps = 10000

# Reservoir full or air as environment
env = ct.Reservoir(ct.Solution('air.yaml'))

# Use GRI-Mech 3.0 for the methane/air mixture, and set its initial state
gas = ct.Solution('gri30.yaml')

gas.TP = 303.15, 1 * ct.one_atm
#gas.TP = 333.15,  40*ct.one_atm

#gas.set_equivalence_ratio(1, 'CH3OH:0.2', 'H2O2:0.6,N2:0.2', basis='mass')
gas.set_equivalence_ratio(1.1, 'CH4:0.2', 'O2:0.8')

gas.mass_fraction_dict()

# create a reactor for the methane/air side
r = ct.IdealGasReactor(gas)

# Heat loss always occur through walls, so we create a wall separating 
# r2 from the environment, give it a non-zero area, and specify the 
# overall heat transfer coefficient through the wall.

w = ct.Wall(r, env, A=80*np.pi,U=5)
sim = ct.ReactorNet([r])

output_data = []
states = ct.SolutionArray(gas, extra=['t', 'V'])

for n in range(n_steps):
    time += 4.e-4
    print(n, time, r.T)
    
    #duration of a lightning
    if time>0 and time<0.2:
        w = ct.Wall(r, env, A=1,U=-5)
    sim.advance(time)
    states.append(r.thermo.state, t=time, V=r.volume)
    output_data.append([time,r.thermo.T,r.thermo.P, r.volume])

with open('piston.csv', 'w', newline="") as outfile:
    csvfile = csv.writer(outfile)
    csvfile.writerow(['time (s)', 'T1 (K)', 'P1 (Bar)', 'V1 (m3)', 'T2 (K)','P2 (Bar)', 'V2 (m3)'])
    csvfile.writerows(output_data)

print('Output written to file piston.csv')
print('Directory: '+os.getcwd())



plt.clf()

plt.figure(1)
plt.title('Temperature of the CH3OH/H2O2 propellant mixture after a lightning strike')
plt.subplot(2, 2, 1)
h = plt.plot(states.t, states.T, 'b-')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (K)')

plt.subplot(2, 2, 2)
plt.plot(states.t, states.P/1e5, 'b-')
plt.xlabel('Time (s)')
plt.ylabel('Pressure (Bar)')

plt.subplot(2, 2, 3)
plt.plot(states.t, states.V, 'b-')
plt.xlabel('Time (s)')
plt.ylabel('Volume (m$^3$)')

plt.figlegend(h, ['Reactor 1', 'Reactor 2'], loc='lower right')
plt.tight_layout()
plt.show()
plt.savefig('CH3OH-H2O2.svg')

