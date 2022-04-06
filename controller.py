import json
import asyncio
import websockets
import motor
import ultrasonic_sensors as u
import RPi.GPIO as GPIO
from multiprocessing import Process, Value
from gpiozero import DistanceSensor
from settings import *
import time

f_state = Value('s', "clear")
r_state = Value('s', "clear")


def front_ultrasonic_detection(a):
    front_ultrasonic = DistanceSensor(echo=F_GPIO_ECHO, trigger=F_GPIO_TRIGGER)
    while True:
        front_ultrasonic.wait_for_in_range()
        print("Front ultrasonic tripped, reversing vehicle")
        a.value = "triggered"
        motor.drive(180, 1)
        front_ultrasonic.wait_for_out_of_range()
        print("Out of range")
        if a.value == "triggered":
            motor.drive(0, 0)
        a.value = "clear"


def rear_ultrasonic_detection(a):
    rear_ultrasonic = DistanceSensor(echo=B_GPIO_ECHO, trigger=B_GPIO_TRIGGER)
    while True:
        rear_ultrasonic.wait_for_in_range()
        print("Rear ultrasonic tripped, advancing vehicle")
        a.value = "triggered"
        motor.drive(0, 1)
        rear_ultrasonic.wait_for_out_of_range()
        print("Out of range")
        if a.value == "triggered":
            motor.drive(0, 0)
        a.value = "clear"


async def handler(websocket):
    print(f"Client connected: {websocket.remote_address}")
    await websocket.send("Connected to server.")
    global f_state
    global r_state

    while True:

        try:
            message = await websocket.recv()
            print(message)
        except websockets.ConnectionClosedOK:
            print("Socket closed.")
            break
        try:
            result = json.loads(message)

            if f_state.value == "clear" and r_state.value == "clear":
                motor.drive(result["degrees"], result["distance"])
            else:
                continue

        except json.JSONDecodeError:
            continue
        # print(message)


async def main():
    print("Initializing ultrasonic sensors")
    u.init()
    global f_state
    global r_state
    p = Process(target=front_ultrasonic_detection, args=f_state)
    p1 = Process(target=rear_ultrasonic_detection, args=r_state)
    p.start()
    p1.start()

    print("Initializing motors")
    motor.init()
    print("Initializing websocket server")
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Cleaning up GPIO")
        GPIO.cleanup()
