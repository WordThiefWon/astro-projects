# gaussian.py --- "bell curve" with mean 0 and standard deviation 1
import matplotlib.pyplot as plt
import numpy as np
import math

''' Plot the Gaussian "bell curve" with mean 0 and standard deviation 1 over the range 
with 101 regularly spaced intervals.

Write code that does the following:
    1. define a function gaussian(x) that computes the Gaussian function. 
    (Hint: use the numpy module, which contains numpy.pi, numpy.sqrt, and numpy.exp)
    2. generate the x values X (using numpy.linspace())
    3. generate the y values Y (If you write your gaussian() 
    function with numpy functions then it should work as a "ufunc" 
    so you should be able to do Y = gaussian(X))
    4. plot with plt.plot(X, Y) (see plot()).
    5. add labels to the axes: "x" to the x-axis and "y" to the y-axis:
        plt.xlabel("x")
        plt.ylabel("y")
    6. save the figure in PNG format to file gaussian.png with
        plt.savefig("gaussian.png")
    In Develop Mode you will be able to see the image that you produced.
'''
def gaussian(x):
    gaussian = (1/np.sqrt(2*np.pi))*np.exp((-1/2)*(x**2))
    return gaussian

if __name__ == "__main__":
    X = np.linspace(-5, 5, 101)
    Y = gaussian(X)
    plt.plot(X, Y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('gaussian.png')