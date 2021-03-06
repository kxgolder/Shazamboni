# Libraries
import RPi.GPIO as GPIO
from settings import *
import time


# set GPIO direction (IN / OUT)
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(F_GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(F_GPIO_ECHO, GPIO.IN)
    GPIO.setup(B_GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(B_GPIO_ECHO, GPIO.IN)


def distance(trigger, echo):
    # set Trigger to HIGH
    #    print("Setting trigger to high")
    GPIO.output(trigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    # GPIO.output(GPIO_TRIGGER_2, False)
    #    print("Get start time")
    StartTime = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        #        print("GPIO input echo is zero")
        StartTime = time.time()

    # while GPIO.input(GPIO_ECHO_2) == 0:
    # StartTime_2 = time.time()
    # save time of arrival
    while GPIO.input(echo) == 1:
        #        print("GPIO Input echo is one")
        StopTime = time.time()
        if ((StopTime - StartTime) * 34300 / 2) >= 250:
            break

    # while GPIO.input(GPIO_ECHO_2) == 1:
    # StopTime_2 = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # TimeElapsed2 = StopTime_2 - StartTime_2

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    distance = (TimeElapsed * 34300) / 2
    # distance2 = (TimeElapsed2 * 34300) / 2
    #    print(distance)
    return distance
