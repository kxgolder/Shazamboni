# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO
from time import sleep

# in1 = 24  # pin 24
# in2 = 23  # pin 24
# en = 25  # pin 25
left_motor_parameters = {
    "in": [23, 24],
    "en": 25
}
# in3 = 26  # pin 24
# in4 = 27  # pin 24
# enb = 28  # pin 28
right_motor_parameters = {
    "in": [26, 27],
    "en": 28
}
SPEED = 75
def init():
GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.OUT)
GPIO.setup((left_motor_parameters["en"], right_motor_parameters["en"]), GPIO.OUT)

GPIO.output(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.LOW)
left_motor = GPIO.PWM(left_motor_parameters["en"], 1000)
right_motor = GPIO.PWM(right_motor_parameters["en"], 1000)

left_motor.start(25)
right_motor.start(25)


def forward():
    GPIO.output(left_motor_parameters["in"][0], GPIO.HIGH)
    GPIO.output(left_motor_parameters["in"][1], GPIO.LOW)
    left_motor.ChangeDutyCycle(SPEED)


def stop():
    GPIO.output(left_motor_parameters["in"], GPIO.LOW)


def backward():
    GPIO.output(left_motor_parameters["in"][0], GPIO.LOW)
    GPIO.output(left_motor_parameters["in"][1], GPIO.HIGH)
