# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:08:29 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt

# Gridded Ion Thruster Designer

# General performances
P_input = 1e3 # W
Isp = 3000 # s
eta = 0.75 # Efficiency %

# Physical constants
g0 = 9.81 # Gravitational acceleration (m/s^2)
e = 1.602e-19 # Elementary charge (C)
epsilon0 = 8.854e-12 # Vacuum permittivity (F/m)
kB = 1.38e-23 # Boltzmann constant m^2*kg/(K*s^2)
me = 9.11e-31 # Mass of the electron (kg)

# Design choices
eta_holes = 0.82 # % of holes in the grid
d_holes = 1.4e-3 # Holes diameter (m)
Ti = 400 # Temperature of the ions (K)
Te = 4.5 # Temperature of the electrons (eV)

# Choice of propellant

prop = ['Helium', 'Argon', 'Xenon']

# Helium
m_He = 4 # amu

# Argon
m_Ar = 39.948 # amu

# Xenon
m_Xe = 131.3 # amu

# LXcat data

# Helium
sigma_s_He = 2e-21 # Scaterring cross-section (m^2)
sigma_i_He = 2.5e-21 # Ionisation cross-section (m^2)

# Argon
sigma_s_Ar = 1e-20 # Scaterring cross-section (m^2)
sigma_i_Ar = 2e-20 # Ionisation cross-section (m^2)

# Xenon
sigma_s_Xe = 1e-20 # Scaterring cross-section (m^2)
sigma_i_Xe = 6e-20 # Ionisation cross-section (m^2)

m_prop = [m_He, m_Ar, m_Xe]
sigma_ioniz = [sigma_i_He, sigma_i_Ar, sigma_i_Xe]
sigma_scatter = [sigma_s_He, sigma_s_Ar, sigma_s_Xe]

eta_holes = np.arange(0,101e-2,1e-2)

for i in range(len(prop)):
    L = []
    B = []
    for k in range(len(eta_holes)):
        vi = g0*Isp # Exhaust velocity (m/s)
        P_meca = eta*P_input # Mechanical power (W)
        mi = m_prop[i]*1.66e-27 # Mass of the ion (kg)
        Vp = 1/(2*e)*mi*vi**2 # Potential bewteen first grid and infinity (V)
        mi_dot = 2*P_meca/vi**2 # Mass flow rate (kg/s)
        T = mi_dot*vi # Thrust (N)
        I = mi_dot*e/mi # Total current (A)
        j = (4*epsilon0/9)*np.sqrt(2*e/mi)*Vp**(3/2)/d_holes**2 # Current density (A/m^2)
        j_true = j*eta_holes[k] # Current density that passes through the holes
        S = I/j_true # Grid surface (m^2)
        d = np.sqrt(4*S/np.pi) # Grid diameter (m)
        r = d/2 # Grid radius (m)
        vi_th = np.sqrt(8*kB*Ti/(np.pi*mi)) # Ions thermal velocity (m/s)
        ve_th = np.sqrt(8*e*Te/(np.pi*me)) # Electrons thermal velocity (m/s)
        kc_ioniz = sigma_ioniz[i]*ve_th # m^3/s
        kc_scatter = sigma_scatter[i]*ve_th # m^3/s
        n_ion = mi_dot/(mi*vi_th*S) # Ion density (m^-3)
        lambda_ioniz = vi_th/(sigma_ioniz[i]*ve_th*n_ion) # Ionisation mean free path (m)
        lambda_scatter = vi_th/(sigma_scatter[i]*ve_th*n_ion) # Scattering mean free path (m)
        L.append(2*lambda_scatter) # Approximate chamber length (m)
        
        # The magnetic field must be such that Be<B<Bi
        Be = me*ve_th/(e*L[k])*1e4 # Gauss
        Bi = mi*vi_th/(e*L[k])*1e4 # Gauss
        B.append((Be+Bi)/2) # Gauss

    fig, ax1=plt.subplots()
    
    plt.title(str(prop[i])+' GIT with 1.4 mm diameter grid holes')
    ax1.plot(eta_holes,L,label='Chamber length (m)',c='r')
    ax1.set_xlabel('% of holes in the grid')
    ax1.set_ylabel('Length of the chamber (m)')
    plt.yscale('log')
    plt.legend()
    ax2=ax1.twinx()
    ax2.plot(eta_holes,B,label='Magnetic field (G)')
    ax2.set_ylabel('Magnitude of the magnetic field (G)')
    plt.legend()
