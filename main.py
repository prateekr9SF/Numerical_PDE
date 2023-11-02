import numpy as np
from postProcess import *
from solver import *
import time

from scipy.sparse import diags
from scipy.sparse.linalg import cg


def solveFD2(nx, ny, dx, dy, f, size, u):
    # Solve Poisson equation using finite difference method
    for it in range(size):
        un = u.copy()
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                u[i, j] = (dx**2 * dy**2 * f[i, j] + dy**2 * (un[i - 1, j] + un[i + 1, j]) + dx**2 * (un[i, j - 1] + un[i, j + 1])) / (2 * (dx**2 + dy**2))
    return u


def solveFD2I(nx, ny, dx, dy, f, size, u):
    # Create the coefficient matrix for the linear system
    diagonals = [-2 / dx**2 - 2 / dy**2, 1 / dx**2, 1 / dx**2, 1 / dy**2, 1 / dy**2]
    offsets = [0, -1, 1, -ny, ny]
    A = diags(diagonals, offsets, shape=(ny*nx, ny*nx))
    
    # Flatten the source term and solution arrays
    f_flat = f.flatten()
    
    # Define a callback function that prints the residual at each iteration
    def callback(xk):
        r = A.dot(xk) - f_flat
        print("Residual: ", np.linalg.norm(r))



    # Solve the linear system using Conjugate Gradient solver
    u_flat, _ = cg(A, f_flat, x0=u.flatten(), callback=callback, maxiter = 1E6, tol = 1e-06)
    
    # Reshape the solution array back to its original shape
    u = u_flat.reshape((ny, nx))
    
    return u

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
size = 200000


# Initialize solution array
u = np.zeros((nx, ny))

# Define boundary conditions
u[0, :] = 0.0  # u = 0 at x = 0
u[-1, :] = 0.0  # u = 0 at x = 1
u[:, 0] = 0.0  # u = 0 at y = 0
u[:, -1] = 0.0  # u = 0 at y = 1

# Solve Poisson equation using second order finite difference method
u = solveFD2I(nx, ny, dx, dy, f, size, u)

plotsurf(u, X, Y)  
