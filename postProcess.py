import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

def plotPoissons(u, X, Y):
    # Plot solution
    F = plt.gcf()
    Size = F.get_size_inches()
    F.set_size_inches(Size[0]*1.5, Size[1]*1.5, forward=True) 

    ax = F.add_subplot(111, projection='3d')
    ax.set_facecolor('white')
    ax.set_facecolor('white')  # Set face color to white
    ax.xaxis.pane.fill = False  # Remove background color from x-axis plane
    ax.yaxis.pane.fill = False  # Remove background color from y-axis plane
    ax.zaxis.pane.fill = False  # Remove background color from z-axis plane
    ax.grid(False)  # Remove grid lines
    ax.zaxis.line.set_visible(False) # Hide the z-axis
    ax.w_zaxis.line.set_color('none')  # Remove z-axis line by setting color 
    for spine in ax.spines.values():
        spine.set_color('none')  # Remove box by setting color to 'none'

    # Create the surface plot
    surf = ax.plot_surface(X, Y, u, cmap='bwr', alpha=0.8)

    # Set contour levels
    contour_min = np.min(u)
    contour_max = np.max(u)
    contour_levels = np.linspace(contour_min, contour_max, 11)

    contour = ax.contour(X, Y, u, zdir='z', offset=contour_min, cmap='bwr', linestyles="solid", levels = contour_levels)

    # Colorbar properties
    cbar = F.colorbar(surf)
    cbar_ticks = np.linspace(contour_min, contour_max, 5)
    cbar.set_ticks(cbar_ticks)
    cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))  # Set format for ticks
    cbar.set_label('u', rotation=0, labelpad=15)
    cbar.ax.tick_params(labelsize=18)  # Set font size for ticks

    ax.set_xlabel('x', fontsize=20,fontname = "Times New Roman", fontweight="normal")
    ax.set_ylabel('y', fontsize=20,fontname = "Times New Roman", fontweight="normal")
    cbar.set_label('u', rotation=90, labelpad=15, fontdict={'family': 'Times New Roman', 'size': 20})  # Set font type and size for label

    #ax.zaxis.set_ticks([])  # Remove z-axis ticks

    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300

    plt.savefig("field.png") 


def plotLaplace(u, X, Y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, u, cmap='viridis')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Surface Plot of u')
    plt.colorbar(surf)
    plt.savefig("field.png")    