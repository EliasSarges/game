import pygame
import math


class Weapon():
    # construtor da Weapon -------------------------------------------------|
    def __init__(self, surface, path_img_weapon, pos_x, pos_y, direction):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.weapon_img = pygame.image.load(path_img_weapon)
        self.weapon_rect = self.weapon_img.get_rect(x=self.pos_x, y=self.pos_y)
        self.direction = direction

    # desenha e rotaciona a arma -------------------------------------------|
    def draw(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.dir_x = self.mouse_x - self.weapon_rect.centerx
        self.dir_y = self.mouse_y - self.weapon_rect.centery

        self.angle = int(math.degrees(
            math.atan2(-self.dir_y, self.dir_x)) - 90)

        self.rot_image = pygame.transform.rotate(
            self.weapon_img,  self.angle)

        # cria o retangulo com base na imagem ------------------------------|
        self.rot_image_rect = self.rot_image.get_rect()

        # define a direcao do player de acordo com a posicao do mouse ------|
        if self.angle <= 0 and self.angle >= -180:
            self.rot_image_rect.center = (self.pos_x + 65, self.pos_y + 55)
            self.direction = 1
        else:
            self.rot_image_rect.center = (self.pos_x - 15, self.pos_y + 55)
            self.direction = 0

        # desenha na tela a arma
        self.surface.blit(
            self.rot_image, self.rot_image_rect)

        return self.direction
