import numpy as np
from postProcess import *
from solver import *
import time

## COMPUTATIONAL DOMAIN DEFINITION
nx, ny = 100, 100  # number of points in x and y directions
dx = 1.0 / (nx - 1)  # grid spacing in the x direction
dy = 1.0 / (ny - 1)  # grid spacing in the y direction

# Create grid
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)

# Define source term
f = np.sin(np.pi * X) * np.sin(np.pi * Y)

# Define size
size = 100

# Initialize solution array
u = np.zeros((nx, ny))

# Define boundary conditions
u[0, :] = 0.0  # u = 0 at x = 0
u[-1, :] = 0.0  # u = 0 at x = 1
u[:, 0] = 0.0  # u = 0 at y = 0
u[:, -1] = 0.0  # u = 0 at y = 1


# Solve Poisson equation using second order finite difference method
start_time = time.time()  # Start timer
u = solveFD2_Poissons(nx, ny, dx, dy, f, size, u)
end_time = time.time()  # End timer

execution_time = end_time - start_time

print(f"Execution time: {execution_time} seconds")

# Plot results
plotPoissons(u, X, Y) 
