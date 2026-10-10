import numpy as np
import matplotlib.pyplot as plt
import math

''' The goal of this project is to simulate the trajectories of the Earth 
and the Moon during one year. 
'''

### Constants
AU = 149597870700 # 1 AU = 149,597,870,700 m
SY = 365.24219 # 1 Solar Year = 365.24219 d
G = 4*np.pi**2

mass = {
    'sun': 1.0,
    'earth': 3.0034e-6,
    'moon': 3.6923e-8
    }

r0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([9.978977040419635E-01, 6.586825681892025E-02, -6.320430920521123E-06]),
    'moon': np.array([9.956768547953816E-01, 6.676030485840675E-02, 1.641093070596718E-04])
    }
v0 = {
    'sun': np.array([0,0,0]),
    'earth': np.array([-4.70015711e-01, 6.25165839e+00, -3.40817831e-04]),
    'moon': np.array([-0.55065949, 6.03534661, 0.01111456])
    }

mS = mass['sun']
mE = mass['earth'] # mass of earth in solar masses
mM = mass['moon'] # mass of moon in solar masses
rS = r0['sun']
rE = r0['earth'] # earth position vector
rM = r0['moon'] # moon position vector
vE = v0['earth'] # earth velocity vector
vM = v0['moon'] # moon velocity vector

# Earth and Moon: Forces
def F_gravity(ri, rj, mi, mj):
    ''' This function calculates the force vector for the equation of motion of force on i at position
    ri due to j at position rj. It returns a numpy array that represents the force vector.
    '''
    rij = ri - rj # difference vector
    rij_sqr = np.dot(rij, rij) # the scalar length of the difference vector squared
    rij_hat = rij/np.sqrt(rij_sqr) # unit vector pointing from j towards i
    F_ij = ((-G*mi*mj)/rij_sqr)*rij_hat # the force on body i at ri due to body j at rj
    return F_ij

def F_ES(rE):
    ''' This function takes the current position of the earth rE (as a numpy array with three 
    elements) as an argument and calculates the force on the Earth due to the Sun. It returns
    a numpy array that represents the force vector.
    '''
    F_ES = F_gravity(rE, rS, mE, mS) # the force on earth at rE due to the Sun at rS
    return F_ES

# Earth's orbit
def integrate_earth(tmax, dt=1e-3):
    ''' This function returns the trajectory of Earth assuming the Earth only feels the 
    attraction from the Sun.
    '''
    t = 0
    rE = r0['earth']
    vE = v0['earth']
    data = [(rE)]
    while t <= tmax:
        t += dt
        rE = rE + vE*dt # first ODE
        vE = vE + (F_ES(rE)/mE)*dt # second ODE
        data.append(rE.copy())
    return np.array(data)

# Earth AND Moon
def F_EM(rE, rM):
    ''' This function calculates the force from the Moon on the Earth. rE is the position of
    Earth, rM is the position of the Moon.
    '''
    F_EM = F_gravity(rE, rM, mE, mM) # the force on earth at rE due to the Moon at rM
    return F_EM

def F_ME(rE, rM):
    ''' This function calculates the force from the Earth on the Moon.'''
    F_ME = -F_EM(rE, rM) # the force on the moon at rM due to the Earth at rE
    return F_ME

def F_MS(rM):
    ''' This function calculates the force from the Sun on the Moon.'''
    F_MS = F_gravity(rM, rS, mM, mS)
    return F_MS

def F_E(rE, rM):
    ''' This function returns the total force on the Earth from the Sun and Moon.'''
    F_E = F_ES(rE) + F_EM(rE, rM)
    return F_E

def F_M(rE, rM):
    ''' This function returns the total force on the Moon from the Sun and Earth.'''
    F_M = F_MS(rM) + F_ME(rE, rM)
    return F_M

def integrate_EM(tmax, dt=1e-3):
    ''' This function integrates the equations of motion of Earth and Moon. It will return a tuple
    with the Earth and Moon trajectories.
    '''
    t = 0
    rE = r0['earth']
    rM = r0['moon']
    vE = v0['earth']
    vM = v0['moon']
    data_E = [(rE)]
    data_M = [(rM)]
    while t <= tmax:
        t += dt
        rE = rE + vE*dt
        rM = rM + vM*dt
        vE = vE + (F_E(rE, rM)/mE)*dt
        vM = vM + (F_M(rE, rM)/mM)*dt
        data_E.append(rE.copy())
        data_M.append(rM.copy())
    return (np.array(data_E), np.array(data_M))

if __name__ == "__main__":

    earth_integrated = integrate_earth(1)
    earth_moon = integrate_EM(1)
    earth, moon = earth_moon

    ### Earth only plot
    plt.figure() # starts us off with a fresh new plot
    plt.plot(earth_integrated[:, 0:1], earth_integrated[:, 1:2], "r", label="Earth")
    plt.xlabel('x (AU)')
    plt.ylabel('y (AU)')
    plt.gca().set_aspect("equal")
    plt.plot(r0["earth"][0], r0["earth"][1], "r^")
    plt.legend()
    filename = "orbit_earth_only.png"
    plt.savefig(filename)

    ### Earth and Moon plot
    plt.figure() # remember to start with a fresh plot here
    plt.plot(earth[:, 0:1], earth[:, 1:2], color="#27DDF5", linestyle="solid", label="Earth")
    plt.plot(moon[:, 0:1], moon[:, 1:2], color="#DD27F5", linestyle="--", label="Moon")
    plt.xlabel('x (AU)')
    plt.ylabel('y (AU)')
    plt.gca().set_aspect("equal")
    plt.plot(r0["earth"][0], r0["earth"][1], "r^")
    plt.legend()
    filename = "orbit_earth_moon.png"
    plt.savefig(filename)

    # NASA Horizons Earth trajectory
    def read_data(datafile):
        positions = []
        with open(datafile) as file:
            begin_append = False
            for line in file:
                line = line.strip()
                if line.startswith("$$EOE"):
                    break
                if begin_append == True:
                    values = line.split(',')
                    positions.append(values[2:5])
                if line.startswith("$$SOE"):
                    begin_append = True
                    continue
        positions = np.array(positions, dtype=np.float64)
        return positions

    datafile = "EARTH_horizons_results.txt"            
    positions = read_data(datafile)
    X, Y, Z = positions.T

    plt.figure()
    plt.plot(X, Y, color="#DD27F5", linestyle="solid", label="NASA")
    plt.plot(earth[:, 0:1], earth[:, 1:2], color="#27DDF5", linestyle="--", label="Euler")
    plt.xlabel('x (AU)')
    plt.ylabel('y (AU)')
    plt.gca().set_aspect("equal")
    plt.legend()
    filename = "NASA_Euler_comparison.png"
    plt.savefig(filename)