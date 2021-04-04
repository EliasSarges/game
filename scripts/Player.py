import pygame
import math

from scripts.Weapon import Weapon


class Player:
    # construtod do player ------------------------------------------------------|
    def __init__(self, surface, path_img, path_img_weapon, speed, up=False, down=False, left=False, right=False):
        self.surface = surface
        self.sprite_img = pygame.image.load(path_img)
        self.rect_player = self.sprite_img.get_rect()

        # variaveis de controle de movimento ------------------------------------|
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        self.speed = speed

        self.path_img_weapon = path_img_weapon

        self.direction = 0

    def rotate_weapon(self):
        weapon = Weapon(self.surface, self.path_img_weapon,
                        self.rect_player.x, self.rect_player.y, self.direction)

        self.direction = weapon.draw()

    def draw(self):

        # muda a direcao do player de acordo com a variavel direction -------------|
        if self.direction == 0:
            self.surface.blit(pygame.transform.flip(
                self.sprite_img, True, False), self.rect_player)
        else:
            self.surface.blit(self.sprite_img, self.rect_player)

        self.rotate_weapon()
        self.move()

    # controle de movimento do jogador
    def move(self):
        if self.up:
            self.rect_player.y -= self.speed

        if self.down:
            self.rect_player.y += self.speed

        if self.left:
            self.rect_player.x -= self.speed

        if self.right:
            self.rect_player.x += self.speed
