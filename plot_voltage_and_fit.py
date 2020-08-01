import numpy as np
import matplotlib.pyplot as plt

# define fitting function
def ChargeProcess(t, V0, t0, tau):
    return V0 * (1-np.exp(-(t-t0)/tau))

# define fitting function
def DischargeProcess(t, V0, t0, tau):
    return V0 * (np.exp(-(t-t0)/tau))


# read data from file
t, v = np.loadtxt('voltageLog.txt', delimiter=' ', unpack = True)

# plot of the experimental data
plt.plot(t, v, 'o', color='blue', markersize = 3)
plt.axhline(color = 'gray', zorder = -1)
plt.axvline(color = 'gray', zorder = -1)
plt.xlabel('time  $t$ (s)')
plt.ylabel('voltage $V_C$ (V)')
plt.text(27, 1.8, 'R = 10 k$\Omega$'+'\n'+'C = 100 $\mu$F')

# model curve for the charge process
t_fit_charge = np.linspace(0, 20, 128)
V0, t0, tau = 3.2915, 0, 1.1687
v_fit_charge = ChargeProcess(t_fit_charge, V0, t0, tau)
plt.plot(t_fit_charge, v_fit_charge, color='green')
#plt.draw()


# model curve for the discharge process
t_fit_discharge = np.linspace(20.01, 40, 128)
V0, t0, tau = 3.3, 20.0053, 1.2019
v_fit_discharge = DischargeProcess(t_fit_discharge, V0, t0, tau)
plt.plot(t_fit_discharge, v_fit_discharge, color='green')
#plt.draw()


plt.savefig('plot_voltage_and_fit.pdf')
#plt.draw()
plt.show()