import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

class BellCurve:
    def __init__(self, mu, sigma, z_score):
        self.mu = mu
        self.sigma = sigma
        self.z_score = z_score

    def plot_c(self):
        x = np.linspace(self.mu - 4 * self.sigma, self.mu + 4 * self.sigma, 100)
        y = stats.norm.pdf(x, self.mu, self.sigma)

        plt.plot(x, y, '-b')
        plt.fill_between(x, y, where=(x >= self.mu - self.z_score * self.sigma) & (x <= self.mu + self.z_score * self.sigma), color='red', alpha=0.5)
        plt.title("Normal Bell Curve")
        plt.xlabel("X")
        plt.ylabel("Probability Density")
        plt.show()

bell_curve = BellCurve(0, 1, 1.96)
bell_curve.plot()
