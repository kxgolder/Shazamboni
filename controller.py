import socket
import json
import math
import motor

s = socket.socket()
print("Created Socket")
port = 12345
s.bind(('', port))
print(f"socket binded to {port}")
s.listen(5)
print("socket is listening")


def servo(degrees):
    print(f"set wheels to {degrees}")


def set_wheels(degrees):
    servo(degrees)


def set_speed(degrees, distance):
    if degrees == 0:
        motor.stop()
        print(f"stop")
    elif degrees > 180:
        motor.backward()
        print(f"go backward")

    elif degrees < 180:
        motor.forward()
        print(f"go forward")

while True:
    c, addr = s.accept()
    print(f"Connected to {addr}")
    c.send("OK".encode())
    while(1):
        try:
            result = json.loads(c.recv(1024).decode())
            print(result)
        except:
            continue
        # x = result["distance"]*math.cos(result["degrees"])
        # y = result["distance"] * math.sin(result["degrees"])
        # print(f"x: {x}, y:{y}")
        set_wheels(result["degrees"])
        set_speed(result["degrees"], result["distance"])

    #c.close()
    # break
