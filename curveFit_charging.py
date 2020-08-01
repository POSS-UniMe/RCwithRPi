import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import scipy.optimize

res = 3.3 / 1023
inputFile = 'chargingProcessData.txt'

# define fitting function
def ChargeProcess(t, V0, t0, tau):
    return V0 * (1-np.exp(-(t-t0)/tau))

# read the experimental data from file
t, v = np.loadtxt(inputFile, delimiter = ' ', unpack = True)

# assign the experimental uncertainty on Voltage values
dv = np.ones(v.size) * res

# initial guesses for fitting parameters
V0_guess, t0_guess, tau_guess = 3., 0., 1.

# fitting procedure
nlfit, nlpcov = \
       scipy.optimize.curve_fit(ChargeProcess, t, v, \
                                p0 = [V0_guess, t0_guess, tau_guess], sigma = dv,\
                                bounds = (0, 100))
		# we apply bounds to the free parameters so that only positive values are allowed.

# obtaining parameters from the best fit procedure
V0, t0, tau = nlfit

# obtaining uncertainties associated with fitting parameters
dV0, dt0, dtau = \
     [np.sqrt(nlpcov[j, j]) for j in range(nlfit.size)]

# create fitting function from fitted parameters
t_fit = np.linspace(t.min(), t.max(), 128)
v_fit = ChargeProcess(t_fit, V0, t0, tau)

# residuals and reduced chi squared
resids = v - ChargeProcess(t, V0, t0, tau)
redchisqr = ((resids/dv)**2).sum()/float(t.size-3)
ndf = t.size-3
# where 3 is the number of free parameters


# create figure window to plot data
fig = plt.figure(1, figsize = (8,8))
gs = gridspec.GridSpec(2, 1, height_ratios = [6, 2])

# plotting data and fit
ax1 = fig.add_subplot(gs[0])
ax1.plot(t_fit, v_fit)
ax1.errorbar(t, v, yerr = dv, fmt = 'or', ecolor = 'black', markersize = 2)
ax1.set_xlabel(' time (s)')
ax1.set_ylabel('voltage $V_C$ (V)')
ax1.text(0.5, 0.50, r'$V_0$ = {0:6.4f}$\pm${1:0.4f}'.format(V0, dV0), transform = ax1.transAxes, fontsize = 14)
ax1.text(0.5, 0.40, r'$\tau$ = {0:6.4f}$\pm${1:0.4f}'.format(tau, dtau), transform = ax1.transAxes, fontsize=14)
ax1.text(0.5, 0.30, r'$t_0$= {0:5.4f}$\pm${1:0.4f}'.format(t0, dt0), transform = ax1.transAxes, fontsize=14)
ax1.text(0.5, 0.20, r'$\chi_r^2$ = {0:0.1f}, ndf = {1}'.format(redchisqr, ndf), transform = ax1.transAxes, fontsize=14)

# plotting residuals
ax2 = fig.add_subplot(gs[1])
ax2.errorbar(t, resids, yerr = dv, ecolor = 'black', fmt ='ro', markersize = 2)
ax2.axhline(color = 'gray', zorder = -1)
ax2.set_xlabel('time (s)')
ax2.set_ylabel('residuals (V)')
plt.savefig('ChargingProcessDataAndFit.pdf')
plt.show()