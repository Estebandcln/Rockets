# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 03:19:30 2023

@author: DECLINE
"""

# Liquid propulsion engine
mass_flow = 10 # kg/s
thrust = 200000 # N
energy = 20e6 # W

# Solid propulsion motor
mass_prop = 1000 # kg
thrust_prop = 100000 # N
t_impulse = 60 # s

# ISP liquid
isp_liquid = thrust / (mass_flow * 9.81) # en secondes

# ISP solid
mass_tot = mass_prop + (mass_flow * t_impulse)
isp_solid = (2 * thrust_prop * t_impulse) / (mass_tot * 9.81) # en secondes

print("ISP liquid engine :", round(isp_liquid,2),'s')
print("ISP solid motor :", round(isp_solid,2),'s')