from cmath import sqrt
from bisecction_class import BisectionMethod

if __name__ == "__main__":
    import math

    # define your function here
    # Example: f(x) = x^2 - 12
    def f(x):
        return pow(x,2) -12

    #pass the function and the interval [a, b] here
    # Example: interval [3, 4]
    biseccion = BisectionMethod(function=f, a=3, b=4)
    biseccion.solve()
    
