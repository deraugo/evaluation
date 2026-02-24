# main.py

import matplotlib.pyplot as plt
from simulation import simulate_case
from config import geometry_sets, motion_sets


def run_all():
    case_number = 1

    for i, geom in enumerate(geometry_sets):
        for j, motion in enumerate(motion_sets):

            theta_deg, Faxial = simulate_case(geom, motion)

            print(f"Case {case_number}")
            print("Max tension:", Faxial.max())
            print("Max compression:", Faxial.min())
            print("---------------------")

            plt.figure()
            plt.plot(theta_deg, Faxial)
            plt.xlabel("Rotation Angle of AB (deg)")
            plt.ylabel("Axial Force in AB")
            plt.title(f"Geometry {i+1} - Motion {j+1}")
            plt.grid(True)

            plt.savefig(f"case_{case_number}.png")
            case_number += 1

    plt.show()


if __name__ == "__main__":
    run_all()
