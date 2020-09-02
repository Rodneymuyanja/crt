import math 

electron_charge = 1.6E-10
electron_mass = 9.11E-31

def accelerating_velocity(voltage):
    v = (2*electron_charge*voltage)/electron_mass

    vel = math.sqrt(v)
    velocity = "{:.3e}".format(vel)
    print(velocity)
    return vel

def focusing_velocity(voltage):
    v = (2*electron_charge*voltage)/electron_mass
    vel = math.sqrt(v)
    velocity = "{:.3e}".format(vel)
    print(velocity)

    return velocity

def anode(accelerating_voltage, focusing_voltage):
    acceleration = accelerating_velocity(accelerating_voltage)
    focus = focusing_velocity(focusing_voltage)  

    return acceleration, focus




