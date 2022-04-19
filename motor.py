# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import math
import RPi.GPIO as GPIO
import differential_drive as d
from gpiozero import Motor
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
#
# left_motor = None
# right_motor = None


# def init():
#     global left_motor
#     global right_motor
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(L_IN_1, GPIO.OUT)
#     GPIO.setup(L_IN_2, GPIO.OUT)
#     GPIO.setup(R_IN_1, GPIO.OUT)
#     GPIO.setup(R_IN_2, GPIO.OUT)
#     GPIO.setup(L_EN, GPIO.OUT)
#     GPIO.setup(R_EN, GPIO.OUT)
#
#     GPIO.output(L_IN_1, GPIO.LOW)
#     GPIO.output(L_IN_2, GPIO.LOW)
#     GPIO.output(R_IN_1, GPIO.LOW)
#     GPIO.output(R_IN_2, GPIO.LOW)
#
#     right_motor = GPIO.PWM(right_motor_parameters["en"], PWM_FREQ)
#     left_motor = GPIO.PWM(left_motor_parameters["en"], PWM_FREQ)
#
#     left_motor.start(0)
#     right_motor.start(0)
#
#     print("Finished initializing motors.")


def drive(degrees, distance, left_motor, right_motor):

    left, right = d.joystickToDiff(degrees, distance, MIN_JOYSTICK, MAX_JOYSTICK, MIN_SPEED, MAX_SPEED)
    left /= 100
    right /= 100
    if left is None and right is None:
        return
    if right > 0:
        # Drive the motor clockwise
        # GPIO.output(right_motor_parameters["in"][0], GPIO.HIGH)
        # GPIO.output(right_motor_parameters["in"][1], GPIO.LOW)
        right_motor.forward(math.fabs(right))
    elif right < 0:
        # Drive the motor counter-clockwise
        # GPIO.output(right_motor_parameters["in"][0], GPIO.LOW)
        # GPIO.output(right_motor_parameters["in"][1], GPIO.HIGH)
        right_motor.backward(math.fabs(right))

    else:
        # Stop the motor
        # GPIO.output(right_motor_parameters["in"][0], GPIO.LOW)
        # GPIO.output(right_motor_parameters["in"][1], GPIO.LOW)
        right_motor.stop()

    if left > 0:
        # Drive the motor clockwise
        # GPIO.output(left_motor_parameters["in"][0], GPIO.HIGH)
        # GPIO.output(left_motor_parameters["in"][1], GPIO.LOW)
        left_motor.forward(math.fabs(left))

    elif left < 0:
        # Drive the motor counter-clockwise

        # GPIO.output(left_motor_parameters["in"][0], GPIO.LOW)
        # GPIO.output(left_motor_parameters["in"][1], GPIO.HIGH)
        left_motor.backward(math.fabs(left))

    else:
        # Stop the motor
        # GPIO.output(left_motor_parameters["in"][0], GPIO.LOW)
        # GPIO.output(left_motor_parameters["in"][1], GPIO.LOW)
        left_motor.stop()

    # Set speed of motor
    # print(f"Degrees: {degrees}")
    # print(f"Set duty cycle: left motor: {math.fabs(left)}, right motor: {math.fabs(right)}")
    # right_motor.ChangeDutyCycle(math.fabs(right))
    # left_motor.ChangeDutyCycle(math.fabs(left))
