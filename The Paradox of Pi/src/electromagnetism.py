import numpy as np
import matplotlib.pyplot as plt

def plot_em_wave():
    # Create a figure and 3D axis
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Parameters
    x = np.linspace(0, 4 * np.pi, 500)  # x-axis range
    E0 = 1  # Amplitude of the electric field
    B0 = 1  # Amplitude of the magnetic field
    k = 1   # Wave number
    omega = 1  # Angular frequency

    # Electric field 
    E_y = E0 * np.sin(k * x)

    # Magnetic field 
    B_z = B0 * np.sin(k * x)

    ax.plot(x, E_y, np.zeros_like(x), label='Electric Field $E(x,t)$', color='blue', linewidth=2)
    ax.plot(x, np.zeros_like(x), B_z, label='Magnetic Field $B(x,t)$', color='green', linewidth=2)

    # Add filled lines for the electric field
    for i in range(0, len(x), 10): 
        ax.plot([x[i], x[i]], [E_y[i], 0], [0, 0], color='blue', alpha=0.3)

    # Add filled lines for the magnetic field
    for i in range(0, len(x), 10):  
        ax.plot([x[i], x[i]], [0, 0], [B_z[i], 0], color='green', alpha=0.3)

    # Propagation direction
    ax.quiver(0, 0, 0, 4 * np.pi, 0, 0, color='gray', linewidth=2, arrow_length_ratio=0.02, label='Wave Propagation $x$')

    ax.set_xlabel('$x$ (Propagation Direction)')
    ax.set_ylabel('$y$ (Electric Field Direction)')
    ax.set_zlabel('$z$ (Magnetic Field Direction)')

    ax.view_init(elev=20, azim=30)

    ax.legend()

    plt.tight_layout()
    plt.show()

plot_em_wave()
