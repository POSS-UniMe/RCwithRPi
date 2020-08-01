from gpiozero import LED
from time import sleep, perf_counter
import spidev
import numpy as np

power = LED(17)

# open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

# read the data corresponding to a selected channel
# of the ADC MCP3008
def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel)<<4, 0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

# convert data to voltage
def ConvertVolts(data):
    volts = (data * 3.3)/float(1023)
    return volts

# define channel
voltage_channel = 0

# function to perform the measurements
def measurement(time_limit):
    while True:
        # read the time
        time = perf_counter() - start_time
        times.append(time)
        # read the voltage
        voltage_level = ReadChannel(voltage_channel)
        voltage_value = ConvertVolts(voltage_level)
        voltages.append(voltage_value)
        if time > time_limit:
            break
        sleep(sleep_time)


sleep_time = 0.1
exec_time = 40
v_high_time = 20
outputFile = 'VoltageSPI-Log.txt'

times = [ ]
voltages = [ ]

start_time = perf_counter()

# charging the capacitor
t_limit = v_high_time
power.on()
measurement(t_limit)

# discharging the capacitor
t_limit = exec_time
power.off()
measurement(t_limit)

    
t = np.array(times)
v = np.array(voltages)

np.set_printoptions(precision = 20)
np.savetxt(outputFile, np.column_stack((t, v)))