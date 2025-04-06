import math as m
import sympy as sp
class NewtonRaphsonMethod:
    def __init__(self, symbol, func, derivative, tolerance=1e-6, max_iterations=100, error=0.1, x1=0, x0 = 0):
        self.func_eval = sp.lambdify(symbol, func, 'numpy')
        self.derivative_eval = sp.lambdify(symbol, derivative, 'numpy')
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.error = error
        self.x1 = x1
        self.x0 = x0
        self.iteration = 1

    def solve(self):
        while True:
            if self.iteration > self.max_iterations:
                return 0
            f_xn = self.func_eval(self.x0)
            f_prime_xn = self.derivative_eval(self.x0)

            if f_prime_xn == 0:
                raise ZeroDivisionError("Derivative is zero. No solution found.")
            
            self.x1 = self.x0 - (f_xn / f_prime_xn)
            self.error = abs(self.x1 - self.x0)

            if self.error <= self.tolerance:
                return 1
            else: 
                self.x0 = self.x1
                self.iteration += 1