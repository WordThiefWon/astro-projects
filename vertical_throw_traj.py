import matplotlib.pyplot as plt
import numpy as np
import math

# constants
g = 9.81

# functions
def y_throw(t, v0, y0=2):
    u_t = (-1/2)*g*(t**2) + v0*t + y0
    y_t = u_t*(np.heaviside(u_t, 0))
    return y_t

# main
if __name__ == "__main__":
    # plotting 
    y_values_0 = []
    y_values_20 = []
    t_range = np.linspace(0, 5, 100)
    
    for t in t_range:
        y_t_0 = y_throw(t, 0)
        y_t_20 = y_throw(t, 20)
        y_values_0.append(y_t_0)
        y_values_20.append(y_t_20)

    plt.plot(t_range, y_values_20, label=r"$v_0={v0}\,\mathrm{{m}}\cdot\mathrm{{s}}^{{-1}}$".format(v0=20), linewidth=4, linestyle='solid')
    plt.plot(t_range, y_values_0, label=r"$v_0={v0}\,\mathrm{{m}}\cdot\mathrm{{s}}^{{-1}}$".format(v0=0), linewidth=2, linestyle='dashed')
    plt.xlabel('time (s)')
    plt.ylabel('position (m)')
    plt.title('vertical throw')
    plt.legend()
    plt.savefig("throw.png")