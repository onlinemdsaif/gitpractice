import math

def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == "__main__":
    r = float(input("Enter the radius: "))
    print("Circle Area:", circle_area(r))
