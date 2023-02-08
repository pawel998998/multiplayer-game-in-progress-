import socket
import _thread, threading
import time
import pickle

#########################################

clients = set()
clients_lock = threading.Lock()
s = socket.socket()
s.bind(("localhost", 25565))
s.listen()

#########################################

data = [1, 2, 3, 4, 5]

#########################################

def on_new_client(client,addr):
    global data
    with clients_lock:
        clients.add(client)
    while True:
        try:
            client.send(pickle.dumps(data))
            data = pickle.loads(client.recv(1024))
        except:
            print("Client left")
            break
        print(data)
        if not data:
            break
        else:
            with clients_lock:
                for c in clients:
                    try:
                        c.send(pickle.dumps(data))
                    except:
                        print("Client left")
                        break
    time.sleep(0.1)
#########################################

print("Server running.")
while True:
    conn, addr = s.accept()
    _thread.start_new_thread(on_new_client,(conn,addr))
