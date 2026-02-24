Engineering Modeling Approach
1. System Description
The system consists of two rigid planar links:
Link AB rotates counterclockwise about a fixed pivot at A.
Link BC rotates clockwise about point B.
Angular velocities are constant.
Lumped masses are located at B and C.
Gravity and damping effects are neglected.
The objective is to compute the axial force in link AB over one full revolution.
2. Kinematic Modeling
Because angular velocities are constant, the motion is fully defined analytically.
Let:
L1 = length of AB
L2 = length of BC
w1 = angular velocity of AB
w2 = angular velocity of BC relative to B
The angular position of AB is:
The angular position of BC in the inertial frame is:
The position of B is obtained directly from circular motion:
y_B = L_1 \cos(\theta) 
Since angular velocity is constant, acceleration is purely centripetal:
The position of C is:
Acceleration of C is obtained as the sum of:
Acceleration of B
Relative centripetal acceleration of BC
Because angular velocities are constant, there are no tangential acceleration components.
3. Dynamic Force Calculation
The only forces considered are inertial forces resulting from acceleration:
\mathbf{F}_C = M_c \mathbf{a}_C 
The total force transmitted through link AB is:
To obtain the axial force in AB, the total force is projected onto the unit vector along AB:
Sign convention:
Positive → Tension
Negative → Compression
This projection isolates the internal force carried along the link’s axis.
4. Numerical Implementation
For each geometry–motion combination:
One full revolution of AB (0–360°) is simulated.
Positions, accelerations, and inertia forces are computed analytically.
Axial force is evaluated at 1000 discrete points.
Force is plotted against rotation angle.
All geometry and motion combinations are simulated independently to ensure full parametric coverage.
5. Engineering Insight
The simulations show that extreme axial forces occur for combinations with:
High angular velocities
Large distal mass Mc
Large secondary link length L2
This behavior follows directly from centripetal force scaling:
Since force increases with the square of angular velocity, rotational speed is the dominant driver of extreme loads.
The mass located farther from the pivot (at point C) contributes disproportionately to axial force in AB because its acceleration includes both the motion of AB and its own rotation about B.
Therefore:
Maximum tensile force occurs when both angular velocities and distal mass are high.
Maximum compressive force occurs when inertial force aligns opposite the AB direction during rotation.
Angular velocity is the primary parameter governing load magnitude due to its quadratic influence.
