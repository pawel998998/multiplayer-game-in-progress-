import socket, threading, time, pickle, re
import sys, pygame

#######################################
player_ids_except_me = []
player_coords_except_me = []
fps = 60
#########################################
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))


floor_x = 0
floor_y = 600
direction = None

floor = pygame.Rect(floor_x, floor_y, 900, 100)
player = pygame.Rect(500, 500, 100, 100)
#########################################
def draw():
    global floor, player, a, cam_poz_y, cam_poz_x
    screen.fill((0, 0, 0))
    floor = pygame.draw.rect(screen, (0, 255, 0), floor)
    player = pygame.draw.rect(screen, (255, 255, 255), player)
    floor = pygame.Rect(floor_x, floor_y, 900, 100)
    player = pygame.Rect(500, 500, 100, 100)

    cam_poz_x = ((floor_x)*(-1))+500
    cam_poz_y = (floor_y-1090)*(-1)
    try:
        for i in range(len(player_ids_except_me)):
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_coords_except_me[i][0], player_coords_except_me[i][1], 100, 100))
    except Exception as e:
        print(e)

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
client_socket.connect(('192.168.0.62', 25565))

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
        floor_y += 20
    if keys[pygame.K_a]:
        floor_x += 10
    if keys[pygame.K_d]:
        floor_x -= 10
        

    floor_y -= 10
    

    if hit(player, floor) == True:
        floor_y += 10

    draw()


    try:
        index = data["id"].index(client_id)
        data["coordinates"][index] = (cam_poz_x, cam_poz_y)
    except:
        pass

    client_socket.send(pickle.dumps(data))

    try:
        player_ids_except_me = data["id"]
        player_ids_except_me.remove(client_id)
        player_coords_except_me = data["coordinates"]
        player_coords_except_me.remove(player.x, player.y).remove(())
    except:
        pass



