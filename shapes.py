import math

def square_area(side):
    return side * side

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

# Example Usage
if __name__ == "__main__":
    print("Square Area:", square_area(5))
    print("Circle Area:", circle_area(7))
    print("Rectangle Area:", rectangle_area(4, 6))
    print("Triangle Area:", triangle_area(3, 8))
