# GitHub:
# https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_rotate_towards_target.md
#
# Stack Overflow:
# https://stackoverflow.com/questions/58603835/how-to-rotate-an-imageplayer-to-the-mouse-direction/58604116#58604116

import math
import pygame

pygame.init()
window = pygame.display.set_mode((300, 300))
player = pygame.transform.smoothscale(
    pygame.image.load("./assets/sprites/sword.png").convert_alpha(), (100, 100))

#   0 - image is looking to the right
#  90 - image is looking up
# 180 - image is looking to the left
# 270 - image is looking down
correction_angle = 90

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player_pos = window.get_rect().center
    player_rect = player.get_rect(center=player_pos)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    direction_x, direction_y = mouse_x - \
        player_rect.centerx, mouse_y - player_rect.centery
    angle = math.degrees(
        math.atan2(-direction_y, direction_x)) - correction_angle

    rot_image = pygame.transform.rotate(player, angle)
    rot_image_rect = rot_image.get_rect(center=player_rect.center)

    window.fill((255, 255, 255))
    window.blit(rot_image, rot_image_rect.topleft)
    pygame.display.flip()

pygame.quit()
exit()
