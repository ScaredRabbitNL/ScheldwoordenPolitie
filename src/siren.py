import time
from gpiozero import LEDBoard, Buzzer

leds = LEDBoard(18,24)
buzzer = Buzzer(22)

def siren(x):
    for y in range(x):
        #buzzer.on()
        #time.sleep(1)
        #buzzer.off()
        for led in leds:
            led.on()
            time.sleep(0.1)
            led.off()
