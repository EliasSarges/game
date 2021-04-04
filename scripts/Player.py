import pygame


class Player:

    def __init__(self, surface, path_img, up=False, down=False, left=False, right=False):
        self.sprite_img = pygame.image.load(path_img)
        self.rect_player = self.sprite_img.get_rect()
        self.surface = surface
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def move(self):
        if self.up:
            self.rect_player.y += -2

        if self.down:
            self.rect_player.y += 2

        if self.left:
            self.rect_player.x += -2

        if self.right:
            self.rect_player.x += 2

    def draw(self):
        self.surface.blit(self.sprite_img, self.rect_player)
