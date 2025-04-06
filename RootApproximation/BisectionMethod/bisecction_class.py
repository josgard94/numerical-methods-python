class BisectionMethod:
    def __init__(self, function, a, b, tolerance=1e-6, max_iterations=100):
        self.f = function
        self.a = a
        self.b = b
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.iterations = 0
        self.root = None

    def is_valid_interval(self):
        return self.f(self.a) * self.f(self.b) < 0

    def solve(self):
        if not self.is_valid_interval():
            raise ValueError("El intervalo [a, b] no contiene un cambio de signo.")

        a, b = self.a, self.b
        for i in range(self.max_iterations):
            c = (a + b) / 2
            self.iterations += 1

            if abs(self.f(c)) < self.tolerance or abs(b - a) / 2 < self.tolerance:
                self.root = c
                return c
            
            if self.f(a) * self.f(c) < 0:
                b = c
            else:
                a = c

        self.root = (a + b) / 2
        return self.root

    def summary(self):
        return {
            "root": self.root,
            "iterations": self.iterations,
            "tolerance": self.tolerance
        }