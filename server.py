import socket, pickle, time, _thread, threading

#########################################
data = {
    "id": [],
    "coordinates": []
}
#########################################
s = socket.socket()
s.bind(("0.0.0.0", 25565))
s.listen()
#########################################
def new_client(client,addr):
    global data
    while True:
        try:
            client.send(pickle.dumps(data))
            data = pickle.loads(client.recv(1024000))
        except:
            index = data["id"].index(addr[1])
            data["coordinates"].remove(data["coordinates"][index])
            data["id"].remove(addr[1])
            print(f"Player {addr[1]} left.")
            break
        time.sleep(0.016)
#########################################
def petla_print():
    while True:
        if () not in data["coordinates"]:
            data["coordinates"].append(())
        print(data)

_thread.start_new_thread(petla_print, ())
#########################################
print("Server running.")
while True:
    conn, addr = s.accept()
    data["id"].append(addr[1])
    _thread.start_new_thread(new_client,(conn,addr))


