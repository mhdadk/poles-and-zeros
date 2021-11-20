# code used to generate the magnitude and phase plots of
#
# H(s) = (s - 0.5) / (s - 1.5) * (s + 2)
#
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams.update({'font.size': 12})

re = np.linspace(-3,3,200)
im = np.linspace(-3,3,200)
s = re[:, None] + 1j * im

H = (s - 0.5) / ((s - 1.5) * (s + 2))

C = np.abs(H)
theta = np.arctan2(H.imag,H.real)

fig = plt.figure()
ax = fig.add_subplot(1,2,1,projection='3d')
ax.plot_surface(s.real, s.imag, C, cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("C")
ax.set_zlim(0,3)

ax = fig.add_subplot(1,2,2,projection='3d')
ax.plot_surface(s.real, s.imag, theta, cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("theta")

plt.tight_layout()