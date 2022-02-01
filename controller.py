import socket
import json
import math

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
    if degrees > 180:
        print(f"go backward")

    elif degrees < 180:
        print(f"go forward")

    else:
        print(f"stop")


while True:
    c, addr = s.accept()
    print(f"Connected to {addr}")
    c.send("OK".encode())
    result = json.loads(c.recv(1024).decode())
    # x = result["distance"]*math.cos(result["degrees"])
    # y = result["distance"] * math.sin(result["degrees"])
    # print(f"x: {x}, y:{y}")
    set_wheels(result["degrees"])
    set_speed(result["degrees"], result["distance"])

    c.close()
    # break
