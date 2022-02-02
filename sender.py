import socket
import json
s1 = {
    "degrees": 0,
    "distance": 0
}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 12345))
s.send(json.dumps(s1).encode())

