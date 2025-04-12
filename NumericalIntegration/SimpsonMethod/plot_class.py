# plotter.py

import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def __init__(self, function):
        self.function = function

    def plot(self, x_points, y_points, a, b, integral_value, title="Simpson's Rule Visualization"):
        x_dense = np.linspace(a, b, 1000)
        y_dense = self.function(x_dense)

        plt.figure(figsize=(10, 5))
        plt.plot(x_dense, y_dense, label="Original Function", color='blue')
        plt.plot(x_points, y_points, 'ro--', label="Simpson Points")
        plt.fill_between(x_dense, y_dense, alpha=0.1)

        # Show integral value as annotation
        plt.annotate(f"∫ ≈ {integral_value:.6f}",
                     xy=(0.7 * (a + b), max(y_points) * 0.8),
                     fontsize=12, color='darkgreen',
                     bbox=dict(boxstyle="round,pad=0.3", edgecolor='green', facecolor='lightyellow'))

        # Update title to include value too
        plt.title(f"{title}\nApprox. Integral: {integral_value:.6f}")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()
