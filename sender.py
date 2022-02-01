import socket
import json
s1 = {
    "degrees": 132,
    "distance": 0.5
}
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('', 12345))
s.send(json.dumps(s1).encode())

