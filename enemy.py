import pygame
from pygame.sprite import Sprite

import math

class Enemy(Sprite):
    def __init__(self, screen, image, start_x, start_y):
        super(Enemy,self).__init__()
        self.image = pygame.image.load(image)
        self.speed = 3
        self.x = start_x
        self.y = start_y
        self.screen = screen
        self.rect = self.image.get_rect()

    def update_me(self, the_player):
        dx = self.x - the_player.x
        dy = self.y - the_player.y
        dist = math.hypot(dx,dy)
        dx = dx / dist
        dy = dy / dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed
        self.rect.left = self.x
        self.rect.top = self.y

    def draw_me(self):
        self.screen.blit(self.image,[self.x,self.y])