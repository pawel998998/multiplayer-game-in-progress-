import pygame
from func import *

pygame.init()
screen = pygame.display.set_mode((500, 500))

#######################

player_x = 0
player_y = 390

jumping = False
player_speed = 5
Y_GRAVITY = 0.5
JUMP_HEIGHT = 10
Y_VELOCITY = 0

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

    if hit(player, floor) == True:
        jumping = False
        Y_VELOCITY = 0
        player_y = floor.top - player.height

    if hit(player, floor2) == True:
        jumping = False
        Y_VELOCITY = 0
        player_y = floor2.top - player.height

    if not hit(player, floor) and not hit(player, floor2):
        jumping = True

    if jumping:
        Y_VELOCITY += Y_GRAVITY
        player_y += Y_VELOCITY

        if hit(player, floor):
            jumping = False
            Y_VELOCITY = 0
            player_y = floor.top - player.height

        if hit(player, floor2):
            jumping = False
            Y_VELOCITY = 0
            player_y = floor2.top - player.height

    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w] and not jumping:
        jumping = True
        Y_VELOCITY = -JUMP_HEIGHT
    if not keys[pygame.K_w]:
        jumping = False

    screen.fill((0, 0, 0))
    floor = pygame.Rect(0, 400, 500, 10)
    floor = pygame.draw.rect(screen, (0, 255, 0), floor)
    floor2 = pygame.Rect(250, 300, 100, 100)
    floor2 = pygame.draw.rect(screen, (0, 0, 255), floor2)
    player = pygame.Rect(player_x, player_y, 40, 40)
    player = pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.display.update()
