import math

def area_circle(x):
    return round(math.pi * x * x)

def circumference(x):
  return round(math.pi * 2 * x)

radius = float(input("Please input the radius of the circle: "))
print("Area of the circle: ", area_circle(radius))
print("Circumference of the circle: ", circumference(radius))
