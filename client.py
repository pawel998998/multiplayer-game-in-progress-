import socket, threading, time, json
from Pgine import *

#########################################

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 25565))

#########################################

while True:
    data = client_socket.recv(1024).decode()
    data = json.loads(data)
    data["player_pos"] = [1]
    data = json.dumps(data)
    client_socket.send(data.encode())



