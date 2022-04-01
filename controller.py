import json
import asyncio
import websockets
import motor
import ultrasonic_sensors as u
import RPi.GPIO as GPIO
from settings import *
import time

def check_distance(trigger1, trigger2, echo1, echo2, back_dist, front_dist):
    print("Checking distance")
    if back_dist <= US_THRESHOLD or front_dist <= US_THRESHOLD:

        # Stop vehicle from moving
        print("Stopping vehicle")
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
                    return 1
        else:
            # If front ultrasonic is tripped, reverse vehicle
            if front_dist <= US_THRESHOLD:
                print("Front ultrasonic tripped, reversing vehicle")
                motor.drive(180, 1)
            else:
                # else read ultrasonic was triggered, advance vehicle
                print("Rear ultrasonic tripped, advancing vehicle")
                motor.drive(0, 1)

            while True:
                # Stop vehicle after threshold is passed
                if u.distance(trigger1, echo1) > US_THRESHOLD + US_ADDITIONAL_DISTANCE and u.distance(trigger2, echo2) > US_THRESHOLD + US_ADDITIONAL_DISTANCE:
                    motor.drive(0, 0)
                    return 1


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
            # check_distance(F_GPIO_TRIGGER, F_GPIO_ECHO)
            front_dist = u.distance(F_GPIO_TRIGGER, F_GPIO_ECHO)
            back_dist = u.distance(B_GPIO_TRIGGER, B_GPIO_ECHO)
            print(back_dist, front_dist)
            if back_dist <= US_THRESHOLD or front_dist <= US_THRESHOLD:
                print("SENDING 1")
                await websocket.send("1")
            if not (check_distance(B_GPIO_TRIGGER, F_GPIO_TRIGGER, B_GPIO_ECHO, F_GPIO_ECHO, back_dist, front_dist)):
                motor.drive(result["degrees"], result["distance"])
            else:
                print("Dropped packet")
                print("SENDING 0")
                await websocket.send("0")
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
