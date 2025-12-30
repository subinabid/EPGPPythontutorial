"""Newton-Raphson method to find the root of a function.

This module implements the Newton-Raphson algorithm for finging
the square root of a number.

Explanation:
The Newton-Raphson method is an iterative numerical method used to find
the roots of a real-valued function. It starts with an initial guess and
refines that guess using the function and its derivative.

The formula used in the Newton-Raphson method is:
    x_{n+1} = x_n - f(x_n) / f'(x_n)
where:
- x_n is the current guess,
- f(x_n) is the value of the function at x_n,
- f'(x_n) is the value of the derivative at x_n.
"""

from sys import argv

TOLERANCE = 1e-7  # Convergence tolerance
MAX_ITERATIONS = 100  # Maximum number of iterations


def newton_raphson(func, dfunc, x0, tol=TOLERANCE, max_iter=MAX_ITERATIONS) -> float:
    """
    Find the root of a function using the Newton-Raphson method.

    Parameters:
    func : function
        The function for which we are trying to find a root.
    dfunc : function
        The derivative of the function.
    x0 : float
        Initial guess for the root.
    tol : float
        Tolerance for convergence.
    max_iter : int
        Maximum number of iterations.

    Returns:
    float
        Approximation of the root.
    """
    x = x0
    for i in range(max_iter):
        fx = func(x)
        dfx = dfunc(x)
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")
        x1 = x - fx / dfx
        if abs(x1 - x) < tol:
            return x1
        x = x1
    # If we reach here, we did not converge
    # Raise an exception
    raise ValueError("Maximum iterations reached. No solution found.")


# Example usage:
if __name__ == "__main__":
    _, n = argv

    n1 = float(n)

    # Define the function and its derivative
    def func(x, n=n1):
        return x**2 - n  # Example: f(x) = x^2 - n

    def dfunc(x):
        return 2 * x  # Derivative: f'(x) = 2x

    # Initial guess
    x0 = n1 / 2 if n1 != 0 else 1.0

    # Find the root
    root = newton_raphson(func, dfunc, x0)
    print(f"The root is approximately: {root}")
