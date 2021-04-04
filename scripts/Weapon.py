import pygame
import math


class Weapon():
    def __init__(self, surface, path_img_weapon, pos_x, pos_y):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.weapon_img = pygame.image.load(path_img_weapon)
        self.weapon_rect = self.weapon_img.get_rect(x=self.pos_x, y=self.pos_y)

    def rotate(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.dir_x = self.mouse_x - self.weapon_rect.centerx
        self.dir_y = self.mouse_y - self.weapon_rect.y
        self.angle = math.degrees(math.atan2(-self.dir_y, self.dir_x)) - 90

        self.rot_image = pygame.transform.rotate(self.weapon_img, self.angle)
        self.rot_image_rect = self.rot_image.get_rect()

        self.rot_image_rect.center = (self.pos_x + 60, self.pos_y + 50)

    def draw(self):
        self.rotate()
        # pygame.draw.rect(self.surface, 'red', self.rot_image_rect)
        self.surface.blit(
            self.rot_image, self.rot_image_rect)
