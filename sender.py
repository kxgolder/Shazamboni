import socket
import json
from time import sleep
s1 = {
    "degrees": 90 ,
    "distance": 0
}
s2 = {
    "degrees": 270 ,
    "distance": 0
}
s3 = {
    "degrees": 0 ,
    "distance": 0
}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 12345))
packet = json.dumps(s1).encode()
packet2 = json.dumps(s2).encode()
packet3 = json.dumps(s3).encode()
print(packet)
s.send(packet)
sleep(1)
print(packet2)
s.send(packet2)
sleep(1)
print(packet3)
s.send(packet3)
sleep(1)

