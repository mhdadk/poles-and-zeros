# code used to generate plots comparing 2D and 3D magnitude and phase plots of
#
# H(s) = (s - 0.5) / (s - 1.5) * (s + 2)
#
import numpy as np
from scipy import signal
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

ax = fig.add_subplot(2,2,1,projection='3d')
ax.plot_surface(s.real[50:100,:], s.imag[50:100,:], C[50:100,:], cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.plot3D(s.real[100,:],s.imag[100,:],C[100,:],color='purple',linewidth=7)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_zlabel("C")
ax.set_xlim(-bound,bound)
ax.set_ylim(-bound,bound)
ax.set_zlim(0,0.4)

ax = fig.add_subplot(2,2,2,projection='3d')
ax.plot_surface(s.real[50:100,:], s.imag[50:100,:], theta[50:100,:], cmap=cm.jet,
                linewidth=0, antialiased=False)
ax.plot3D(s.real[100,:],s.imag[100,:],theta[100,:],color='purple',linewidth=7)
ax.set_xlabel("Real")
ax.set_ylabel("Imaginary")
ax.set_xlim(-bound,bound)
ax.set_ylim(-bound,bound)
ax.set_zlabel("theta")
ax.set_zlim(-1.5,1.5)

omega = np.linspace(-3,3,200)
omega,H_omega = signal.freqs_zpk([0.5],[1.5,-2],1,omega)
mag = np.abs(H_omega)
phase = np.arctan2(H_omega.imag,H_omega.real)

ax = fig.add_subplot(2,2,3)
ax.plot(omega,mag)
ax.set_ylim(0,0.4)
ax.set_xlabel("Omega")
ax.set_ylabel("C")

ax = fig.add_subplot(2,2,4)
ax.plot(omega,phase)
ax.set_ylim(-1.5,1.5)
ax.set_xlabel("Omega")
ax.set_ylabel("theta")