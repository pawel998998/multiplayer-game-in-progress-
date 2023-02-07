import socket, threading
from Pgine import *

client_socket = socket.socket()
client_socket.connect(('localhost', 25565))

def multiplayer():
    while True:
        data = client_socket.recv(1024).decode()
        data = json.loads(data)
        client_socket.send(data).encode()
        data["player_pos"] = [0, 0]


threading.Thread(target=multiplayer).start()







