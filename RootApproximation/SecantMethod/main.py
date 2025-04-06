# main.py

from function_class import Function
from secant_class import SecantMethod
from plotter import plot_function_and_iterations
import numpy as np
if __name__ == "__main__":
    # Definir la función f(x) = x^3 - x - 2
    f = Function(lambda x: np.tan(0.1*x) -9.2 * np.exp(-x))
    # Definir los puntos iniciales x0 y x1
    secant = SecantMethod(f, x0=3.2, x1=3.7)

    root = secant.solve()
    df = secant.get_iterations_dataframe()

    print("\nRaíz aproximada:", root)
    print("\nTabla de iteraciones:")
    print(df)

    plot_function_and_iterations(f, df, x_range=(2, 3.5))
