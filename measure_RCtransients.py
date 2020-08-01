from gpiozero import LED, MCP3008
from time import sleep, perf_counter
import numpy as np

power = LED(17)
pot = MCP3008(0)

sleep_time = 0.1
exec_time = 40
v_high_time = 20
Vdc = 3.3
outputFile='voltageLog.txt'

def measurement(time_limit):
    while True:
        time = perf_counter() - start_time
        times.append(time)
        voltage = pot.value * Vdc
        voltages.append(voltage)
        if time > time_limit:
            break
        sleep(sleep_time)
        
times = [ ]
voltages = [ ]

start_time = perf_counter()

# charging
t_limit = v_high_time
power.on()
measurement(t_limit)

# discharging
t_limit = exec_time
power.off()
measurement(t_limit)

t = np.array(times)
v = np.array(voltages)

np.set_printoptions(precision = 20)
np.savetxt(outputFile, np.column_stack((t, v)))