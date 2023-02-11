import socket, threading, time, pickle, re
from Pgine import *

#######################################

client_socket = socket.socket()
client_socket.connect(('localhost', 25565))

client_id = str(client_socket).split(" ")
client_id = int(client_id[6].replace(")", "").replace(",", ""))

#########################################
window(title="Client", size="1280x720")

floor = obj(x=10, y=600, color="black", width=70, height=5)
player = obj(x=50, y=0, color="red", width=5, height=5)

player_x = 50
player_y = 0

lista_graczy_oprocz_mnie = []
lista_kordow_oprocz_mnie = []
#########################################



while True:
    data = pickle.loads(client_socket.recv(1024))

    if key_down("w"):
        player_y -= 12
    if key_down("a"):
        player_x -= 6
    if key_down("d"):
        player_x += 6


    if hit(floor, player) == None:
        player_y -= 6

    player_y += 6

    try:
        index = data["id"].index(client_id)
        data["coordinates"][index] = obj_pos(player)
    except:
        pass
    
    set_pos(player, player_x, player_y)

    client_socket.send(pickle.dumps(data))

    try:
        lista_graczy_oprocz_mnie = data["id"]
        lista_graczy_oprocz_mnie.remove(client_id)
    except:
        pass

    try:
        lista_kordow_oprocz_mnie = data["coordinates"]
        lista_kordow_oprocz_mnie.remove(obj_pos(player)).remove(())
    except:
        pass


    refresh()
    time.sleep(0.016)

