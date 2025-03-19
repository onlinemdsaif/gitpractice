import matplotlib.pyplot as plt
import numpy as np

def draw_square():
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]])
    plt.plot(square[:, 0], square[:, 1], 'r-', label="Square")

def draw_circle():
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot(x, y, 'b-', label="Circle")

def draw_rectangle():
    rectangle = np.array([[0, 0], [2, 0], [2, 1], [0, 1], [0, 0]])
    plt.plot(rectangle[:, 0], rectangle[:, 1], 'g-', label="Rectangle")

def draw_triangle():
    triangle = np.array([[0, 0], [1, 2], [2, 0], [0, 0]])
    plt.plot(triangle[:, 0], triangle[:, 1], 'm-', label="Triangle")

def draw_shapes():
    plt.figure(figsize=(6,6))
    draw_square()
    draw_circle()
    draw_rectangle()
    draw_triangle()

    plt.legend()
    plt.axis("equal")
    plt.title("Geometric Shapes")
    plt.show()

if __name__ == "__main__":
    draw_shapes()
