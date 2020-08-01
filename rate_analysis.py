import numpy as np
import matplotlib.pyplot as plt

inputDataFile = 'ChargeProcessDataZeroSleepOneSecond.txt'
outputDataFile = 'timeLapsesChargeProcessOneSecond.txt'
outParFile = 'ChargeDeltatParamsOneSecond.txt'

# read data from the file
t = np.loadtxt(inputDataFile, delimiter = ' ', usecols=(0), unpack = True)

# compute time lapses
delta_t = np.diff(t)
t_prime = t[:-1] + (delta_t/2)

# save the results as text
np.set_printoptions(precision = 20)
np.savetxt(outputDataFile, np.column_stack((t_prime, delta_t)))

# statistical analysis on time lapses
dt_mean = np.mean(delta_t, dtype = np.float64)
dt_min = np.min(delta_t)
dt_max = np.max(delta_t)
dt_std = np.std(delta_t, dtype = np.float64)

print('Delta t mean value = ', dt_mean)
print('Delta t minimum = ', dt_min)
print('Delta t mean value = ', dt_mean)
print('Delta t maximum = ', dt_max)

# write the results of the statistical analysis to a text file
fout = open(outParFile, 'w')
fout.write('Statistical analysis on times from the file: \n')
fout.write(outputDataFile + '\n' + '\n')
fout.write('Delta_t mean value = ' + str(dt_mean) + '\n')
fout.write('Delta_t minimum = ' + str(dt_min) + '\n')
fout.write('Delta_t maximum = ' + str(dt_max) + '\n')
fout.write('Delta_t standard deviation = ' + str(dt_std))
fout.close()


# plot of Delta_t vs- t
plt.plot(t_prime, delta_t*1e6, 'o', color = 'blue', markersize = 1)
plt.xlabel('time $t$ (s)')
plt.ylabel('time lapses $\Delta t$ ($\mu$s)')
plt.tight_layout()
plt.ylim(140, 360)
# save the plot to a file
plt.savefig('rate_analysis_zeroSleepOneSecond.pdf')
#plt.draw()
plt.show()