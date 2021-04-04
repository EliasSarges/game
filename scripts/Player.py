import pygame
import math


class Player:

    def __init__(self, surface, path_img, speed, direction=0, up=False, down=False, left=False, right=False):
        self.sprite_img = pygame.image.load(path_img)
        self.rect_player = self.sprite_img.get_rect()
        self.surface = surface

        self.up = up
        self.down = down
        self.left = left
        self.right = right

        self.speed = speed
        self.direction = 0

    def draw(self):
        self.surface.blit(self.sprite_img, self.rect_player)

    def move(self):
        if self.up:
            self.rect_player.y -= self.speed

        if self.down:
            self.rect_player.y += self.speed

        if self.left:
            self.rect_player.x -= self.speed

        if self.right:
            self.rect_player.x += self.speed
