import pygame
clock = pygame.time.Clock()
def fps():
    fps = 60
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

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