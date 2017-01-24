import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

led1 = 1

while led1 <= 25:
    led1 += 1
    GPIO.output(7, True)
    time.sleep(0.25)
    GPIO.output(7, False)
    time.sleep(0.25)
    GPIO.output(7, True)
    time.sleep(0.12)
    GPIO.output(7, False)
    time.sleep(0.12)

print("Show's over, folks!")

GPIO.cleanup()
