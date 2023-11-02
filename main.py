import numpy as np
import matplotlib.pyplot as plt


def solveFD(nx, ny, f, size):
    # Solve Poisson equation using finite difference method
    for it in range(size):
        un = u.copy()
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                u[i, j] = (dx**2 * dy**2 * f[i, j] + dy**2 * (un[i - 1, j] + un[i + 1, j]) + dx**2 * (un[i, j - 1] + un[i, j + 1])) / (2 * (dx**2 + dy**2))
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
size = 100


# Initialize solution array
u = np.zeros((nx, ny))

# Define boundary conditions
u[0, :] = 0.0  # u = 0 at x = 0
u[-1, :] = 0.0  # u = 0 at x = 1
u[:, 0] = 0.0  # u = 0 at y = 0
u[:, -1] = 0.0  # u = 0 at y = 1

# Solve Poisson equation using finite difference method
u = solveFD(nx, ny, f, size)

# Plot solution
fig = plt.figure(figsize=(8, 6), dpi=300)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, u, cmap='bwr', alpha=0.8)
contour = ax.contour(X, Y, u, zdir='z', offset=np.min(u), cmap='bwr', linestyles="solid")
fig.colorbar(surf)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('u')
plt.show()