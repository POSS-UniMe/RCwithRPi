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
def measurement():
    for time_lapse in lapses:
        # read the time
        time = perf_counter() - start_time
        times.append(time)
        # read the voltage
        voltage_level = ReadChannel(voltage_channel)
        voltage_value = ConvertVolts(voltage_level)
        voltages.append(voltage_value)
        #
        sleep(time_lapse)


times = [ ]
voltages = [ ]

outputFile = 'VoltageSPI-LogSpaced.txt'
Delta_t_min = 50e-6
v_high_time = 20
points = 1000

start = np.log10(Delta_t_min)
stop = np.log10(v_high_time)
spots = np.logspace(start, stop, points)
lapses = np.diff(spots)

start_time = perf_counter()

# charging the capacitor
power.on()
measurement()

# discharging the capacitor
power.off()
measurement()

    
t = np.array(times)
v = np.array(voltages)

np.set_printoptions(precision = 20)
np.savetxt(outputFile, np.column_stack((t, v)))