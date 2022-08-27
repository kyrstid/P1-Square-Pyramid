print("DeaneP1")
print("Programmer: Kyrsti Deane")
print("Email: kdeane1@cnm.edu")
print("Purpose: Pthyon program provides user capability to calculate the")
print("volume and surface area of a pyramid")

from math import sqrt

length = float(input("Please input the sidelength in feet of the pyramid base: "))
height = float(input("Please input the height in feet of the pyramid: "))

base_area = float(length * length)
volume = float((base_area * height) * 1/3)
slant_height = float(sqrt(pow(height, 2) + pow(length / 2, 2)))

outside = float(1/2 * (length * slant_height))
surface_area = float((1/2 * (length * 4 * slant_height)) + base_area)

print("The volume of the square pyramid equals ", volume)
print("The surface area of the square pyramid equals ", surface_area)




