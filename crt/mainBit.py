from electronGun.anode import anode
from deflectingSystem.y_plates import y_plates
from deflectingSystem.x_plates import x_plates
from deflectingSystem.x_plates import SMH
import math

def main():
    accelerating , focusing = anode(1500, 600)
    print(accelerating, "m/s")
    print(focusing, "m/s")
    
    print("......starting vertical deflection........")
    x = -1000
    velocity, verticalDistance, angle, displacement_y = y_plates(0.03,0.08,0.2,x,accelerating)
    print("velocity", velocity,"m/s")
    print("verticalDistance", verticalDistance,"m")
    print("angle off horizontal", angle,"degrees")
    print("displacement", displacement_y,"m")
    
    print("........starting horizontal displacement...........")
    w, displacement_x, amplitude, angleH, maximumAngle, eEmax = x_plates(0.03,0.08,0.11,600,100,velocity)
    maximumVelocity, maximumAcceleration, acceleration, velocity = SMH(amplitude,displacement_x,angleH,maximumAngle,w,eEmax)

    print("velocity", velocity,"m/s")
    print("acceleration", acceleration,"m/s2")
    print("amplitude", amplitude,"m")
    print("angle off vertical", angleH,"degrees")
    print("displacement", displacement_x,"m")
    print("maxvelocity", maximumVelocity,"m/s")
    print("maxAcc", maximumAcceleration,"m")
    
main()
