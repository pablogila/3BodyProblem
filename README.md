# 3BodyProblem

3BodyProblem is a Python program that simulates the motion of three celestial bodies in a two-dimensional space using numerical integration of Newton's equations of motion. The program can be used to generate animations of the motion of three bodies under the influence of their mutual gravitational attraction.
Requirements

Three Body Problem runs in Python 3.X with the following libraries installed: numpy, matplotlib and pandas. The use of a virtual environment such as venv is recommended, but not required.

## Usage

First download the source code from GitHub.  
* From your web browser:  
On GitHub, click on 'Code', 'Download ZIP', and extract.
*Using git:  
`git clone https://github.com/pablogila/3BodyProblem.git`

After downloading the source code, navigate to the directory containing the code in your terminal or command prompt.

The program can be executed by running the Three_Body_Problem.py file:

`python3 3-body.py`

By default, the program generates an animation of the motion of three celestial bodies with randomly generated initial positions, velocities and masses.

The initial positions, velocities, masses and other parameters of the simulation can be modified by editing the initial.txt file in the same directory as the Python code. The format of the initial.txt file should be as follows:

x1,y1,vx1,vy1,m1  
x2,y2,vx2,vy2,m2  
x3,y3,vx3,vy3,m3  

Where x and y are the initial positions of each celestial body, vx and vy are the initial velocities, and m is the mass.

To generate an animation of the motion of the three celestial bodies with the modified initial conditions, run the program again.

The program will generate an animation of the motion of the three celestial bodies and save it as a GIF file called three_body_problem.gif in the same directory as the Python code.
Parameters

The following parameters can be modified in the Three_Body_Problem.py file:

* G: gravitational constant
* dt: time step of the simulation
* time: total time of the simulation
* max_mass: maximum mass of the celestial bodies
* min_mass: minimum mass of the celestial bodies
* velocity: maximum initial velocity of the celestial bodies
* distance: maximum initial distance of the celestial bodies from the origin
* view: size of the viewing window
* initial_conditions_file: the name of the file containing the initial conditions of the simulation
* title: the title of the animation

Output

The program generates an animation of the motion of the three celestial bodies and saves it as a GIF file called three_body.gif in the same directory as the Python code.