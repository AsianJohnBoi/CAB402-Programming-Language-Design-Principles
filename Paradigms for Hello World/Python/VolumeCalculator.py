import math #module to access math functions

#Function to calculate the volume of the cylinder
def volume_cylinder(r, h): 
    volume = math.pi * (r ** 2) * h #Uses volume formula (pi x radius x height)
    return volume

#Listens for user input
radius = input("What is the radius of the cylinder?") 
height = input("What is the height of the cylinder?")

#Calls the function to calculate volume
volume = volume_cylinder(float(radius), float(height))

#prints result
print("The volume is {0}".format(volume))