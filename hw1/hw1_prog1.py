import numpy

radius = float(input("enter the radius of a sphere: "))
print("to calculate surface area, enter 1 \nto calculate volume, enter 2")

invalid = True
while invalid:
    quantity = int(input("What do you want to calculate: "))
    if quantity ==1:
        surface_area = 4*numpy.pi*numpy.square(radius)
        print("the sphere surface area is ", surface_area)
        invalid = False
    elif quantity ==2:
        volume = (4*numpy.pi*numpy.power(radius, 3))/3
        print("the sphere volume is ", volume)
        invalid = False
    else:
        print("please re-enter a valid choice.")
