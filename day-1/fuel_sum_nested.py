import numpy as np

file = open("input.txt", "r") 
fuel_tot = 0

def calc_fuel(mass):
    fuel = np.floor(mass/3.)-2
    return fuel

FUEL_TOT = 0

for line in file.readlines():
    mass = (float(line))
    fuel_tot = 0
    while mass > 0:
        fuel = calc_fuel(mass)
        if fuel < 0:
            fuel = 0
        fuel_tot = fuel+fuel_tot
        mass = fuel
    FUEL_TOT = FUEL_TOT + fuel_tot

print(FUEL_TOT)

 
