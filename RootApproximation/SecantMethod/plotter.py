# plotter.py

import numpy as np
import matplotlib.pyplot as plt

def plot_function_and_iterations(function, iterations_df, x_range=(-10, 10)):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = function.evaluate(x)

    # Coordenadas de todas las aproximaciones
    x_approximations = iterations_df["x2"].values
    y_approximations = function.evaluate(x_approximations)

    # Última aproximación (raíz final)
    x_final = x_approximations[-1]
    y_final = y_approximations[-1]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='f(x)', color='green')
    plt.axhline(0, color='gray', linestyle='--')

    # Aproximaciones intermedias en rojo
    if len(x_approximations) > 1:
        plt.scatter(x_approximations[:-1], y_approximations[:-1], color='red', label='Aproximaciones')

    # Última aproximación en azul
    plt.scatter(x_final, y_final, color='blue', label='Raíz final', zorder=5)

    plt.title("Método de la Secante")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
