import os
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime


def simulate():
    h = 0.01            # time step
    h_min = 1e-8        # minimum step size
    tol_max = 1e-2      # max tolerance
    tol_min = 1e-3      # minimum tolerance

    points = [[] for _ in range(3)]
    distance = [[] for _ in range(2)]

    p = np.array([      # populate with inital positions
        0.325514,
        -0.459460,
        0.166229
    ])

    v = np.array([      # populate with inital velocities
        -9.096111,
        -6.916686,
        -1.305721
    ])

    time = 0

    def accel(p):
        return (-4*pow(np.pi, 2))*(p/(np.dot(p, p)**1.5))

    min_ = float("inf")
    min_time = 0

    while time + h <= 200 + 1e-1:

        k1v = accel(p)
        k1p = v
        k2v = accel(p + k1p*(h/2))  
        k2p = v + k1v * (h/2)
        k3v = accel(p + k2p*(h/2))
        k3p = v + k2v * (h/2)
        k4v = accel(p + k3p*h)
        k4p = v + k3v * h

        v1 = v + (h/6) * (k1v + 2*k2v + 2*k3v + k4v)
        p1 = p + (h/6) * (k1p + 2*k2p + 2*k3p + k4p)

        k2v = accel(p + k1p*(h/4))  
        k2p = v + k1v * (h/4)
        k3v = accel(p + k2p*(h/4))
        k3p = v + k2v * (h/4)
        k4v = accel(p + k3p*(h/2))
        k4p = v + k3v * (h/2)

        v2 = v + (h/12) * (k1v + 2*k2v + 2*k3v + k4v)
        p2 = p + (h/12) * (k1p + 2*k2p + 2*k3p + k4p)

        p_le = abs(np.amax(p2 - p1))

        if p_le > tol_max:
            # large error
            # halve step size until acceptable error
            if h/2 < h_min:
                h = h_min
            else:
                h = h/2
            continue
        elif p_le < tol_min:
            # small error
            time += h
            v = v1
            p = p1
            h = h*2
        else:
            # acceptable error
            time += h
            v = v1
            p = p1

        for i in range(3):
            points[i].append(p[i])

        d = np.dot(p, p)**0.5

        distance[0].append(time)
        distance[1].append(d)

        if d < min_ and 50 < time < 100:
            # find value of next perihelion
            min_ = d
            min_time = time
    
    print(
"""
Next Perihelion (years from 02/09/1986): {}
""".format(min_time)
    )

    current_path = os.path.abspath('plots')


    fig = plt.figure()
    xyz = fig.add_subplot(111, projection='3d')
    xyz.plot(*points)
    xyz.set_xlabel('$x$-axis')
    xyz.set_ylabel('$y$-axis')
    xyz.set_zlabel('$z$-axis')
    plt.draw()
    plt.savefig(os.path.join(current_path, '3d-orbit.png'))
    plt.show()

    plt.clf()
    plt.scatter(*distance, s = 0.05)
    plt.title('Euclidean distance from Sun ($r$) vs time ($t$)')
    plt.xlabel('$t$ (years since 1986)')
    plt.ylabel('$r$ (distance in AU)')
    plt.grid()
    plt.draw()
    plt.savefig(os.path.join(current_path, 'r-t-scatter.png'))

    plt.clf()
    plt.plot(*distance)
    plt.title('Euclidean distance from Sun ($r$) vs time ($t$)')
    plt.xlabel('$t$ (years since 1986)')
    plt.ylabel('$r$ (distance in AU)')
    plt.grid()
    plt.draw()
    plt.savefig(os.path.join(current_path, 'r-t.png'))

if __name__ == "__main__":
    if not os.path.exists('plots'):
        os.makedirs('plots')

    simulate()
