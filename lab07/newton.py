import argparse
import sympy as sp

def newton_method(func, func_derivative, initial_value, accuracy=1e-6, max_iterations=100):
    x = initial_value
    iteration = 0
    while abs(func(x)) > accuracy and iteration < max_iterations:
        x = x - func(x) / func_derivative(x)
        iteration += 1
    if iteration == max_iterations:
        print("Maximum iterations reached. No convergence.")
    return x

def main():
    parser = argparse.ArgumentParser(description="Newton method for finding roots of a function.")
    parser.add_argument("function", help="The function in terms of 'x'.")
    parser.add_argument("initial_guess", type=float, help="Initial guess for the root.")
    parser.add_argument("--accuracy", type=float, default=1e-6, help="Desired accuracy. (default: 1e-6)")
    parser.add_argument("--max_iterations", type=int, default=100, help="Maximal number of method iterations. (default: 100)")
    args = parser.parse_args()

    x = sp.symbols('x')
    func = sp.sympify(args.function)
    func_derivative = sp.diff(func, x)

    root = newton_method(sp.lambdify(x, func), sp.lambdify(x, func_derivative), args.initial_guess, args.accuracy, args.max_iterations)

    print("Approximate root:", root)

if __name__ == "__main__":
    main()
