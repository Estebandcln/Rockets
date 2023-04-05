# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 00:48:11 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt

# This 20 kN engine uses UDMH/N204 propellant. 
# It has a pressure fed cycle.
# Tanks are pressurized with gaseous Helium.
# The Helium tank is spherical. 

tp = 800 # Functioning time (s)
q_tot = 6.5 # Overall mass flow rate (kg/s)

# Propellant

MR = 1.8 # Mixture ratio
rho_UDMH = 780 # Density (kg/m3)
rho_N2O4 = 1447 # Density (kg/m3)

# Propellant tanks

P = 2.4e6 # Tanks pressure (Pa)
V_u = 5 # Ullage volume (% of the volume of each tank)
T_He = 300 # Helium temperature (K)
M_He = 4e-3 # Helium molar mass (kg)
z = 1.01 # Compressibility factor of Helium at 2.4 MPa & 300 K
R = 8.314 # Perfect gas constant (J/K/mol)


# Helium mass (useful) needed to pressurize the tanks

q_UDMH = q_tot/(1+MR) # Fuel
q_N2O4 = q_tot-q_UDMH # Oxidizer

m_UDMH = q_UDMH*tp # kg
m_N2O4 = q_N2O4*tp # kg

V_UDMH = m_UDMH/rho_UDMH # Useful volume of fuel (m3)
V_N2O4 = m_N2O4/rho_N2O4 # Useful volume of oxidizer (m3)

V_UDMH_tot = (1+10/(100-V_u))*V_UDMH # Total volume of the fuel tank (m3)
V_N2O4_tot = (1+10/(100-V_u))*V_N2O4 # Total volume of the oxidizer tank (m3)

V_tot = V_UDMH_tot+V_N2O4_tot # Total volume of both tanks (m3)

rho_He = P*M_He/(z*R*T_He) # Helium density (kg/m3)

m_He_UDMH = rho_He*V_UDMH_tot # Mass of Helium within the fuel tank
m_He_N2O4 = rho_He*V_N2O4_tot # Mass of Helium within the oxidizer tank
m_He_useful = rho_He*V_tot # Useful mass of Helium (kg)

# Helium tank

res = 30 # % of the overall mass of Helium that are residuals
P_He = 350e5 # Helium storage pressure (Pa)
T_He = 300 # Helium storage temperature (K)
z = 1.16 # Compressibility factor of Helium at 35 MPa & 300 K
Cs = 2 # Safety coefficient

# Helium tank material (Titanium, Cast Iron, Aluminum, Copper, Stainless Steel, Tungsten, Nickel)

sigma_Ti = 460e6 # Ultimte tensile strength (Pa)
rho_Ti = 4510 # Density (kg/m3)
sigma_Fe = 431e6 # Ultimte tensile strength (Pa)
rho_Fe = 7130 # Density (kg/m3)
sigma_Al = 193e6 # Ultimte tensile strength (Pa)
rho_Al = 2700 # Density (kg/m3)
sigma_Cu = 380e6 # Ultimte tensile strength (Pa)
rho_Cu = 8960 # Density (kg/m3)
sigma_SS = 1100e6 # Ultimte tensile strength (Pa)
rho_SS = 7800 # Density (kg/m3)
sigma_Ni = 760e6 # Ultimte tensile strength (Pa)
rho_Ni = 8910 # Density (kg/m3)
sigma_W = 3447e6 # Ultimte tensile strength (Pa)
rho_W = 19280 # Density (kg/m3)

mat = ['Titanium', 'Iron', 'Aluminum', 'Copper', 'Stainless Steel', 'Tungsten', 'Nickel']
c = ['r', 'b', 'k', 'orange', 'g', 'grey', 'c']
sigma = [sigma_Ti, sigma_Fe, sigma_Al, sigma_Cu, sigma_SS, sigma_Ni, sigma_W]
rho = [rho_Ti, rho_Fe, rho_Al, rho_Cu, rho_SS, rho_Ni, rho_W]

# Helium sphere mass


for i in range(len(rho)-2):
    n = []
    m = []
    n.append(i)
    m_He_tot = 100*m_He_useful/(100-res)
    rho_He = P_He*M_He/(z*R*T_He) # Helium density in its tank (kg/m3)
    V_He = m_He_tot/rho_He # Volume of the Helium tank (m3)
    r = (3*V_He/(4*np.pi))**(1/3) # Internal radius of the Helium tank (m)
    e = Cs*P_He*r/(2*sigma[i]) # Thickness of the Helium tank (m)
    V_m = 4/3*np.pi*((r+e)**3-r**3) # Volume of the material (m3)
    m_tank = rho[i]*V_m # Mass of the Helium tank (kg)
    m.append(m_tank)
    plt.scatter(n,m,c=str(c[i]),label=str(mat[i]))
plt.title('Mass of the tank for the same volume of Helium')
plt.xlabel('Material')
plt.ylabel('Mass of the tank (kg)')
plt.xticks(range(len(mat)))
plt.legend()
plt.grid()
plt.show()
