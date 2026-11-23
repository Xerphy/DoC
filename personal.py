import numpy as np
import matplotlib.pyplot as plt

def draw(func, x_min=-10, x_max=10, puntos=1000, nodos=None):
    x = np.linspace(x_min, x_max, puntos)
    y = func(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    if nodos is not None:
        ax.scatter(*nodos, color="black", zorder=3)
    ax.axhline(0, color="red", linewidth=0.8)
    ax.axvline(0, color="red", linewidth=0.8)
    ax.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    plt.show()