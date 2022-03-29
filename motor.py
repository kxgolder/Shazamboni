# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import math
import RPi.GPIO as GPIO
import differential_drive as d
from settings import *

from time import sleep

left_motor_parameters = {
    "in": [L_IN_1, L_IN_2],
    "en": L_EN
}

right_motor_parameters = {
    "in": [R_IN_1, R_IN_2],
    "en": R_EN
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.OUT)
GPIO.setup((left_motor_parameters["en"], right_motor_parameters["en"]), GPIO.OUT)

GPIO.output(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.LOW)
left_motor = GPIO.PWM(left_motor_parameters["en"], 1000)
right_motor = GPIO.PWM(right_motor_parameters["en"], 1000)

left_motor.start(25)
right_motor.start(25)


def drive(degrees, distance):
    right, left = d.joystickToDiff(degrees, distance, MIN_JOYSTICK, MAX_JOYSTICK, MIN_SPEED, MAX_SPEED)
    if right > 0:
        # Drive the motor clockwise
        GPIO.output(right_motor_parameters["in"][0], GPIO.HIGH)
        GPIO.output(right_motor_parameters["in"][1], GPIO.LOW)
    elif right < 0:
        # Drive the motor counter-clockwise
        GPIO.output(right_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(right_motor_parameters["in"][1], GPIO.HIGH)
    else:

        GPIO.output(right_motor_parameters["in"], GPIO.LOW)

    if left > 0:
        # Drive the motor clockwise
        GPIO.output(left_motor_parameters["in"][0], GPIO.HIGH)
        GPIO.output(left_motor_parameters["in"][1], GPIO.LOW)
    elif left < 0:
        # Drive the motor counter-clockwise

        GPIO.output(left_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(left_motor_parameters["in"][1], GPIO.HIGH)
    else:

        GPIO.output(left_motor_parameters["in"], GPIO.LOW)

    # Set speed of motor
    left_motor.ChangeDutyCycle(math.fabs(left))
    right_motor.ChangeDutyCycle(math.fabs(right))
