# code used to generate the magnitude and phase plots of H(s) = s^2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams.update({'font.size': 12})

re = np.linspace(-2,2,100)
im = np.linspace(-2,2,100)
s = re[:, None] + 1j * im

C = np.sqrt((s.real**2 - s.imag**2)**2 + (2*s.real*s.imag)**2)
theta = np.arctan2(2*s.real*s.imag,
                   s.real**2 - s.imag**2)

fig = plt.figure()
ax = fig.add_subplot(1,2,1,projection='3d')
ax.plot_surface(s.real, s.imag, C, cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("C")

ax = fig.add_subplot(1,2,2,projection='3d')
ax.plot_surface(s.real, s.imag, theta, cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("theta")

plt.tight_layout()
