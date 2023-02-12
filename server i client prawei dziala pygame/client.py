import socket, threading, time, pickle, re
import sys, pygame

#######################################
lista_graczy_oprocz_mnie = []
lista_kordow_oprocz_mnie = []
fps = 60
#########################################
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

player = pygame.Rect(0, 0, 100, 100)
floor = pygame.Rect(0, 400, 900, 100)
#########################################
def draw():
    global floor, player
    screen.fill((0, 0, 0))
    floor = pygame.draw.rect(screen, (0, 255, 0), floor)
    player = pygame.draw.rect(screen, (255, 255, 255), player)
    for i in range(len(lista_graczy_oprocz_mnie)):
        i = pygame.draw.rect(screen, (255, 0, 0), (pygame.Rect(lista_kordow_oprocz_mnie[i][0], lista_kordow_oprocz_mnie[i][1], 100, 100)))
    pygame.display.update()

def hit(obj1, obj2):
    x_obj1 = obj1.x
    y_obj1 = obj1.y
    height_obj1 = obj1.height
    width_obj1 = obj1.width
    x_obj2 = obj2.x
    y_obj2 = obj2.y
    height_obj2 = obj2.height
    width_obj2 = obj2.width
    if y_obj1+height_obj1 > y_obj2 and x_obj1 > x_obj2-width_obj1 and x_obj1 < x_obj2+width_obj2 and y_obj1 < y_obj2+height_obj1:
        touching = True
        return touching
    else:
        touching = False
        return touching
#######################################
client_socket = socket.socket()
client_socket.connect(('localhost', 25565))

client_id = str(client_socket).split(" ")
client_id = int(client_id[6].replace(")", "").replace(",", ""))

#########################################
while True:
    data = pickle.loads(client_socket.recv(1024000))

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= 20
    if keys[pygame.K_a]:
        player.x -= 10
    if keys[pygame.K_d]:
        player.x += 10

    player.y += 10

    if hit(player, floor) == True:
        player.y -= 10

    draw()

    try:
        index = data["id"].index(client_id)
        data["coordinates"][index] = (player.x, player.y)
    except:
        pass

    client_socket.send(pickle.dumps(data))

    try:
        lista_graczy_oprocz_mnie = data["id"]
        lista_graczy_oprocz_mnie.remove(client_id)
        lista_kordow_oprocz_mnie = data["coordinates"]
        lista_kordow_oprocz_mnie.remove((player.x, player.y)).remove(())
    except:
        pass



