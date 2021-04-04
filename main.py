import pygame
import sys
from scripts.Player import Player

# instancia da lib Pygame
pygame.init()
clock = pygame.time.Clock()

WINDOW_SIZE = (640, 480)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Jogo01")  # Mudando nome e icone da janela do jogo

player = Player(screen, "assets/sprites/player.png", 3)

# loop principal do jogo
while True:
    screen.fill('#333333')  # preenchendo a tela do jogo com a cor #333333

    player.draw()
    player.move()

    # evento de saida do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # ao pressionar uma tecla
        if event.type == pygame.KEYDOWN:
            if(event.key == 119):
                player.up = True

            if(event.key == 115):
                player.down = True

            if(event.key == 97):
                player.left = True

            if(event.key == 100):
                player.right = True

        # ao soltar uma tecla
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
