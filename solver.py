import numpy as np
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
    offsets = [0, -1, 1, -nx, nx]
    A = diags(diagonals, offsets, shape=(nx*ny, nx*ny))
    
    # Flatten the source term and solution arrays
    f_flat = f[1:-1, 1:-1].flatten()
    u_flat = u[1:-1, 1:-1].flatten()
    
    # Solve the linear system using Conjugate Gradient solver
    u_flat, _ = cg(A, f_flat)
    
    # Reshape the solution array back to its original shape
    u[1:-1, 1:-1] = u_flat.reshape((nx-2, ny-2))
    
    return u