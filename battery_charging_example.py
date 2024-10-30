# ===============================================================
# Basic battery charging function
# ===============================================================

'Define variables and units'
soc = 1 # state of charge of the battery [energy, kWh]
power = 1 # power demand [power, kW]
E_total = 1 # energy capacity of the battery [energy, kWh]
P_max = 1 # max power capacity of the battery [power, kW]
T = 1 # length of time of a single period [default 1hr]

'''Define battery charging function 
    soc: updated state of charge of battery at end of period [energy, kWh]
    net_demand: net demand post operation [power, kW]'''
    
def battery_charge_action(soc, power, E_tot, P_max, T):
    
    if power > 0:
        # power is positive, so system is demanding energy from the battery
        # delta_E should be the energy change of the battery, which is negative
        
        deltaE = -1 * min(P_max * T, soc, power * T)

    if power < 0:
        
        # power is negative, so system can charge the battery
        deltaE = min(P_max * T, E_total - soc, -1 * power * T)
        
        
    else:
        
        deltaE = 0
        
    soc += deltaE
    net_power = deltaE * T
        
    return soc, net_power
     

# ===============================================================
# Basic battery class
# ===============================================================    


