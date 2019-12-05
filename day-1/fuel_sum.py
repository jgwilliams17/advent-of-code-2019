import numpy as np

file = open("input.txt", "r") 
fuel_tot = 0

for line in file.readlines():
    mass = (float(line))
    fuel = np.floor(mass/3.)-2
    fuel_tot = fuel+fuel_tot

print(fuel_tot)

 
