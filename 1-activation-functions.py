# Activation functions

import matplotlib.pyplot as plt
import numpy as np

# plt.style.use('ggplot')

# def step(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

def step_2(x):
    return 1 * (x > 0)

def linear(x):
    return x

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def rectified_linear(x):
    return np.maximum(0, x)

# graph step function and save the graph as eps
def graph_step():
    x = np.array([-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    y = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0])

    plt.title("The Step Activation Function")
    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.xlim(-5.0, 5.0) # x-axis range
    plt.ylim(-3.0, 3.0) # y-axis range
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid()

    plt.step(x, y, color='red', where='pre', label="y = 1 if x > 0 else 0")

    plt.legend(loc='upper left')
    
    plt.savefig("step.eps")
    plt.savefig("step.png")
    
    plt.show()

# graph linear function and save the graph as eps
def graph_linear():
    x = np.linspace(-5.0, 5.0, 100)
    y = linear(x)

    plt.title("The Linear Activation Function")
    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.xlim(-5.0, 5.0) # x-axis range
    plt.ylim(-5.0, 5.0) # y-axis range
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid()

    plt.plot(x, y, color="red", label="y = x")

    plt.legend(loc='upper left')

    plt.savefig("linear.eps")
    plt.savefig("linear.png")

    plt.show()

# graph sigmoid function and save the graph as eps
def graph_sigmoid():
    x = np.linspace(-5.0, 5.0, 100)
    y = sigmoid(x)

    plt.title("The Sigmoid Activation Function")
    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.xlim(-5.0, 5.0) # x-axis range
    plt.ylim(-5.0, 5.0) # y-axis range
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid()

    plt.plot(x, y, color="red", label="y = 1 / (1 + e^-x)")

    plt.legend(loc='upper left')

    plt.savefig("sigmoid.eps")
    plt.savefig("sigmoid.png")

    plt.show()

# graph rectified linear function and save the graph as eps and png
def graph_rectified_linear():
    x = np.linspace(-5.0, 5.0, 100)
    y = rectified_linear(x)

    plt.title("The Rectified Linear Activation Function")
    plt.axhline(y=0)
    plt.axvline(x=0)
    plt.xlim(-5.0, 5.0) # x-axis range
    plt.ylim(-5.0, 5.0) # y-axis range
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.grid()

    plt.plot(x, y, color="red", label="y = max(0, x)")

    plt.legend(loc='upper left')

    plt.savefig("rectified_linear.eps")
    plt.savefig("rectified_linear.png")

    plt.show()

graph_step()
graph_linear()
graph_sigmoid()
graph_rectified_linear()
