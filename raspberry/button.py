import RPi.GPIO as GPIO
from time import sleep

btn_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  if GPIO.input(btn_pin) == GPIO.HIGH:
    print("按下按鈕")
  elif GPIO.input(btn_pin) == GPIO.LOW:
    print("未按下按鈕")
  sleep(0.2)
