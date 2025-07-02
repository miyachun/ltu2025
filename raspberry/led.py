import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25,GPIO.OUT)
    print("OK")

def blink():
    while True:
        GPIO.output(25,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25,GPIO.LOW)
        time.sleep(1)

if __name__=="__main__":
    setup()
    blink()
