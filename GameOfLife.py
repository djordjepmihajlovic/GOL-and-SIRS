#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 22:16:58 2023

@author: djordjemihajlovic
"""

from GameOfLifeUpdate import Simulate
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GameOfLife(object):  # Set up simple class to animate dependent on chosen simulation
    
    def __init__(self, N):
        
        self.GOL = Simulate(N)
        
        self.fig, self.ax = plt.subplots()        
        self.implot = self.ax.imshow(self.GOL.lattice, cmap = 'gray')
        self.ani = None # For storing animation object
        
    def run(self):

        self.ani = animation.FuncAnimation(self.fig, self.animate,
                                           interval=5, blit=True)
        plt.show()

        
    def animate(self, frame): #This determines each frame of animation
        self.GOL.update()
        self.implot.set_data(self.GOL.lattice)
        self.GOL.count() #want to compare previous GOL counts every 10

        return self.implot,
    
         
def main():
    
    Sim = int(input("Simulation type, 0 for random, 1 for glider, 2 for blinker, 3 for beehive = "))
    S = GameOfLife(100)
    if Sim == 1:
        S.GOL.glider()
        
    if Sim == 2:
        S.GOL.blinker()
        
    if Sim == 3:
        S.GOL.beehive()
        
    
   
    S.run()

    
main()
   
