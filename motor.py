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

left_motor = None
right_motor = None


def init():
    global left_motor, right_motor
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.OUT)
    GPIO.setup((left_motor_parameters["en"], right_motor_parameters["en"]), GPIO.OUT)

    GPIO.output(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.LOW)
    left_motor = GPIO.PWM(left_motor_parameters["en"], PWM_FREQ)
    right_motor = GPIO.PWM(right_motor_parameters["en"], PWM_FREQ)

    left_motor.start(0)
    right_motor.start(0)

    print("Finished initializing motors.")


def drive(degrees, distance):
    left, right = d.joystickToDiff(degrees, distance, MIN_JOYSTICK, MAX_JOYSTICK, MIN_SPEED, MAX_SPEED)
    if right > 0:
        # Drive the motor clockwise
        GPIO.output(right_motor_parameters["in"][0], GPIO.HIGH)
        GPIO.output(right_motor_parameters["in"][1], GPIO.LOW)
    elif right < 0:
        # Drive the motor counter-clockwise
        GPIO.output(right_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(right_motor_parameters["in"][1], GPIO.HIGH)
    else:
        # Stop the motor
        GPIO.output(right_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(right_motor_parameters["in"][1], GPIO.LOW)

    if left > 0:
        # Drive the motor clockwise
        GPIO.output(left_motor_parameters["in"][0], GPIO.HIGH)
        GPIO.output(left_motor_parameters["in"][1], GPIO.LOW)
    elif left < 0:
        # Drive the motor counter-clockwise

        GPIO.output(left_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(left_motor_parameters["in"][1], GPIO.HIGH)
    else:
        # Stop the motor
        GPIO.output(left_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(left_motor_parameters["in"][1], GPIO.LOW)

    # Set speed of motor
    print(f"Set duty cycle: left motor: {math.fabs(left)}, right motor: {math.fabs(right)}")
    left_motor.ChangeDutyCycle(math.fabs(left))
    right_motor.ChangeDutyCycle(math.fabs(right))
