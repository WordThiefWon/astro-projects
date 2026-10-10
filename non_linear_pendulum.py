import numpy as np
import matplotlib.pyplot as plt

# parameters
default_omega0 = 1

def integrate(theta0, dt=0.01, nmax=5, omega0=default_omega0):
    """Integrate the non-linear pendulum with Euler.
    Parameters
    ----------
    theta0 : float
         initial angular displacement (in radians)
    dt : float
         integrator time step
    nmax : float or int
         number of harmonic periods T0 = 2π/omega0
         for which the trajectory is sampled.
    omega0 : float
         angular frequency of the harmonic pendulum
    Returns
    -------
    array
          The array has shape (3, N) where N is the number
          of time steps and the three rows correspond to
          time, theta, Omega time series.
    Note
    ----
    The initial angular velocity is set to 0, i.e., the pendulum
    always starts from rest and the largest deflection is theta0.
    """
    omega2 = omega0**2
    T0 = 2*np.pi/omega0   # harmonic period
    Tmax = nmax * T0      # max sampling time

    theta = theta0
    Omega = 0
    t = 0
    data = [(t, theta, Omega)]
    
    while t <= Tmax:
        t += dt
        theta += Omega*dt
        Omega -= omega2*np.sin(theta)*dt
        data.append((t, theta, Omega))

    # return numpy array [t, theta, Omega]
    # of shape (3 x N) (see doc string)
    return np.transpose(data)

theta0 = 0.75*np.pi
data = integrate(theta0)
times, thetas, Omegas = data

# add output printing and plotting here
print("time range: {0:.3f} ... {1:.3f}".format(times.min(), times.max()))
print("theta range: {0:.3f} ... {1:.3f}".format(thetas.min(), thetas.max()))
print("Omega range: {0:.3f} ... {1:.3f}".format(Omegas.min(), Omegas.max()))

plt.matplotlib.style.use('ggplot')
fig, (axtheta, axW) = plt.subplots(2, 1, figsize=(5,5), sharex=True)
axtheta.plot(times, thetas, lw=3, color="#38BCE5")
axW.plot(times, Omegas, lw=3, color="#DD27F5")
axtheta.set_ylabel(r"angle $\theta$")
axW.set_ylabel(r"angular velocity $\Omega$")
axW.set_xlabel(r"time $t$")
axtheta.set_title(r"non-linear pendulum with $\theta_0=\frac{{3\pi}}{{4}}$")
fig.savefig("non_linear_pendulum.png")