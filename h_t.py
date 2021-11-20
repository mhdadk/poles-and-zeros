# code used to generate the 2D plot of h(t)
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,2,1000)
h = np.sin(2*np.pi*t)
fig,ax = plt.subplots()
ax.plot(t,h)
ax.set_xlabel("t")
ax.set_ylabel("h(t)")