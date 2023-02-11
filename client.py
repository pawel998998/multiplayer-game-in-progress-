import socket, threading, time, pickle, re
from Pgine import *

#######################################
lista_graczy_oprocz_mnie = []
lista_kordow_oprocz_mnie = []
#########################################
window(title="Client", size="500x500")

floor = obj(x=10, y=400, color="black", width=34, height=5)
player = obj(x=0, y=0, color="red", width=5, height=5)

player_x = 0
player_y = 0
#######################################
client_socket = socket.socket()
client_socket.connect(('localhost', 25565))

client_id = str(client_socket).split(" ")
client_id = int(client_id[6].replace(")", "").replace(",", ""))

#########################################
while True:
    data = pickle.loads(client_socket.recv(1024000))

    if key_down("w"):
        player_y -= 12
    if key_down("a"):
        player_x -= 6
    if key_down("d"):
        player_x += 6

    player_y += 6

    if hit(floor, player) == None:
        player_y -= 6

    try:
        index = data["id"].index(client_id)
        data["coordinates"][index] = obj_pos(player)
    except:
        pass
    
    set_pos(player, player_x, player_y)

    client_socket.send(pickle.dumps(data))

    for i in range(len(lista_graczy_oprocz_mnie)):
        try:
            a = obj(x=0, y=0, color="red", width=5, height=5)
            set_pos(a, x=lista_kordow_oprocz_mnie[i][0], y=lista_kordow_oprocz_mnie[i][1])
        except:
            pass

    try:
        lista_graczy_oprocz_mnie = data["id"]
        lista_graczy_oprocz_mnie.remove(client_id)
        lista_kordow_oprocz_mnie = data["coordinates"]
        lista_kordow_oprocz_mnie.remove(obj_pos(player)).remove(())
    except:
        pass

    refresh()
    time.sleep(0.016)
    try:
        kill_obj(a)
    except:
        pass

