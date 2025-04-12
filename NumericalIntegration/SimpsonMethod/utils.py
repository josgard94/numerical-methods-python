import numpy as np

def parse_function(func_str):
    """
    Returns a callable function from a string expression.
    WARNING: This uses eval and should be sanitized for production use.
    """
    def f(x):
        return eval(func_str, {"x": x, "np": np, "sin": np.sin, "cos": np.cos, "exp": np.exp, "log": np.log})
    return f
