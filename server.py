import socket
import _thread, threading
import json, time

#########################################

clients = set()
clients_lock = threading.Lock()
s = socket.socket()
s.bind(("localhost", 25565))
s.listen()

#########################################

data = {
    "player_id": [],
    "player_pos": [],
    "total_players": 0,
    "player_ip": []
}

#########################################

def on_new_client(client,addr):
    global data
    with clients_lock:
        clients.add(client)
  
    while True:
        client.send(json.dumps(data).encode())
        data = client.recv(1024).decode()
        data = json.dumps(data)
        print(data)
        if not data:
            break
        else:
            with clients_lock:
                for c in clients:
                    client.send(json.dumps(data).encode())

#########################################

print("Server running.")
while True:
    conn, addr = s.accept()
    _thread.start_new_thread(on_new_client,(conn,addr))

