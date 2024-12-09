import numpy as np
import matplotlib.pyplot as plt

def plot_inscribed_circumscribed_polygon(sides_list, radius=1):
    # Figure and axis
    fig, ax = plt.subplots(1, len(sides_list), figsize=(6 * len(sides_list), 6))

    if len(sides_list) == 1:
        ax = [ax]

    # Loop over the number of sides to plot each polygon
    for i, sides in enumerate(sides_list):
        # Generate points for inscribed polygon
        inscribed_angles = np.linspace(0, 2 * np.pi, sides + 1)
        x_inscribed = radius * np.cos(inscribed_angles)
        y_inscribed = radius * np.sin(inscribed_angles)

        # Generate points for the circle
        circle_angles = np.linspace(0, 2 * np.pi, 1000)
        x_circle = radius * np.cos(circle_angles)
        y_circle = radius * np.sin(circle_angles)

        # Circumscribed polygon radius (adjusted so the sides are tangent to the circle)
        circumscribed_radius = radius / np.cos(np.pi / sides)
        x_circumscribed = circumscribed_radius * np.cos(inscribed_angles)
        y_circumscribed = circumscribed_radius * np.sin(inscribed_angles)

        # Plot circle
        ax[i].plot(x_circle, y_circle, linestyle='--', color='blue')

        # Plot inscribed polygon
        ax[i].plot(x_inscribed, y_inscribed, marker='o', color='red')

        # Plot circumscribed polygon
        ax[i].plot(x_circumscribed, y_circumscribed, marker='o', color='green')

        # Formatting
        ax[i].set_aspect('equal')
        ax[i].set_title(f'{sides}-sided Polygon')
        ax[i].annotate('', xy=(x_inscribed[1], y_inscribed[1]), xytext=(-10, 10),
                       textcoords='offset points', color='red', fontsize=10)
        ax[i].annotate('', xy=(x_circumscribed[1], y_circumscribed[1]), xytext=(-10, -15),
                       textcoords='offset points', color='green', fontsize=10)

    plt.tight_layout()
    plt.show()

plot_inscribed_circumscribed_polygon(sides_list=[3, 5, 10])
