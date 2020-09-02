#we'll consider tungsten as we start since different metals have different 
#temperature coefficients 

def filament(metal):
    coefficients = {"tungsten":0.004403}
    used_metal = coefficients[metal]

    return used_metal


def cathode (voltage, initial_temperature, power, metal):
    t = 0 #this is more of a counter not temperature
    current = power / voltage
    initial_resistance = voltage / current #ohms
    print (initial_resistance,"ohms init")

    coefficient = filament(metal)

    temperature = (coefficient*initial_resistance*initial_temperature) / (coefficient*initial_resistance)
    #temperature_difference = temp - initial_temperature

    while (temperature < 800):
        t = t + 1
        print(t,"sec")
        #power = power * 1.1
        voltage = voltage * 1.1
        print(voltage,"V")
        new_current = power / voltage
        print(new_current,"A")
        resistance = voltage / new_current
        #resistance = second_resistance * (1 + coefficient*temperature_difference)
        print(resistance,"ohms")
        #temperature = ( (coefficient * resistance * temperature)) / coefficient * resistance
        temperature = (resistance - initial_resistance*(1 + (coefficient*temperature)))/(coefficient*initial_resistance)
        print(temperature,"celcius")
       

            

cathode(240,29,350,"tungsten")









