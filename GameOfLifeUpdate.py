import random
import numpy as np
import math

class Simulate(object):
    
    def __init__(self, N): #Random initializer
        self.lattice = np.random.rand(N, N)
        for i in range (0, len(self.lattice)):
            for j in range(0, len(self.lattice)):
                if self.lattice[i][j] < 0.5:
                    self.lattice[i][j] = 0
                else:
                    self.lattice[i][j] = 1 #generating lattice 1 = alive; 0 dead
        
                   
        self.active_data = [np.sum(self.lattice)]
                   
    def glider(self): #Single glider initializer in middle of 50*50 array
        dim = len(self.lattice)           
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][25] = 1 
        self.lattice[25][26] = 1 
        self.lattice[26][24] = 1 
        self.lattice[26][25] = 1 
        self.lattice[26][26] = 1
        
    def blinker(self):
        dim = len(self.lattice)
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][25] = 1
        self.lattice[25][25] = 1
        self.lattice[26][25] = 1
        
    def beehive(self):
        dim = len(self.lattice)
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][25] = 1 
        self.lattice[25][26] = 1 
        self.lattice[26][26] = 1
        self.lattice[25][24] = 1
        self.lattice[26][24] = 1
        self.lattice[27][25] = 1
        
    def update(self):  
        
        dim = len(self.lattice)    
        update = np.zeros((dim,dim))
    
        for i in range (0, len(self.lattice)):
            for j in range(0, len(self.lattice)):
                
                lattice_point = self.lattice[i][j] #lattice point
                
                neighbourR = self.lattice[(i+1)%dim][j] #8 neighbours
                neighbourL = self.lattice[(i-1)%dim][j]
                neighbourT = self.lattice[i][(j+1)%dim]
                neighbourB = self.lattice[i][(j-1)%dim]    
                neighbourDTL = self.lattice[(i+1)%dim][(j+1)%dim]
                neighbourDTR = self.lattice[(i+1)%dim][(j-1)%dim]
                neighbourDBL = self.lattice[(i-1)%dim][(j+1)%dim]
                neighbourDBR = self.lattice[(i-1)%dim][(j-1)%dim]
                
                neighbour_no = neighbourR+ neighbourL+ neighbourT+ neighbourB+ neighbourDTL + neighbourDTR + neighbourDBL + neighbourDBR
                
                if lattice_point == 1:
                
                    if neighbour_no == 2 or neighbour_no == 3 :
                        update[i][j] = 1
                        
                    else:
                        update[i][j] = 0
                        
                else:
                    
                    if neighbour_no == 3:
                        update[i][j] = 1
                        
        self.lattice = update
        

    def count(self):

        active_sites = np.sum(self.lattice)
        self.active_data.append(active_sites)
        
        
        
