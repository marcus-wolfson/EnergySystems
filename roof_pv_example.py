"""In-class practice problem, Week 3 Tuesday (10/29/2024)

Problem: calculate maximum number and power capacity (in kWp) of solar PV
panels that can fit on an angled roof. Rectangular shed-style roof, rectangular
panels, no overhang."""

import numpy as np

# Inputs
building_width = 8 #meters
building_length = 28 #meters
roof_angle = 22 #degrees
pv_width = 1690 #mm
pv_height = 1046 #mm
pv_power = 400 #Wp

# Calculate maximum number of panels
def max_number_of_panels(building_width, building_length, roof_angle, pv_width, pv_height):
    
    # roof is angled in the middle, so the roof_width must be divided by 2
    # this is because if there is >1/2 width of panel space left, doing it
    # all at once will result in thinking a whole panel could be built.
   angled_roof_width = ( building_width / np.cos(np.deg2rad(roof_angle)) ) / 2
    
   pv_fit_width = np.floor(angled_roof_width / (pv_width/1000)) #meters
   
   pv_fit_length = np.floor(building_length / (pv_height/1000)) #meters
   
   pv_total = (pv_fit_width * 2) * pv_fit_length # count
   
   return pv_total


def pv_power_capacity(pv_total, pv_power):
    
    power_capacity = pv_total * pv_power / 1000 #kPW
    
    return power_capacity


pv_total = max_number_of_panels(building_width, building_length, roof_angle, pv_width, pv_height)
power_capacity = pv_power_capacity(pv_total, pv_power)

print("pv_total:",pv_total," and pv_power_capacity [kWp]:",power_capacity)




    
    

