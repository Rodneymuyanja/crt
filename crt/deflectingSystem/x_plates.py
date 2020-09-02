import math
from deflectingSystem.plates import plates

electron_charge = 1.6E-10
electron_mass = 9.11E-31

def x_plates(breadth,length,distance_from_screen,maximumVoltage,minimumVoltage,Verticalvelocity):
    horizontal = plates(breadth,length,distance_from_screen)
    #electrical force,E
    E = minimumVoltage / horizontal.length #v/m
    Emax = maximumVoltage / horizontal.length 
    eEmax = electron_charge*Emax

    eE = electron_charge*E
    time = horizontal.length / Verticalvelocity #seconds

    halfPlateLength = horizontal.length/2
    radius = halfPlateLength + horizontal.dist_from_screen

    def angularVelocity():
        #if we observe a whole revolution it'd make a circle
        #since thats the aim of the electric field 
        #with a radius
        #angular velocity, w
        w = Verticalvelocity / radius

        return w

    def displacementOffVertical(angularVelocity):
        try:
            displacement = eE / ((angularVelocity**2)*electron_mass)

            try:
                amplitude = eEmax / ((angularVelocity**2)*electron_mass)
            except ZeroDivisionError as identifier:
                print("division by zero.......switching amplitude to zero")
                amplitude = 0

        except ZeroDivisionError as zero:
            print("division by zero.......switching displacement to zero")
            #elE = elE only reset to zero 
            displacement = 0 #elE / ((angularVelocity**2)*electron_mass)

        return displacement, amplitude   

    def angleOffVertical(displacement, amplitude):
        temp = displacement/radius
        temp2 = amplitude / radius
        maxAngl = math.atan(temp2)
        angl = math.atan(temp)
        angle = math.degrees(angl)
        maxAngle = math.degrees(maxAngl)

        return angle, maxAngle   

    w = angularVelocity()   
    displacement, amplitude = displacementOffVertical(w)
    angle, maximumAngle = angleOffVertical(displacement, amplitude)

    return w, displacement, amplitude, angle, maximumAngle, eEmax

    #def horizontalVelocity(angularVelocity,amplitude, displacement):
        

def SMH (amplitude, displacement, angle, maxAngle, angularvelocity, eEmax):
    maximumVelocity = None
    maximumAcceleration = None
    try:
        if  angle == 0 and displacement == amplitude:
            maximumVelocity = eEmax / (angularvelocity*electron_mass)
            acceleration = 0
        elif (angle == maxAngle):
            maximumAcceleration = (angularvelocity**2)*amplitude
            maximumVelocity = 0
        else:
            speed = (amplitude**2) - (displacement**2)
            velocity = math.sqrt(speed)
            acceleration = (angularvelocity**2)*displacement
    except ZeroDivisionError as zero:
        print("no maximum velocity")

    return maximumVelocity, maximumAcceleration, acceleration, velocity    
            


