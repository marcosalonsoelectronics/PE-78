# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 10:17:54 2024

@author: Alonso
"""
import numpy as np
from   math import floor, log
import matplotlib.pyplot as plt
Vi=10; Vo=5.0; rC=0.2
L= 100e-6
DVo=0.05 # for hysteretic control
ton=7e-6 # for cot control
fh=rC*Vo*(1 - Vo/Vi)/(DVo*L)
print("Frequency (kHz)= ", fh/1000)
fcot=Vo/(Vi*ton)
print("Frequency (kHz)= ", fcot/1000)

Xmin=6
Xmax=15
Step=0.1
Npoints = floor( (Xmax-Xmin)/Step ) # usa floor para convertir a entero
print ("Npoints =", Npoints)

Vis =     np.arange(Xmin,Xmax,Step, dtype=np.float)
fsh  =    np.arange(Xmin,Xmax,Step, dtype=np.float)
fscot =   np.arange(Xmin,Xmax,Step, dtype=np.float)
DVocot =   np.arange(Xmin,Xmax,Step, dtype=np.float)

for i in range (0, Npoints):
    # frequency under hysteretic control
    fsh[i] = ( rC*Vo*(1 - Vo/Vis[i])/(DVo*L) )/1000
    # frequency under constant on-time control
    fscot[i]= ( Vo/(Vis[i]*ton) )/1000
    # voltage ripple under constant on-time control
    DVocot= (Vis[i] - Vo)*ton*rC/L
    print(Vis[i], DVocot)
   
# Plotting
plt.figure(1)
plt.plot(Vis, fsh,  'blue', label="Hysteretic")
plt.plot(Vis, fscot, 'red', label="COT")
plt.grid(True)
plt.xlabel("Input Voltage (V) $V_i$")
plt.ylabel("Switching Frequency (kHz), $f_s$")
plt.xlim(4,16)
plt.ylim(20,140)
plt.legend()
# plt.xticks(np.arange(0, 10, 1))
# plt.yticks(np.arange(0, 15, 2))
#plt.text(4, 14.6, "My Function", size=14, backgroundcolor='white')
#plt.savefig("My_Function.png", dpi=300)
