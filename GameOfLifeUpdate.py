import numpy as np

class Simulate(object):  # Create class for update method of Game of Life
    
    def __init__(self, N): #Random initializer for lattice of dimension size N
        self.lattice = np.random.rand(N, N)
        for i in range (0, len(self.lattice)):
            for j in range(0, len(self.lattice)):
                if self.lattice[i][j] < 0.5:
                    self.lattice[i][j] = 0
                else:
                    self.lattice[i][j] = 1  # Generating lattice 1 = alive; 0 dead
        
                   
        self.active_data = [np.sum(self.lattice)]  # Initial number of active points
                   
    def glider(self): #Single glider initializer in middle of empty lattice
        dim = len(self.lattice)
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][25] = 1 
        self.lattice[25][26] = 1 
        self.lattice[26][24] = 1 
        self.lattice[26][25] = 1 
        self.lattice[26][26] = 1
        
    def blinker(self):  # Single blinker initializer in middle of empty lattice
        dim = len(self.lattice)
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][25] = 1
        self.lattice[25][25] = 1
        self.lattice[26][25] = 1
        
    def beehive(self):  # Single beehive initializer in middle of empty lattice
        dim = len(self.lattice)
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][25] = 1 
        self.lattice[25][26] = 1 
        self.lattice[26][26] = 1
        self.lattice[25][24] = 1
        self.lattice[26][24] = 1
        self.lattice[27][25] = 1
        
    def tester1(self):  # Example test situation for fluctuating equilibrium
        
        dim = len(self.lattice)           
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][24] = 1 
        self.lattice[25][24] = 1 
        self.lattice[24][25] = 1 
        
        self.lattice[26][27] = 1 
        self.lattice[27][26] = 1 
        self.lattice[27][27] = 1 
        
    def tester2(self):  # Example test situation for finding equilibrium when glider can move for a lot of steps before causing change
        
        dim = len(self.lattice)           
        self.lattice = np.zeros((dim,dim))
        self.lattice[24][24] = 1 
        self.lattice[25][24] = 1 
        self.lattice[24][25] = 1 
        
        self.lattice[26][27] = 1 
        self.lattice[27][26] = 1 
        self.lattice[27][27] = 1 
        
        self.lattice[28][29] = 1 
        self.lattice[29][30] = 1 
        self.lattice[30][28] = 1 
        self.lattice[30][29] = 1
        self.lattice[30][30] = 1
        

        
    def update(self):  # Update method class
        
        dim = len(self.lattice)  # Define dimension    
        update = np.zeros((dim,dim))  # Create empty update lattice: points made active accordingly
    
        for i in range (0, len(self.lattice)):
            for j in range(0, len(self.lattice)):  # Summing over all lattice points
                
                lattice_point = self.lattice[i][j]  # Lattice point of concern
                
                neighbourR = self.lattice[(i+1)%dim][j] # 8 nearest neighbours with boundary conditions
                neighbourL = self.lattice[(i-1)%dim][j]
                neighbourT = self.lattice[i][(j+1)%dim]
                neighbourB = self.lattice[i][(j-1)%dim]    
                neighbourDTL = self.lattice[(i+1)%dim][(j+1)%dim]
                neighbourDTR = self.lattice[(i+1)%dim][(j-1)%dim]
                neighbourDBL = self.lattice[(i-1)%dim][(j+1)%dim]
                neighbourDBR = self.lattice[(i-1)%dim][(j-1)%dim]
                
                neighbour_no = neighbourR+ neighbourL+ neighbourT+ neighbourB+ neighbourDTL + neighbourDTR + neighbourDBL + neighbourDBR
                
                if lattice_point == 1:  # Update rules according to number of active neighbours
                
                    if neighbour_no == 2 or neighbour_no == 3 :
                        update[i][j] = 1  # Empty update lattice updated accordingly
                        
                    else:
                        update[i][j] = 0
                        
                else:
                    
                    if neighbour_no == 3:
                        update[i][j] = 1
                        
        self.lattice = update
        

    def count(self):

        active_sites = np.sum(self.lattice)  # Number of active sites in lattice
        return active_sites
        
        
        
