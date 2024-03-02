#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:16:58 2023

@author: djordjemihajlovic
"""


from SIRSUpdate import Simulate  # Import SIRSUpdate class to run simulation
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class SIRS(object): #Set up simple class to animate dependent on chosen simulation
    
    def __init__(self, N, pi, pr, ps):
        
        self.SIRS = Simulate(N)
        
        self.pi = pi
        self.pr = pr
        self.ps = ps
        
        self.fig, self.ax = plt.subplots()        
        self.implot = self.ax.imshow(self.SIRS.lattice, cmap = 'Greens')
        self.ani = None # For storing animation object
        
    def run(self):

        self.ani = animation.FuncAnimation(self.fig, self.animate,
                                           interval=2, blit=True)
        plt.show()
        
  
    def animate(self, frame): #This determines each frame of animation
        for i in range (0, 2500): #runs100 simulation 2500 iterations before updating frame / considers all points
            self.SIRS.update(self.pi, self.pr, self.ps) 
        self.implot.set_data(self.SIRS.lattice)

        return self.implot,
    


         
        
        
def main():
    
    initial = int(input("Presents (0), Choice (1) or Immunity (2): "))
    if initial == 0:
        preset = int(input("Absorbing state (0), Dynamic equilibrium (1), Cyclic waves (2): "))
        if preset == 0:
            S = SIRS(50, 0.3, 0.6, 0.1)
            S.run()
        if preset == 1:
            S = SIRS(50, 0.5, 0.5, 0.5)
            S.run()
        if preset == 2:
            S = SIRS(50, 0.8, 0.1, 0.01)
            S.run()
    if initial == 1:
        
        PI = float(input("Probability of infection = "))
        PR = float(input("Probability of recovery = "))
        PS = float(input("Probability of susceptibility = "))
        S = SIRS(50, PI, PR, PS)
        S.run()
     
    if initial == 2:
        
        immunity = float(input("Probability of Immunity = "))
        S = SIRS(50, 0.5, 0.5, 0.5)
        S.SIRS.initial_immune(50, immunity)
        S.run()
    
    
main()
   
