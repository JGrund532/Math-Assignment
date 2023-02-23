import function_operators as fo 
import statistics_operator as so
import probability_operators as po
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.stats as stats
import math 



import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(3, 3))

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = ax.plot(t, s, lw=2)

ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.set_ylim(-2, 2)