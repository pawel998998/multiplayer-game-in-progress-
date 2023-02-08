import socket, threading, time
import pickle

#########################################

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 25565))

#########################################

while True:
    data = pickle.loads(client_socket.recv(1024))
    client_socket.send(pickle.dumps(data))
    time.sleep(0.1)
