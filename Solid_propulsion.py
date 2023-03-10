# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 23:17:32 2023

@author: DECLINE
"""

import numpy as np
import matplotlib.pyplot as plt


# Données
Pe = 0.101325 #MPa
Pa = 0.101325 #MPa
R = 8314
M = 29.8813 #kg
a = 4.1
n = 0.43
F = 5000000 #N
g0 = 9.81
tp = 130
Rho_solide = 1801

# Commencer par la pression de la chambre
Pc = 10

# Prendre dans RPA
gamma = 1.1510
Tc = 3564.41 #K
Isp = 273.3445

# Calcul pour la tuyère
At_Ae = ((gamma+1)/2)**(1/(gamma-1))*(Pe/Pc)**(1/gamma)*np.sqrt((gamma+1)/(gamma-1)*(1-((Pe)/(Pc))**((gamma-1)/gamma)))
cf = np.sqrt(((2*gamma**2)/(gamma-1))*((2/(gamma+1)))**((gamma+1)/(gamma-1))*(1-((Pe)/(Pc))**((gamma-1)/gamma)))+((Pe-Pa)/Pc)*At_Ae
Q_gaz = F/(g0*Isp)
Vreg = 10**(-3)*a*Pc**n # m/s
At = F /(Pc*10**6*cf)
r = R/M
Qt = At * Pc*10**6 /(np.sqrt(r*Tc))*np.sqrt(gamma*(2/(gamma+1))**((gamma+1)/(gamma-1)))
Ae = At / At_Ae
Phi_t = np.sqrt(At*4/np.pi)


# Calcul pour le bloc propergol
Sc = Q_gaz/(Rho_solide*Vreg)
w = Vreg*tp # m
m = Q_gaz*tp
V = m/Rho_solide
H = 4/(np.pi*w**2)*(V-(Sc*w)/2)
Phi_i = Sc/(np.pi*H)
Phi_e = Phi_i + w

print("H =",H,", Phi_i =",Phi_i,", Phi_e =",Phi_e,", Phi_t =",Phi_t)
print("We must have phi_t =",Phi_t,"< phi_i =",Phi_i)