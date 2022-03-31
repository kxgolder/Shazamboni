import json
import asyncio
import websockets
import motor
import ultrasonic_sensors as u
import RPi.GPIO as GPIO
from settings import *
import time


def check_distance(trigger, echo):
    if u.distance(trigger, echo) <= US_THRESHOLD:
        # Stop vehicle from moving
        motor.drive(0, 0)

        # if both sensors tripped threshold, vehicle is stuck
        if u.distance(F_GPIO_TRIGGER, F_GPIO_ECHO) <= US_THRESHOLD and u.distance(B_GPIO_TRIGGER,
                                                                                  B_GPIO_ECHO) <= US_THRESHOLD:
            print("Vehicle is stuck. Remove obstacles or adjust position")
            while True:
                # if vehicle is adjusted to be ok, return
                if u.distance(F_GPIO_TRIGGER, F_GPIO_ECHO) > US_THRESHOLD and u.distance(B_GPIO_TRIGGER,
                                                                                          B_GPIO_ECHO) > US_THRESHOLD:
                    print("Vehicle adjusted.")
                    return
        else:
            # If front ultrasonic is tripped, reverse vehicle
            if trigger == F_GPIO_TRIGGER:
                motor.drive(180, 0.5)
            else:
                # else read ultrasonic was triggered, advance vehicle
                motor.drive(0, 0.5)

            while True:
                # Stop vehicle after threshold is passed
                if u.distance(trigger, echo) > US_THRESHOLD:
                    motor.drive(0, 0)
                    return


async def handler(websocket):
    print(f"Client connected: {websocket.remote_address}")
    await websocket.send("Connected to server.")
    while True:

        try:
            message = await websocket.recv()
            print(message)
        except websockets.ConnectionClosedOK:
            print("Socket closed.")
            break
        try:
            result = json.loads(message)
            print(f"degrees: {result['degrees']}, distance: {result['distance']}")

            check_distance(F_GPIO_TRIGGER, F_GPIO_ECHO)
            check_distance(B_GPIO_TRIGGER, B_GPIO_ECHO)

            motor.drive(result["degrees"], result["distance"])
        except:
            continue
        # print(message)


async def main():
    print("Initializing ultrasonic sensors")
    u.init()
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
