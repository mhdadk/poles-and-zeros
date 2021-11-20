# code used to generate slices of the magnitude and phase plots of
#
# H(s) = (s - 0.5) / (s - 1.5) * (s + 2)
#
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams.update({'font.size': 12})

bound = 3
re = np.linspace(-bound,bound,200)
im = np.linspace(-bound,bound,200)
s = re[:, None] + 1j * im

H = (s - 0.5) / ((s - 1.5) * (s + 2))

C = np.abs(H)
theta = np.arctan2(H.imag,H.real)

fig = plt.figure()

ax = fig.add_subplot(1,2,1,projection='3d')
ax.plot_surface(s.real[:100,:], s.imag[:100,:], C[:100,:], cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.plot3D(s.real[100,:],s.imag[100,:],C[100,:],color='purple',linewidth=7)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("C")
ax.set_xlim(-bound,bound)
ax.set_ylim(-bound,bound)
ax.set_zlim(0,3)

ax = fig.add_subplot(1,2,2,projection='3d')
ax.plot_surface(s.real[:100,:], s.imag[:100,:], theta[:100,:], cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.plot3D(s.real[100,:],s.imag[100,:],theta[100,:],color='purple',linewidth=7)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_xlim(-bound,bound)
ax.set_ylim(-bound,bound)
ax.set_zlabel("theta")

plt.tight_layout()