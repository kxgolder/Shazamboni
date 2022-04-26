import json
import asyncio
import websockets
import motor
import ultrasonic_sensors as u
import RPi.GPIO as GPIO
from multiprocessing import Process, Value
from gpiozero import DistanceSensor, Motor
from settings import *
import time

f_state = Value('i', 0)
r_state = Value('i', 0)


def front_ultrasonic_detection(a):
    front_ultrasonic = DistanceSensor(echo=F_GPIO_ECHO, trigger=F_GPIO_TRIGGER)
    front_ultrasonic.threshold_distance = US_THRESHOLD

    # u.init()
    # motor.init()

    while True:
        front_ultrasonic.wait_for_in_range()
        lm = Motor(L_IN_1, L_IN_2, enable=L_EN)
        rm = Motor(R_IN_1, R_IN_2, enable=R_EN)
        print("Front ultrasonic tripped, reversing vehicle")
        a.value = 1

        lm.backward(1)
        rm.backward(1)

        front_ultrasonic.wait_for_out_of_range()
        print("Out of range")
        # if a.value == "triggered":
        # motor.drive(0, 0)
        lm.stop()
        rm.stop()
        lm.close()
        rm.close()
        a.value = 0


def rear_ultrasonic_detection(a):
    rear_ultrasonic = DistanceSensor(echo=B_GPIO_ECHO, trigger=B_GPIO_TRIGGER)
    rear_ultrasonic.threshold_distance = US_THRESHOLD

    # u.init()
    # motor.init()

    while True:
        rear_ultrasonic.wait_for_in_range()
        lm = Motor(L_IN_1, L_IN_2, enable=L_EN)
        rm = Motor(R_IN_1, R_IN_2, enable=R_EN)
        print("Rear ultrasonic tripped, advancing vehicle")
        a.value = 1
        lm.forward(1)
        rm.forward(1)
        rear_ultrasonic.wait_for_out_of_range()
        print("Out of range")
        # if a.value == "triggered":
        # motor.drive(0, 0)
        lm.stop()
        rm.stop()
        lm.close()
        rm.close()
        a.value = 0


left_motor = None
right_motor = None
front_ultrasonic = DistanceSensor(echo=F_GPIO_ECHO, trigger=F_GPIO_TRIGGER)
front_ultrasonic.threshold_distance = US_THRESHOLD

rear_ultrasonic = DistanceSensor(echo=B_GPIO_ECHO, trigger=B_GPIO_TRIGGER)
rear_ultrasonic.threshold_distance = US_THRESHOLD

async def handler(websocket):
    global left_motor, right_motor
    print(f"Client connected: {websocket.remote_address}")
    await websocket.send("Connected to server.")

    while True:
        try:
            message = await websocket.recv()
        except websockets.ConnectionClosedOK:
            print("Socket closed.")
            break
        try:
            result = json.loads(message)
            print(result)
            if f_state.value == 0 and r_state.value == 0:
                if left_motor is None:
                    left_motor = Motor(L_IN_1, L_IN_2, enable=L_EN, pwm=True)
                if right_motor is None:
                    right_motor = Motor(R_IN_1, R_IN_2, enable=R_EN, pwm=True)

                if(front_ultrasonic.distance <= US_THRESHOLD):
                    motor.drive(180, 1, left_motor, right_motor)
                    time.sleep(0.5)
                    motor.drive(0, 0, left_motor, right_motor)


                if (rear_ultrasonic.distance <= 0.4):
                    motor.drive(0, 1, left_motor, right_motor)
                    time.sleep(0.5)
                    motor.drive(0, 0, left_motor, right_motor)


                motor.drive(result["degrees"], result["distance"], left_motor, right_motor)
                # left_motor.forward(1)

            else:
                # print("Closing motors")
                if left_motor is not None:
                    left_motor.close()
                    left_motor = None

                if right_motor is not None:
                    right_motor.close()
                    right_motor = None
                print("Continue")
                continue

        except json.JSONDecodeError:
            continue
        # print(message)


async def main():
    print("Initializing websocket server")
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    # print("Initializing motors")
    # motor.init()
    # print("Initializing ultrasonic sensors")

    try:
        # p = Process(target=front_ultrasonic_detection, args=(f_state,))
        # p1 = Process(target=rear_ultrasonic_detection, args=(r_state,))
        # p.start()
        # p1.start()

        asyncio.run(main())
    except KeyboardInterrupt:
        # p.terminate()
        # p1.terminate()
        print("Cleaning up GPIO")
        GPIO.cleanup()
