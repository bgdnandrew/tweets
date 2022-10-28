import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

# Newton's Method for finding roots with a max number of iterations
# using scipy's derivative
def newton_raphson_1(f, x0, max_iter):
    x = x0
    approx_list = [x0]
    print('x:', x)
    for i in range(max_iter):
        x_new = x - f(x)/derivative(f, x, dx=1e-6)
        approx_list.append(x_new)
        x = x_new
        print("Approx. number ", i+1, " is ", x)
    return approx_list

# Newton's Method for finding roots with a max number of iterations
# using the hard-coded derivative
def newton_raphson_2(f, f_prime, x0, max_iter):
    x = x0
    approx_list = [x0]
    print('x:', x)
    for i in range(max_iter):
        x_new = x - f(x)/f_prime(x)
        approx_list.append(x_new)
        x = x_new
        print("Approx. number ", i+1, " is ", x)
    return approx_list


# Newton's Method for finding roots with a max numbe rof itertaions
# using scipy's derivative
def newton_method_visual(f, x0, max_iter):
    # setting up the graph
    plt.title("Newton's Method")
    plt.grid()
    plt.axhline(y=0)
    plt.axvline(x=0)

    # plotting the original function
    x = np.linspace(-1, 1, 100)
    y = f(x)
    plt.plot(x, y, color="r")

    # plotting our initial guess (x0) and its image
    plt.scatter(x0, 0, color="g")
    plt.pause(1)
    plt.scatter(x0, f(x0), color="b")

    x = x0
    approx_list = [x0]

    for i in range(max_iter):
        # graphing the tangent line to the function's graph in the point (x, f(x)), where for the 1st step x = x0
        x_tg  = np.linspace(-1, 1, 100)
        y_tg = derivative(f, x, dx=1e-6)*x_tg + (f(x) - derivative(f, x, dx=1e-6)*x) # y = mx + n
        plt.pause(2)
        plt.plot(x_tg, y_tg, color="g", linestyle="--")

        # calculating the next approximation (Newton's Method)
        x_new = x - f(x) / derivative(f, x)
        plt.pause(1)

        # graphing the next approximation
        plt.scatter(x_new, 0, color="g")
        plt.pause(1)

        # graphing the next approximation's image
        plt.scatter(x_new, f(x_new), color="b")
        plt.pause(1)

        approx_list.append(x_new)
        x = x_new

    plt.show()
    return x

# Newton's Method for finding roots with a max numbervof iterations
# using the hard-coded derivative
def newton_method_visual_2(f, x0, max_iter):
    # setting up the graph
    plt.title("Newton's Method")
    plt.grid()
    plt.axhline(y=0)
    plt.axvline(x=0)

    plt.pause(10)

    # plotting the original function
    x = np.linspace(-1, 1, 100)
    y = f(x)
    plt.plot(x, y, color="r", label="x + e^(-x^2)*cos(x)")

    # plotting our initial guess (x0) and its image
    plt.scatter(x0, 0, color="g")
    plt.pause(1)
    plt.scatter(x0, f(x0), color="b")

    x = x0
    approx_list = [x0]

    # show legend labels only once, based on color
    for legend_item in ["approximations"]:
        plt.scatter([], [], color="g", label=legend_item)
    # show legend labels only once, based on color
    for legend_item in ["image of approximations"]:
        plt.scatter([], [], color="b", label=legend_item)
    # show legend labels only once, based on color
    for legend_item in ["tangents to the function graph in (x_approx, f(x_approx))"]:
        plt.plot([], [], color="g", linestyle="--", label=legend_item)

    plt.legend(loc="upper left")

    for i in range(max_iter):
        # graphing the tangent line to the function's graph in the point (x, f(x)), where for the 1st step x = x0
        x_tg  = np.linspace(-1, 1, 100)
        y_tg = f_prime(x)*x_tg + (f(x) - f_prime(x)*x) # y = mx + n
        plt.pause(2)
        plt.plot(x_tg, y_tg, color="g", linestyle="--")

        # calculating the next approximation (Newton's Method)
        x_new = x - f(x) / f_prime(x)
        plt.pause(1)

        # graphing the next approximation
        plt.scatter(x_new, 0, color="g")
        plt.pause(1)

        # graphing the next approximation's image
        plt.scatter(x_new, f(x_new), color="b")
        plt.pause(1)

        approx_list.append(x_new)
        x = x_new

    plt.show()
    return x


# Newton's Method for finding roots with a max numbervof iterations
# using the hard-coded derivative
def newton_method_visual_3(f):
    x = np.linspace(-1, 1, 100)
    y = f(x)

    plt.title("Graph of converging approximations")
    plt.grid()
    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.xlim(-1, 1)
    plt.plot(x, y, color="r", label="x + e^(-x^2)*cos(x)")

    # show legend labels only once, based on color
    for legend_item in ["approximation"]:
        plt.scatter([], [], color="g", label=legend_item)

    plt.legend(loc="upper left")

    for approx in newton_raphson_2(f, f_prime, 0, 10):
        plt.scatter(approx, 0, color="g")

    plt.savefig("newton_method_converging_approximations.png")
    plt.show()




# ---
def f(x):
    return x + np.exp(-x**2)*np.cos(x)

def f_prime(x):
    #return the derivative of f(x)
    return (np.exp(x**2)-2*x*np.cos(x)-np.sin(x)) / np.exp(x**2)

# ---
newton_method_visual_2(f, 0, 10)
# newton_method_visual_3(f)
