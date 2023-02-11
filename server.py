import socket, pickle, time, _thread, threading

#########################################
data = {
    "id": [],
    "coordinates": [],
}

#########################################

clients = set()
clients_lock = threading.Lock()
s = socket.socket()
s.bind(("0.0.0.0", 25565))
s.listen(10)

#########################################
def on_new_client(client,addr):
    global data
    with clients_lock:
        clients.add(client)
    while True:
        if () not in data["coordinates"]:
            data["coordinates"].append(())
        try:
            client.send(pickle.dumps(data))
            data = pickle.loads(client.recv(100000))
            print(data)
        except:
            while True:
                break
            print(f"{addr[1]} left.")
            break
        if not data:
            break
        else:
            with clients_lock:
                for c in clients:
                    try:
                        c.send(pickle.dumps(data))
                    except:
                        break
    #time.sleep(0.016)
#########################################

print("Server running.")
while True:
    conn, addr = s.accept()
    _thread.start_new_thread(on_new_client,(conn,addr))

