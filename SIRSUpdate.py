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
       self.number_immune = 0
       self.lattice = np.random.rand(N, N)
       for i in range (0, len(self.lattice)):  # Equally initialized (random)
           for j in range(0, len(self.lattice)):
               if self.lattice[i][j] <= 0.33:
                   self.lattice[i][j] = -1
                   
               elif self.lattice[i][j] <= 0.66:
                   self.lattice[i][j] = 0
                   
               else:
                   self.lattice[i][j] = 1 #generating lattice 1 infected; 0 susceptible; -1 recovered
                   
    def update(self, pi, pr, ps):  # Function to implement update rule
        
        dim = len(self.lattice)    
    
        i = random.choice(list(range(0, dim)))
        j = random.choice(list(range(0, dim)))
         
        if self.lattice[i][j] == 0:
            
            neighbourR = self.lattice[(i+1)%dim][j] #4 neighbours
            neighbourL = self.lattice[(i-1)%dim][j]
            neighbourT = self.lattice[i][(j+1)%dim]
            neighbourB = self.lattice[i][(j-1)%dim]    
            
        
            if neighbourR == 1 or neighbourL == 1 or neighbourT == 1 or neighbourB == 1:  # If any neighbours infected - chance infection
                
                R1 = random.random()
                if R1<pi:
                    self.lattice[i][j] = 1

        elif self.lattice[i][j] == 1:
            
            R2 = random.random()
            if R2<pr:
                self.lattice[i][j] = -1
                
        elif self.lattice[i][j] == -1:
            
            R3 = random.random()
            if R3<ps:
                self.lattice[i][j] = 0
                
                
                
    def infected(self):  # Number infected sites
        
        infected = 0
        
        for i in range(0, len(self.lattice)):
            for j in range(0, len(self.lattice)):
                if self.lattice[i][j] == 1:
                    infected += 1
                    
        return infected
    
    def initial_immune(self, N, immune):  # Initializer for immunity (sets x number of agents to be immune at start dependent on percent immune given)
        
        self.lattice = np.random.rand(N, N)
        
        for i in range (0, len(self.lattice)):
            for j in range(0, len(self.lattice)):
                if self.lattice[i][j] <= 0.33:
                    self.lattice[i][j] = -1
                    
                elif self.lattice[i][j] <= 0.66:
                    self.lattice[i][j] = 0
                    
                else:
                    self.lattice[i][j] = 1 #generating lattice 1 infected; 0 susceptible; -1 recovered    
                   
        for k in range (0, len(self.lattice)):
            for l in range (0, len(self.lattice)):
                R = random.random()
                if R<immune:
                    self.lattice[k][l] = -2  # IMMUNE
                
                
                
     # Below this is experimental code // NOT PART OF CHECKPOINT was done out of interest to simulate seasonal disease.
     # ***************************************************************************************************************          
                
            
    # def initial(self, N):
    #     self.lattice = np.zeros((N,N))
    #     for i in range (len(self.lattice)-5, len(self.lattice)):
    #         for j in range (len(self.lattice)-5, len(self.lattice)):
    #             self.lattice[i][j] = 1
            
            
    # def updateexp(self, pi, pr, ps):  #experimenting with hemispheres
    
    #     self.cycle = self.cycle + (math.pi/200000)
        
    #     dim = len(self.lattice)    
    
    #     i = random.choice(list(range(0, dim)))
    #     j = random.choice(list(range(0, dim)))
         
    #     if self.lattice[i][j] == 0:
            
    #         neighbourR = self.lattice[(i+1)%dim][j] #8 neighbours
    #         neighbourL = self.lattice[(i-1)%dim][j]
    #         neighbourT = self.lattice[i][(j+1)%dim]
    #         neighbourB = self.lattice[i][(j-1)%dim]    
            
    #         neighbour_no = neighbourR+ neighbourL+ neighbourT+ neighbourB 
        
    #         if neighbour_no >= 1:
                
    #             R1 = random.random()
    #             if R1*math.sin(self.cycle)*4<pi:
    #                     self.lattice[i][j] = 1

    #     elif self.lattice[i][j] == 1:
            
    #         R2 = random.random()
    #         if R2<pr:
    #             self.lattice[i][j] = -1
                
    #     else:
            
    #         R3 = random.random()
    #         if R3<ps:
    #             self.lattice[i][j] = 0