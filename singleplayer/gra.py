import pygame
#######################
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
def fps():
    fps = 60
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
#######################
player_x = 0
player_y = 400

jumping = False
player_speed = 3
Y_GRAVITY = 0.5
JUMP_HEIGHT = 10
Y_VELOCITY = 0
#######################
floor = pygame.Rect(0, 400, 500, 10)
floor2 = pygame.Rect(250, 300, 100, 100)
player = pygame.Rect(player_x, player_y, 40, 40)
#######################
while True:
    fps()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not jumping:
        jumping = True
        Y_VELOCITY = -JUMP_HEIGHT

    if player.colliderect(floor) == True:
        jumping = False
        Y_VELOCITY = 0
        player_y = floor.top - player.height

    if player.colliderect(floor2) == True:
        jumping = False
        player_y = floor2.top - player.height
        Y_VELOCITY = 0

    if not player.colliderect(floor) and not player.colliderect(floor2):
        jumping = True

    if jumping:
        Y_VELOCITY += Y_GRAVITY
        player_y += Y_VELOCITY

    if keys[pygame.K_a]:
        player_x -= player_speed

    if keys[pygame.K_d]:
        player_x += player_speed

    print(player.right)

    screen.fill((0, 0, 0))
    floor = pygame.Rect(0, 400, 500, 10)
    floor = pygame.draw.rect(screen, (0, 255, 0), floor)
    floor2 = pygame.Rect(250, 350, 100, 50)
    floor2 = pygame.draw.rect(screen, (0, 0, 255), floor2)
    player = pygame.Rect(player_x, player_y, 40, 40)
    player = pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.update()

