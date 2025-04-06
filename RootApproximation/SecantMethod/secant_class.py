# secant.py

import pandas as pd

class SecantMethod:
    def __init__(self, function, x0: float, x1: float, tolerance: float = 1e-6, max_iterations: int = 100):
        self.function = function
        self.x0 = x0
        self.x1 = x1
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.iterations = []

    def solve(self):
        x0, x1 = self.x0, self.x1
        f = self.function.evaluate

        for i in range(self.max_iterations):
            f_x0 = f(x0)
            f_x1 = f(x1)

            if f_x1 - f_x0 == 0:
                print("División por cero en iteración", i)
                break

            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            error = abs(x2 - x1)

            self.iterations.append({
                "iteración": i + 1,
                "x0": x0,
                "x1": x1,
                "f(x0)": f_x0,
                "f(x1)": f_x1,
                "x2": x2,
                "error": error
            })

            if error < self.tolerance:
                break

            x0, x1 = x1, x2

        return x2

    def get_iterations_dataframe(self):
        return pd.DataFrame(self.iterations)
