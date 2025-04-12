import numpy as np

class SimpsonIntegrator:
    def __init__(self, function, a, b, n):
        if n % 2 != 0:
            raise ValueError("The number of subintervals (n) must be even.")
        self.function = function
        self.a = a
        self.b = b
        self.n = n
        self.h = (b - a) / n

    def integrate(self):
        x_values = np.linspace(self.a, self.b, self.n + 1)
        y_values = self.function(x_values)

        odd_sum = np.sum(y_values[1:-1:2])
        even_sum = np.sum(y_values[2:-1:2])

        result = (self.h / 3) * (y_values[0] + 4 * odd_sum + 2 * even_sum + y_values[-1])
        return result, x_values, y_values
