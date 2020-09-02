import math
from deflectingSystem.plates import plates

electron_charge = 1.6E-10
electron_mass = 9.11E-31

def y_plates(breadth,length,distance_from_screen,voltage_across,anode_velocity):
    vertical = plates(breadth,length,distance_from_screen)
    voltage = voltage_across
    #electrical force,E
    E = voltage / vertical.length #v/m
    eE = electron_charge*E
    time = vertical.length / anode_velocity #seconds

    def verticalVelocity():
        finalVelocity = ((eE*time)/electron_mass) #m/s
        velocity = "{:.3e}".format(finalVelocity)
        return finalVelocity, velocity
        
    def vertical_Distance():
        verticalDistance = (eE/(electron_mass*(anode_velocity**2)))*(vertical.length**2)
        verticaldist = "{:.3e}".format(verticalDistance)
        return verticaldist
        
    def angleOffHorizontal(verticalVelocity):
        angl = math.atan((eE*vertical.length)/(electron_mass*(anode_velocity**2)))
        angle = "{:.3e}".format(angl)
        deg_Angle = math.degrees(angl) #np.rad2deg(angl)
        return deg_Angle, angl

#from original direction
    def displacementOffHorizontal(angleInDegrees):
        angle = math.radians(angleInDegrees)
        displace = (math.tan(angle))*(vertical.dist_from_screen + (vertical.length/2))
        displacement = "{:.3e}".format(displace)
        return displacement, displace

    verticalVelocity, v = verticalVelocity()
    verticalDistance = vertical_Distance()
    angle_str,angle = angleOffHorizontal(verticalVelocity)
    displacement , displace = displacementOffHorizontal(angle_str)

    return verticalVelocity, verticalDistance, angle_str, displace
