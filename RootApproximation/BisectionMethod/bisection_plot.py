import matplotlib.pyplot as plt
import numpy as np

class BisectionPlotter:
    def __init__(self, method_instance):
        self.method = method_instance

    def plot(self, num_points=1000):
        if self.method.root is None:
            raise RuntimeError("Error: Please run the method `.solve()` before plotting.")

        f = self.method.f
        a = self.method.a
        b = self.method.b
        root = self.method.root

        x_vals = np.linspace(a, b, num_points)
        y_vals = [f(x) for x in x_vals]

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label='f(x)', color='blue')
        plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
        plt.axvline(root, color='red', linestyle='--', label=f'Raíz ≈ {root:.6f}')
        plt.scatter([root], [f(root)], color='red', zorder=5)
        plt.title('Método de Bisección')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
