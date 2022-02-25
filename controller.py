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


while True:
    c, addr = s.accept()
    print(f"Connected to {addr}")
    c.send("OK".encode())
    while (1):
        try:
            result = json.loads(c.recv(1024).decode())
            print(result)
        except:
            continue
        # x = result["distance"]*math.cos(result["degrees"])
        # y = result["distance"] * math.sin(result["degrees"])
        # print(f"x: {x}, y:{y}")
        motor.drive(result["degrees"], result["distance"])

    # c.close()
    # break
