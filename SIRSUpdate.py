#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 14:18:32 2023

@author: djordjemihajlovic
"""

import random
import numpy as np
import math

class Simulate(object):
    
    def __init__(self, N): #Random initializer
       self.cycle = 0
       self.lattice = np.random.rand(N, N)
       for i in range (0, len(self.lattice)):
           for j in range(0, len(self.lattice)):
               if self.lattice[i][j] <= 0.33:
                   self.lattice[i][j] = -1
                   
               elif self.lattice[i][j] <= 0.66:
                   self.lattice[i][j] = 0
                   
               else:
                   self.lattice[i][j] = 1 #generating lattice 1 infected; 0 susceptible; -1 recovered
                   
    def update(self, pi, pr, ps):  
        
        dim = len(self.lattice)    
    
        i = random.choice(list(range(0, dim)))
        j = random.choice(list(range(0, dim)))
         
        if self.lattice[i][j] == 0:
            
            neighbourR = self.lattice[(i+1)%dim][j] #8 neighbours
            neighbourL = self.lattice[(i-1)%dim][j]
            neighbourT = self.lattice[i][(j+1)%dim]
            neighbourB = self.lattice[i][(j-1)%dim]    
            
            neighbour_no = neighbourR+ neighbourL+ neighbourT+ neighbourB 
        
            if neighbour_no >= 1:
                
                R1 = random.random()
                if R1<pi:
                    self.lattice[i][j] = 1

        elif self.lattice[i][j] == 1:
            
            R2 = random.random()
            if R2<pr:
                self.lattice[i][j] = -1
                
        else:
            
            R3 = random.random()
            if R3<ps:
                self.lattice[i][j] = 0
            
    def initial(self, N):
        self.lattice = np.zeros((N,N))
        for i in range (len(self.lattice)-5, len(self.lattice)):
            for j in range (len(self.lattice)-5, len(self.lattice)):
                self.lattice[i][j] = 1
            
            
    def updateexp(self, pi, pr, ps):  #experimenting with hemispheres
    
        self.cycle = self.cycle + (math.pi/200000)
        
        dim = len(self.lattice)    
    
        i = random.choice(list(range(0, dim)))
        j = random.choice(list(range(0, dim)))
         
        if self.lattice[i][j] == 0:
            
            neighbourR = self.lattice[(i+1)%dim][j] #8 neighbours
            neighbourL = self.lattice[(i-1)%dim][j]
            neighbourT = self.lattice[i][(j+1)%dim]
            neighbourB = self.lattice[i][(j-1)%dim]    
            
            neighbour_no = neighbourR+ neighbourL+ neighbourT+ neighbourB 
        
            if neighbour_no >= 1:
                
                R1 = random.random()
                if R1*math.sin(self.cycle)*4<pi:
                        self.lattice[i][j] = 1

        elif self.lattice[i][j] == 1:
            
            R2 = random.random()
            if R2<pr:
                self.lattice[i][j] = -1
                
        else:
            
            R3 = random.random()
            if R3<ps:
                self.lattice[i][j] = 0