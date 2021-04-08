import pygame
import math


class Player:
    # construtod do player ------------------------------------------------------|
    def __init__(self, surface, path_img, path_img_weapon, speed, up=False, down=False, left=False, right=False):
        self.surface = surface

        self.path_img = path_img
        self.sprite_img = pygame.image.load(path_img)
        self.rect_player = self.sprite_img.get_rect(center=(300, 300))

        self.weapon_img = pygame.image.load(path_img_weapon)
        self.weapon_rect = self.weapon_img.get_rect(
            x=self.rect_player.x, y=self.rect_player.y)

        # variaveis de controle de movimento ------------------------------------|
        self.up = up
        self.down = down
        self.left = left
        self.right = right

        self.speed = speed

        self.path_img_weapon = path_img_weapon

        self.direction = 0



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

    def rotate_weapon(self):
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
            self.direction = 1
            self.rot_image_rect.center = (
                self.rect_player.x + 75, self.rect_player.y + 40)
        else:
            self.direction = 0
            self.rot_image_rect.center = (
                self.rect_player.x - 15, self.rect_player.y + 40)

        self.weapon_rect = self.rect_player

    def draw(self):
        # pygame.draw.rect(self.surface,  'red', self.rect_player)
        # muda a direcao do player de acordo com a variavel direction -------------|
        if self.direction == 0:
            self.surface.blit(pygame.transform.flip(
                self.sprite_img, True, False), self.rect_player)
        else:
            self.surface.blit(self.sprite_img, self.rect_player)

        # desenha na tela a arma
        self.surface.blit(
            self.rot_image, self.rot_image_rect)

    def melee_circle_attack(self):
        pygame.draw.circle(self.surface, 'red',
                           (self.rect_player.x + (self.rect_player.width // 2), self.rect_player.y + (self.rect_player.height // 2)), 100)
