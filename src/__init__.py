import time
from gpiozero import Buzzer, LEDBoard

buzzer = Buzzer(22)
leds = LEDBoard(18,24)

def __init__(x):
    for y in range(5 * x):
    
        for led in leds:
            led.on()
            time.sleep(0.1)
            led.off()

__init__(5)
