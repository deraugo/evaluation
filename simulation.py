# simulation.py

import numpy as np


def simulate_case(geom, motion, n_points=1000):
    L1 = geom["L1"]
    L2 = geom["L2"]
    Mb = geom["Mb"]
    Mc = geom["Mc"]

    omega1 = motion["omega1"]
    omega2 = -abs(motion["omega2"])  # clockwise

    # Time for one full rotation of AB
    T = 2 * np.pi / omega1
    t = np.linspace(0, T, n_points)

    theta = omega1 * t
    phi = theta + omega2 * t

    # Position of B
    xB = L1 * np.sin(theta)
    yB = L1 * np.cos(theta)

    # Acceleration of B
    aBx = -omega1**2 * xB
    aBy = -omega1**2 * yB

    # Position of C
    xC = xB + L2 * np.sin(phi)
    yC = yB + L2 * np.cos(phi)

    # Relative acceleration of BC
    relAx = -omega2**2 * L2 * np.sin(phi)
    relAy = -omega2**2 * L2 * np.cos(phi)

    # Acceleration of C
    aCx = aBx + relAx
    aCy = aBy + relAy

    # Inertia forces
    FBx = Mb * aBx
    FBy = Mb * aBy

    FCx = Mc * aCx
    FCy = Mc * aCy

    # Total force transmitted through AB
    Ftotx = FBx + FCx
    Ftoty = FBy + FCy

    # Unit vector along AB
    magAB = np.sqrt(xB**2 + yB**2)
    ux = xB / magAB
    uy = yB / magAB

    # Axial force projection
    Faxial = Ftotx * ux + Ftoty * uy

    theta_deg = np.degrees(theta)

    return theta_deg, Faxial
