# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:21:59 2023

@author: djord
"""

from SIRSUpdate import Simulate
import numpy as np
import matplotlib.pyplot as plt
import random


class SIRSfluc(object): #Set up simple class to analyze data dependent on chosen simulation
    
    def __init__(self, pr):  # Initially set probability of recovery; only variable constant throughout analyzing all required data
        self.pr = pr

    def phase_diagram(self):
        
        pi = np.arange(0, 1, 0.05)
        ps = np.arange(0, 1, 0.05)
        infection_average = []
        for i in range (0, len(pi)):  # iterate over range of probability for infection and susceptibility
            for j in range (0, len(ps)):
                self.SIRS = Simulate(50)
                infected_data = []
                for k in range (0, 500):  # chose 500 iterations due to time constraints, found to still be accurate
                    for l in range (0, 2500):
                        self.SIRS.update(pi[i], self.pr, ps[j])
                    if k > 100:  # Find infection average after 100 iterations i.e. after equilibrium reached
                        I = self.SIRS.infected()
                        infected_data.append(I)
                infected_data = np.array(infected_data)
                average = np.mean(infected_data)
                infection_average.append(average)
                file = open("PI VS PS.txt", "a") 
                file.write("infection average: " + str(average) + ", PI: " + str(pi[i]) + ", PS: "+ str(ps[j])+ ".\n")
                file.close()
            print(str(i) + " Done")
                
        return infection_average, pi, ps
    
    
    def waves(self, ps):
        
        pi = np.arange(0.2, 0.51, 0.01)
        self.ps = ps
        
        infection_variance = []
        error = [0] * len(pi)
        for i in range (0, len(pi)):

            self.SIRS = Simulate(50)
            infected_data = []
            for k in range (0, 10000):
                for l in range (0, 2500):
                    self.SIRS.update(pi[i], self.pr, self.ps)
                if k > 100:
                    I = self.SIRS.infected()
                    infected_data.append(I)
                    
                if k%1000 == 0:
                    print(str(k/100) + "% done.")
                    
            infected_data = np.array(infected_data)
            variance = np.var(infected_data)
            variance = variance/2500
            infection_variance.append(variance)
            file = open("Waves.txt", "a") 
            file.write("infection variance: " + str(variance) + ", PI: " + str(pi[i]))
            file.close()
            print(str(i) + " Done")
            

            
            
            error_data = [] # Calculated error using resampling bootstrap method 
            for j in range(1000):#no. of resamplings
                resample_infected_data = random.choices(infected_data, k=len(infected_data))
                err = np.var(resample_infected_data)
    
                error_data.append(err)
            error[i] = np.std(error_data)
            error[i] = error[i]/2500
            file = open("Waves.txt", "a") 
            file.write(" with std. error: " + str(error[i]) + ".\n")
            file.close()
        
        return infection_variance, pi, error
    
    
    def immunity_infection(self):
        
        vax = np.arange(0, 1, 0.025)  # Set up possible range of immunity percentage of population
        infection_average = []
        for i in range (0, len(vax)):  # Iterate over different immunities
            self.SIRS = Simulate(50)
            infected_data = []
            self.SIRS.initial_immune(50, vax[i])
            for k in range (0, 1000):
                for l in range (0, 2500):
                    self.SIRS.update(0.5, 0.5, 0.5)
                if k > 100:
                    I = self.SIRS.infected()
                    infected_data.append(I)
            infected_data = np.array(infected_data)
            average = np.mean(infected_data)  # Find average infection
            infection_average.append(average)
            file = open("Immunity vs Infection.txt", "a") 
            file.write("infection average: " + str(average) + ", immunity " + str(vax[i]) + ".\n")
            file.close()
            print(str(i) + " Done")
                
        return infection_average, vax
      
def main():

    # S = SIRSfluc(0.5)
    # infection_average, pi, ps = S.phase_diagram()
    # infection_average = np.array(infection_average).reshape(len(pi), len(ps))

    # fig, ax = plt.subplots()
    # im = ax.imshow(infection_average, extent = (pi.min(), pi.max(), ps.min(), ps.max()), cmap='viridis')

    # cbar = ax.figure.colorbar(im, ax=ax)
    # cbar.ax.set_ylabel("Average infection rate", rotation=-90, va="bottom")
    # plt.xlabel("Probability of Susceptibility")
    # plt.ylabel("Probability of Infection")
    
    
    S = SIRSfluc(0.5)
    infection_variance, pi, error = S.waves(0.5)
    plt.plot(pi, infection_variance)
    plt.errorbar(pi, infection_variance, yerr= error, fmt=".k")
    plt.title("Infection variance vs Probability of infection at PR = PS = 0.5")
    plt.xlabel("Probability of Infection")
    plt.ylabel("Infection variance")
    
    # S = SIRSfluc(0.5)
    # infection_average, vax = S.immunity_infection()
    # plt.plot(vax, infection_average)
    # plt.xlabel("Immunity percentage.")
    # plt.ylabel("Infection average.")
    

main()