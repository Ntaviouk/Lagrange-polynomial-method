import math
import numpy as np
import matplotlib.pyplot as plt


def Func(x):
    return math.sinh(x)


def lagrange_polynomial(x, x_values, y_values):
    n = len(x_values)
    s = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        s += term

    return s


def draw(lst1, lst2, x):
    x_values = np.linspace(0, 3, 400)
    y_values = [Func(x) for x in x_values]

    plt.plot(x_values, y_values)
    plt.title('Графік функції sinh(x)')
    plt.xlabel('x')
    plt.ylabel('sinh(x)')
    plt.grid(True)

    for i in x:
        plt.scatter(i, lagrange_polynomial(i, lst1, lst2), color='green')

    plt.show()


if __name__ == "__main__":
    x_values = [0.1, 0.5, 0.8, 1.3, 1.8, 2.6]
    y_values = [0.100167, 0.521095, 0.888106, 1.69838, 2.94217, 6.69473]
    x = [0.2, 1.4, 2.5]

    for i in x:
        print(
            f"P({i}) = {lagrange_polynomial(i, x_values, y_values)}\nSh({i}) = {Func(i)} \nε = {abs(lagrange_polynomial(i, x_values, y_values) - Func(i))}",
            end="\n\n")

    draw(x_values, y_values, x)
