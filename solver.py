import numpy as np
from multiprocessing import Pool

def solveFD2_Poissons(nx, ny, dx, dy, f, size, u):
    """
    Solve the Poisson equation using the finite difference method.
    
    Parameters
    ----------
    nx : int
        The number of grid points in the x-direction.
    ny : int
        The number of grid points in the y-direction.
    dx : float
        The grid spacing in the x-direction.
    dy : float
        The grid spacing in the y-direction.
    f : ndarray
        The source term of the Poisson equation.
    size : int
        The number of iterations to perform.
    u : ndarray
        The initial guess for the solution.

    Returns
    -------
    u : ndarray
        The numerical solution to the Poisson equation.
    """

    # Solve Poisson equation using finite difference method
    for it in range(size):
        un = u.copy()
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                u[i, j] = (dx**2 * dy**2 * f[i, j] + dy**2 * (un[i - 1, j] + un[i + 1, j]) + dx**2 * (un[i, j - 1] + un[i, j + 1])) / (2 * (dx**2 + dy**2))
    return u

