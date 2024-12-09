import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi_approximation(num_terms):
    approximations = []
    actual_pi = np.pi
    errors = []

    # Calculate the Leibniz approximation for pi
    for n in range(num_terms):
        approx_pi = 4 * sum((-1)**k / (2*k + 1) for k in range(n + 1))
        approximations.append(approx_pi)
        errors.append(abs(approx_pi - actual_pi))

    return approximations, errors

def plot_leibniz_series(num_terms, zoom_range=200):
    approximations, errors = leibniz_pi_approximation(num_terms)
    actual_pi = np.pi
    terms = np.arange(1, num_terms + 1)

    # Plot the approximation of pi
    plt.figure(figsize=(10, 6))
    plt.plot(terms, approximations, label='Leibniz Approximation', color='blue')
    plt.axhline(y=actual_pi, color='red', linestyle='--', label=f'True Value of $\pi$ ({actual_pi:.5f})')
    plt.title(f'Convergence of the Leibniz Series for $\pi$ (First {num_terms} Terms)')
    plt.xlabel('Number of Terms')
    plt.ylabel('Approximation of $\pi$')
    plt.legend()
    plt.grid(True)

    # Zoom out 
    plt.xlim(0, zoom_range)
    plt.ylim(actual_pi - 0.1, actual_pi + 0.1)  # Wider y-axis around π

    plt.show()

    # Plot the error
    plt.figure(figsize=(10, 6))
    plt.plot(terms, errors, label='Error', color='purple')
    plt.title(f'Error in the Leibniz Approximation of $\pi$ (First {num_terms} Terms)')
    plt.xlabel('Number of Terms')
    plt.ylabel('Error')
    plt.yscale('log')
    plt.xlim(0, zoom_range)
    plt.legend()
    plt.grid(True, which='both', linestyle='--')

    plt.show()

plot_leibniz_series(num_terms=1000, zoom_range=200)
