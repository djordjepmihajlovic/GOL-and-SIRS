#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:16:58 2023

@author: djordjemihajlovic
"""

from SIRSUpdate import Simulate
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
        for i in range (0, 2500): #runs100 simulation 2500 iterations before updating frame
            self.SIRS.update(self.pi, self.pr, self.ps) 
        self.implot.set_data(self.SIRS.lattice)

        return self.implot,
    


         
        
        
def main():
    N = int(input("Lattice Dimension = "))
    PI = float(input("Probability of infection = "))
    PR = float(input("Probability of recovery = "))
    PS = float(input("Probability of susceptibility = "))
    S = SIRS(N, PI, PR, PS)
    S.SIRS.initial(N)
    S.run()
     #change between kawasaki and glauber, S.runG() = Glauber, S.runK() = Kawasaki
    
    
main()
   
