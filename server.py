import socket
import _thread, threading
import json

clients = set()
clients_lock = threading.Lock()

s = socket.socket()
s.bind(("localhost", 25565))
s.listen(1)

player_data= {
    "player_id": [],
    "player_pos": [],
    "total_players": 0,
    "player_ip": []
}

def on_new_client(client,addr):

    with clients_lock:
        clients.add(client)
        player_data["player_id"].append(addr[1])
        player_data["player_ip"].append(addr[0])
        player_data["total_players"] = len(player_data["player_id"])
        data = json.dumps(player_data)
        print(player_data)
    try:    
        while True:
            try:
                recived_data = client.recv(1024).decode()
            except ConnectionResetError:
                try:
                    player_data["player_id"].remove(addr[1])
                    player_data["player_ip"].remove(addr[0])
                    player_data["total_players"] -= 1
                    print(player_data)
                except:
                    pass
            try:
                if not recived_data:
                    break
                else:
                    with clients_lock:
                        for c in clients:
                            client.send(data.encode())
            except UnboundLocalError:
                try:    
                    player_data["player_id"].remove(addr[1])
                    player_data["player_ip"].remove(addr[0])
                    player_data["total_players"] -= 1
                    print(player_data)

                except:
                    pass
    finally:
        with clients_lock:
            client.close()

print("Server running.")

print(player_data)

while True:
    conn, addr = s.accept()
    _thread.start_new_thread(on_new_client,(conn,addr))
