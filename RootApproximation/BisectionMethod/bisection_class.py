from tabulate import tabulate

class BisectionMethod:
    def __init__(self, function, a, b, tolerance=1e-6, max_iterations=100):
        self.f = function
        self.a = a
        self.b = b
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.iterations = 0
        self.root = None
        self.table_data = []

    def is_valid_interval(self):
        return self.f(self.a) * self.f(self.b) < 0

    def solve(self):

        if not self.is_valid_interval():
            raise ValueError("The interval [a, b] does not contain a sign change.")

        a, b = self.a, self.b

        for _ in range(self.max_iterations):
            c = (a + b) / 2
            fa = self.f(a)
            fb = self.f(b)
            fc = self.f(c)
            interval_size = b - a

            update = "a = c" if fa * fc < 0 else "b = c"

            self.table_data.append([
                round(a, 6), round(b, 6),
                round(fa, 6), round(fb, 6),
                round(c, 6), round(fc, 6),
                update,
                round(interval_size, 6)
            ])

            self.iterations += 1

            if abs(fc) < self.tolerance or interval_size / 2 < self.tolerance:
                self.root = c
                self.print_table()
                return c

            if fa * fc < 0:
                b = c
            else:
                a = c

        self.root = (a + b) / 2
        self.print_table()
        return self.root
    
    def print_table(self):
        headers = ["a", "b", "f(a)", "f(b)", "c = (a + b)/2", "f(c)", "Update", "new b − a"]
        print("\nBisection Method Iteration Table:\n")
        print(tabulate(self.table_data, headers=headers, tablefmt="grid"))
    def summary(self):
        return {
            "root": self.root,
            "iterations": self.iterations,
            "tolerance": self.tolerance
        }