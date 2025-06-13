#Write a program that takes the radius of a sphere (a floating-point number) 
#as input and then outputs the sphere's diameter, circumference, surface area, and volume.
import math
r= float(input("Enter the radius of Sphere: "))
diameter = 2*r
Surface_area = 4*math.pi*(r**2)
Volume = (4/3)*math.pi*(r**3)
print("Diameter of Sphere is: ", diameter)
print("Surface area of Sphere is: ", Surface_area)
print("Volume of Sphere is: ", Volume)