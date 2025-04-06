from newtonraphson_class import NewtonRaphsonMethod
from derivation_class import Derivation
if __name__ == "__main__":
    
    fh = Derivation("tanh(x) + pow(x,2) -1")
    
    newraphson = NewtonRaphsonMethod(fh.get_symbol(), fh.get_function(), fh.get_derivative(), x0=-2)
    result = newraphson.solve()

    if result == 0:
        print("No convergence")
    else:
        print("Converged")
        print("Root: ", newraphson.x1)
        print("Function value at root: ", fh.get_function().subs(fh.get_symbol(), newraphson.x1))
        print("Derivative value at root: ", fh.get_derivative().subs(fh.get_symbol(), newraphson.x1))
        print("Iterations: ", newraphson.iteration)