import sys
import pygame

from scripts.Player import Player

pygame.init()
clock = pygame.time.Clock()

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Jogo01")

# instancia do player
player = Player(screen, "assets/sprites/player.png",
                "assets/sprites/sword.png", 3)

# game loop ----------------------------------------------------|
while True:
    screen.fill('#333333')
    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # ao pressionar uma tecla ------------------------------|
        if event.type == pygame.KEYDOWN:
            if(event.key == 119):
                player.up = True

            if(event.key == 115):
                player.down = True

            if(event.key == 97):
                player.left = True
                player.direction = 0

            if(event.key == 100):
                player.right = True
                player.direction = 1

        # ao soltar uma tecla -----------------------------------|
        if event.type == pygame.KEYUP:
            if(event.key == 119):
                player.up = False

            if(event.key == 115):
                player.down = False

            if(event.key == 97):
                player.left = False

            if(event.key == 100):
                player.right = False

    pygame.display.flip()
    clock.tick(60)


"""
    W = 119
    S = 115
    A = 97
    D = 100
"""
