import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import pandas as pd
import os


G = 6.674e-11
dt = 0.02
time = 10
t = np.arange(0, time, dt)
max_mass = 10000000000000
min_mass = 100000000000
velocity = 10
distance = 20
#distance_far = 40 # The third body will be placed further away from the other two
view = 50
# If you want any specific initial conditions, enter them in the following file
initial_conditions_file = 'initial.txt'
title = 'Three Body Problem'


# Empty arrays for initial positions and velocities
pos = np.zeros((3, len(t), 2))
vel = np.zeros((3, len(t), 2))


path = os.path.dirname(os.path.realpath(__file__))
init_file = os.path.join(path, initial_conditions_file)


# Check if initial conditions file exists
if initial_conditions_file in os.listdir(path):

     print('Using initial conditions from file: ', initial_conditions_file)

     initial_conditions = pd.read_csv(init_file, header=0).values.tolist()

     pos[0, 0] = [initial_conditions[0][0], initial_conditions[0][1]]
     vel[0, 0] = [initial_conditions[0][2], initial_conditions[0][3]]
     m1 = initial_conditions[0][4]
     
     pos[1, 0] = [initial_conditions[1][0], initial_conditions[1][1]]
     vel[1, 0] = [initial_conditions[1][2], initial_conditions[1][3]]
     m2 = initial_conditions[1][4]
     
     pos[2, 0] = [initial_conditions[2][0], initial_conditions[2][1]]
     vel[2, 0] = [initial_conditions[2][2], initial_conditions[2][3]]
     m3 = initial_conditions[2][4]

else:

     print('Initial conditions were randomly set:')

     x1, y1 = np.random.uniform(-distance, distance), np.random.uniform(-distance, distance)
     vx1, vy1 = np.random.uniform(-velocity, velocity), np.random.uniform(-velocity, velocity)
     m1 = np.random.uniform(min_mass, max_mass)

     x2, y2 = np.random.uniform(-distance, distance), np.random.uniform(-distance, distance)
     vx2, vy2 = np.random.uniform(-velocity, velocity), np.random.uniform(-velocity, velocity)
     m2 = np.random.uniform(min_mass, max_mass)

     x3, y3 = np.random.uniform(-distance, distance), np.random.uniform(-distance, distance)
     vx3, vy3 = np.random.uniform(-velocity, velocity), np.random.uniform(-velocity, velocity)
     m3 = np.random.uniform(min_mass, max_mass)

     pos[0, 0] = [x1, y1]
     vel[0, 0] = [vx1, vy1]

     pos[1, 0] = [x2, y2]
     vel[1, 0] = [vx2, vy2]

     pos[2, 0] = [x3, y3]
     vel[2, 0] = [vx3, vy3]

     initial_conditions = [[x1,y1,vx1,vy1,m1],[x2,y2,vx2,vy2,m2],[x3,y3,vx3,vy3,m3]]

     df = pd.DataFrame(initial_conditions, columns=['x', 'y', 'vx', 'vy', 'm'])
     df.to_csv('initial_conditions.txt', header=True, index=False)

for condition in initial_conditions:
    print('x =', condition[0], ' y =', condition[1], ' vx =', condition[2], ' vy =', condition[3], ' m =', condition[4])


# Calculate positions and velocities over time
for i in range(1, len(t)):
    r1 = np.linalg.norm(pos[0, i-1] - pos[1, i-1])
    r2 = np.linalg.norm(pos[0, i-1] - pos[2, i-1])
    r3 = np.linalg.norm(pos[1, i-1] - pos[2, i-1])
    
    a1 = G * m2 / r1**2 * (pos[1, i-1] - pos[0, i-1]) / r1 + \
         G * m3 / r2**2 * (pos[2, i-1] - pos[0, i-1]) / r2
         
    a2 = G * m1 / r1**2 * (pos[0, i-1] - pos[1, i-1]) / r1 + \
         G * m3 / r3**2 * (pos[2, i-1] - pos[1, i-1]) / r3
         
    a3 = G * m1 / r2**2 * (pos[0, i-1] - pos[2, i-1]) / r2 + \
         G * m2 / r3**2 * (pos[1, i-1] - pos[2, i-1]) / r3
    
    vel[:, i] = vel[:, i-1] + np.array([a1, a2, a3]) * dt
    pos[:, i] = pos[:, i-1] + vel[:, i] * dt


fig, ax = plt.subplots()
ax.set_xlim((-view, view))
ax.set_ylim((-view, view))
ax.set_title(title)
plt.axis('off')

line1, = ax.plot([], [], 'r--', linewidth=0.5)
line2, = ax.plot([], [], 'b--', linewidth=0.5)
line3, = ax.plot([], [], 'g--', linewidth=0.5)
dot1, = ax.plot([], [], 'ro', markersize=5)
dot2, = ax.plot([], [], 'bo', markersize=5)
dot3, = ax.plot([], [], 'go', markersize=5)

def animate(i):
    line1.set_data(pos[0, :i, 0], pos[0, :i, 1])
    line2.set_data(pos[1, :i, 0], pos[1, :i, 1])
    line3.set_data(pos[2, :i, 0], pos[2, :i, 1])
    dot1.set_data(pos[0, i-1, 0], pos[0, i-1, 1])
    dot2.set_data(pos[1, i-1, 0], pos[1, i-1, 1])
    dot3.set_data(pos[2, i-1, 0], pos[2, i-1, 1])
    return line1, line2, line3, dot1, dot2, dot3

ani = FuncAnimation(fig, animate, frames=len(t), interval=50)

writer = PillowWriter(fps=20)
ani.save('three_body_problem.gif', writer=writer)
