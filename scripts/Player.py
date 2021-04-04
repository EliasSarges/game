import pygame
import math

from scripts.Weapon import Weapon


class Player:

    def __init__(self, surface, path_img, path_img_weapon, speed, direction, up=False, down=False, left=False, right=False):
        self.sprite_img = pygame.image.load(path_img)
        self.rect_player = self.sprite_img.get_rect()
        self.surface = surface

        self.up = up
        self.down = down
        self.left = left
        self.right = right

        self.direction = direction

        self.speed = speed

        self.path_img_weapon = path_img_weapon

    def rotate_weapon(self):
        weapon = Weapon(self.surface, self.path_img_weapon,
                        self.rect_player.x, self.rect_player.y)
        weapon.draw()

    def draw(self):
        self.surface.blit(self.sprite_img, self.rect_player)
        self.rotate_weapon()
        self.move()

    def move(self):
        if self.up:
            self.rect_player.y -= self.speed

        if self.down:
            self.rect_player.y += self.speed

        if self.left:
            self.rect_player.x -= self.speed
            self.sprite_img = pygame.transform.flip(
                self.sprite_img, True, False)

        if self.right:
            self.rect_player.x += self.speed
