# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import math
import RPi.GPIO as GPIO
import differential_drive as d

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
    "in": [27, 17],
    "en": 22
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.OUT)
GPIO.setup((left_motor_parameters["en"], right_motor_parameters["en"]), GPIO.OUT)

GPIO.output(left_motor_parameters["in"] + right_motor_parameters["in"], GPIO.LOW)
left_motor = GPIO.PWM(left_motor_parameters["en"], 1000)
right_motor = GPIO.PWM(right_motor_parameters["en"], 1000)

left_motor.start(25)
right_motor.start(25)
MAX_JOYSTICK = 1
MIN_JOYSTICK = -1
MAX_SPEED = 100
MIN_SPEED = -100


def drive(degrees, distance):
    right, left = d.joystickToDiff(degrees, distance, MIN_JOYSTICK, MAX_JOYSTICK, MIN_SPEED, MAX_SPEED)
    if right > 0:

        GPIO.output(right_motor_parameters["in"][0], GPIO.HIGH)
        GPIO.output(right_motor_parameters["in"][1], GPIO.LOW)
    elif right < 0:

        GPIO.output(right_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(right_motor_parameters["in"][1], GPIO.HIGH)
    else:

        GPIO.output(right_motor_parameters["in"], GPIO.LOW)

    if left > 0:

        GPIO.output(left_motor_parameters["in"][0], GPIO.HIGH)
        GPIO.output(left_motor_parameters["in"][1], GPIO.LOW)
    elif left < 0:

        GPIO.output(left_motor_parameters["in"][0], GPIO.LOW)
        GPIO.output(left_motor_parameters["in"][1], GPIO.HIGH)
    else:

        GPIO.output(left_motor_parameters["in"], GPIO.LOW)

    left_motor.ChangeDutyCycle(math.fabs(left))
    right_motor.ChangeDutyCycle(math.fabs(right))
