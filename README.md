# GOL-SIRS
Game of life &amp; the SIRS model

Game Of Life.

To run visualization: run GameOfLife file, user will be prompted accordingly
To run data finder (Histogram & Glider Center of Mass): run GameOfLifeData file WARNING: will take long -2 hours- to generate all data

SIRS

To run visualization: run SIRS file, user will be prompted accordingly
To run data finder (Wave position, Phase diagram, Immunity vs infection): run SIRSData WARNING: again, will take long -2 hours- to generate all data


INFO ABOUT CODE & CHOICES MADE IN IMPLEMENTATION:

For the game of life part of the checkpoint 3 different files consisting of 3 different classes,
the first file is used to initialize the lattice and has functions for the update rule, it also has a few
other initializers such as beehive, glider etc to demonstrate their behaviour.
The second file is an animation class used to utilize the update class, it also prompts the user 
for the required simulation. Finally there is the data class which again utilizes the update file to run the 
simulation a number of times to determine the number of iterations required to reach equilibrium.

Specifics on Histogram:
In order to determine the number of iterations required to reach equilibrium a function to calculate activity is implemented
that analyzes the count of active sites of the lattice. Every 10 iterations a list of the 10 most recent counts 
of active sites is compared in two ways:
the average of the list is compared to the average of the previous 10
the number of active sites is compared i.e is it fluctuating or staying the same; if fluctuating is the fluctuation constant
i.e. is the unique number of counts of active sites the same.
Once both these requirements is met the program is at equilibrium.

Specifics on Center of Mass:
For the center of mass data the position of active sites per time step is found and averaged over,
in order to eliminate boundary changing data the difference in position of active sites is compared:
at most for the glider the position of active sites differs by a value of 2, when crossing the boundary however this
number is ~50 (the size of the lattice) hence to elimate this data I've removed all points which correspond to a difference
that is greater than 2 i.e. part of the glider is at [50][50] and another is [0][0] = difference between previous x,y and current
x, y > 2.

For the SIRS simulator 3 different files with 3 classes.
The first two classes act similar to the Game of Life where one determines the intial set up and update rules,
the second is a animation class to visualize the update rule with a set of presets to choose from.
The third class is a data class to determine required data from the SIRS model with 3 functions:
one function to determine the phase diagram, one to determine the area that waves occur and the other to determine behaviour 
according to changing immunity.


All code is run simply running the file either through terminal or any IDE and following the user prompts.
