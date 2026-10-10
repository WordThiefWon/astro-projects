# parametrized_gaussian.py --- family of Gaussian curves with different mu and sigma
import matplotlib.pyplot as plt 
import numpy as np 
import math

''' Plot the Gaussian "bell curve" with mean mu and standard deviation sigma over the range -5 <= x <= 5
with 101 regularly spaced intervals and for the following parameters:
    mu = 0, sigma = 4
    mu = 0, sigma = 2
    mu = 0, sigma = 1
    mu = 0, sigma = 1/2
    mu = 1, sigma = 1

Write code that does the following:
    1. define a function gaussian(x, mu=0, sigma=1) that computes the Gaussian function 
        and takes mean and standard deviation as optional parameters.
    2. generate the x values X

    Then for each of the required parameters mu and sigma do the following to plot the corresponding graph:
    3. generate the y values Y
    4. plot with plt.plot(X, Y, label="mu={mu} sigma={sigma}".format(mu=mu, sigma=sigma)) 
        and add a label to the graph that indicates the given parameters mu and sigma (see plot()).

    Then finalize the plot by adding labels:
    5. add labels to the axes: "x" to the x-axis and "y" to the y-axis
    6. add a legend with
    plt.legend(loc="best")
    7. add a title with
    plt.title("Gaussians")
    8. save the figure in PNG format with
    plt.savefig("parametrized_gaussian.png")
'''

def gaussian(x, mu=0, sigma=1):
    gaussian = (1/np.sqrt(2*np.pi*(sigma**2)))*np.exp(-(((x - mu)**2))/(2*(sigma**2)))
    return gaussian

if __name__ == "__main__":
    parameters = [[0, 4], [0, 2], [0, 1], [0, 0.5], [1, 1]] # [mu, sigma]

    X = np.linspace(-5, 5, 101)

    for mu, sigma in parameters:
        Y = gaussian(X, mu, sigma)
        plt.plot(X, Y, label="mu={mu} sigma={sigma}".format(mu=mu, sigma=sigma))
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc="best")
    plt.title("Gaussians")
    plt.savefig("parametrized_gaussian.png")