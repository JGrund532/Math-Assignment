import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate sample data
np.random.seed(0)
data = np.random.normal(loc=50, scale=10, size=100)

# Calculate z-scores
zscores = stats.zscore(data)

# Plot the normal distribution curve
mu = 0
sigma = 1
x = np.linspace(-4, 4, 100)
y = stats.norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r-', label='normal distribution')

# Fill the area under the curve from minus infinity to the calculated z-score
z = zscores[0]
plt.fill_between(x[x<z], y[x<z], 0, color='red', alpha=0.3)

plt.title("Normal Distribution Curve")
plt.xlabel("Z-Score")
plt.ylabel("Density")
plt.legend()
plt.show()