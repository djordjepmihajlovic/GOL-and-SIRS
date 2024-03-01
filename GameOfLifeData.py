# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:40:56 2023

@author: djord
"""

from GameOfLifeUpdate import Simulate
import matplotlib.pyplot as plt
import numpy as np
import math


class GameOfLife(object):  # Set up class to determine required data from game of life using game of life update class
    
    def __init__(self, N):
        
        self.GOL = Simulate(N)  # Create simulation of size N
        
    def activity(self):  # Function used to determine number of active sites
        
        test_freq = 10  # How often to compare number of active sites (i.e every 10 counts compare change in activity)
        time = 0  # time of iteration (single iteration = 1 timestep)
        unique = 0  # Initializer of unique variable - unique is used to determine how often number of active sites has changed in "test freq" number of iterations. i.e. if constant = no change in active site number
        
        active_site_data = []  # Empty list to save active site numbers
        prev_average = 0  # Initializer
        prev_unique = 1  # Initializer
        average = self.GOL.count()  # initial average (first count)
        
        while prev_unique != unique or prev_average != average:  # while statement to run while active site number is changing
            
            prev_unique = unique
            prev_average = average
            for i in range(0 , test_freq):
                time += 1 
                self.GOL.update()
                active_count = self.GOL.count()
                active_site_data.append(active_count)
            prev_iter = active_site_data[-test_freq:]
            unique = set(prev_iter)  # unique number of active site counts 
            average = sum(unique)/len(unique)  # average of unique set
        
        return time
    
    def centre_of_mass(self):  # Function for finding center of mass
        self.GOL.glider()  # Initialize glider
        position_data = []
        position_average_data = []
        
        for i in range(0, 500):  # Run simulation 500 times, determine active sites every timestep 
            self.GOL.update()
            position_iteration = []
            for j in range(0, len(self.GOL.lattice)):
                for k in range(0, len(self.GOL.lattice)):
                    if self.GOL.lattice[j][k] == 1:
                        position_iteration.append([j,k])
                        
            position_data.append(position_iteration)  # Data of active sites per timestep - used to find center of mass
            
        for i in range(0, len(position_data)):  # Determine center of mass of set of active sites per timestep
            x = np.array(position_data[i])
            X_sum = 0
            Y_sum = 0
            difference_data = []
            for j in range(0, len(position_data[i])):
                Y_ax = x[j][0]
                X_ax = x[j][1]
                difference = abs(X_ax - Y_ax)
                difference_data.append(difference)
                X_sum += X_ax
                Y_sum += Y_ax
            
            if all (x <= 2 for x in difference_data):  # Used to remove center of mass data while glider crosses boundary (loops back)
                position_averageX = X_sum/len(position_data[i])
                position_averageY = Y_sum/len(position_data[i])
                position_averagesq = (position_averageX**2) + (position_averageY**2)
                position_average = math.sqrt(position_averagesq)
                position_average_data.append(position_average)
            
            
            
        time = np.arange(0, len(position_average_data), 1)  # Timestep
        
        dx = time[50]-time[0]
        dy = position_average_data[50]-position_average_data[0]
        velocity = dy/dx  # Calculate gradient = velocity of Glider
        
        print("Gliders speed along lattice is: " + str(velocity))  # speed found in run used to find data: 0.3535183652558746
        
        return time, position_average_data
                

def main():  # main class to run previously defined data finding functions and return suitable plots
    
    time_data = []
    
    for i in range(0, 500):
        R = GameOfLife(50)
        time = R.activity()
        time_data.append(time)
        file1 = open("Histogram Data.txt", "a") 
        file1.write("Simulation: " + str(i) + ". No. Iterations: " + str(time) + ".\n")
        file1.close()
        print("Simulation " + str(i) + " completed.")
        
    f = plt.figure(1);
    plt.hist(time_data)
    plt.xlabel("Time to Equilibrium (no. of iterations)")
    plt.ylabel("Frequency")
    plt.title('Equilibrium time: Game of Life.')
    f.show()
    
    S = GameOfLife(50)
    time, pos_avg = S.centre_of_mass()
    
    for i in range(0, len(time)):
        file2 = open("Glider Data.txt", "a") 
        file2.write("Time: " + str(time[i]) + ". Centre of Mass: " + str(pos_avg[i]) +".\n")
        file2.close()
    
    g = plt.figure(2)
    plt.plot(time, pos_avg)
    plt.xlabel("Time")
    plt.ylabel("Centre of Mass")
    plt.title('Glider Movement as function of time.')
    g.show()

main()
        

        