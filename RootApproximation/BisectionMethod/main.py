from cmath import sqrt
from bisection_class import BisectionMethod
from bisection_plot import BisectionPlotter

if __name__ == "__main__":
    import math

    # define your function here
    # Example: f(x) = x^2 - 12
    def f(x):
        return math.tanh(x) + pow(x,2) -1

    #pass the function and the interval [a, b] here
    # Example: interval [3, 4]
    biseccion = BisectionMethod(function=f, a=0, b=2)
    biseccion.solve()
    
    plotter = BisectionPlotter(biseccion)
    plotter.plot()