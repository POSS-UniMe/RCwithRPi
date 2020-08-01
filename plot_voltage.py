#   plot_voltage.py

import numpy as np
import matplotlib.pyplot as plt

# read data from file
t, v = np.loadtxt('voltageLog.txt', delimiter=' ', unpack = True)

# plot of the experimental data
plt.plot(t, v, 'o', color='blue', markersize = 3)
plt.axhline(color = 'gray', zorder = -1)
plt.axvline(color = 'gray', zorder = -1)
plt.xlabel('time  $t$ (s)')
plt.ylabel('voltage $V_C$ (V)')
plt.text(27, 1.8, 'R = 10 k$\Omega$'+'\n'+'C = 100 $\mu$F')

plt.savefig('plot_voltage.pdf')
plt.show()