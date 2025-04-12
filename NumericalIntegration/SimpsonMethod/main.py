from simpson_class import SimpsonIntegrator
from plot_class import Plotter
from utils import parse_function

def main():
    # Parameters
    function_str = "2 * pow(x,3) - 4 * x + 1"     # You can change to "np.sin(x)", "np.exp(-x**2)", etc.
    a = 2
    b = 4
    n = 8                 # Must be even

    function = parse_function(function_str)

    # Integration
    integrator = SimpsonIntegrator(function, a, b, n)
    result, x_vals, y_vals = integrator.integrate()

    print(f"Approximate integral value: {result:.6f}")

    # Plotting
    plotter = Plotter(function)
    plotter.plot(x_vals, y_vals, a, b, result, title=f"Simpson's Rule for {function_str} on [{a}, {b}] with n={n}")

if __name__ == "__main__":
    main()
