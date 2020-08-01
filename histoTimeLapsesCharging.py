import numpy as np
import matplotlib.pyplot as plt

DataFile='timeLapsesChargeProcess.txt'
OutputFile='histoLapsesCharging.pdf'
bins=100

# read data from file
t, Delta_t = np.loadtxt(DataFile, delimiter=' ', unpack = True)
# plot
plt.hist(Delta_t*1e6, bins, log = True)
plt.xlabel('time lapses  $\Delta t$ ($\mu$s)')
plt.ylabel('counts')
plt.tight_layout()
plt.savefig(OutputFile)
plt.show()