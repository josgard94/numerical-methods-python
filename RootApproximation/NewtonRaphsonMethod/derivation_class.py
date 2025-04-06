import sympy as sp

class Derivation:
    def __init__(self, func_str):
        self.x = sp.symbols('x')
        self.func = sp.sympify(func_str)
        self.derivative = sp.diff(self.func, self.x)

    def get_function(self):
        return self.func

    def get_derivative(self):
        return self.derivative

    def get_symbol(self):
        return self.x