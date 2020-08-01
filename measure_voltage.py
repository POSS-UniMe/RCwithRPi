from gpiozero import LED, MCP3008
from time import sleep

power = LED(17)
pot = MCP3008(0)
Vdc = 3.3

while True:
    power.on()
    print(pot.value * Vdc)
    sleep(1)
    power.off()
    print(pot.value * Vdc)
    sleep(1)