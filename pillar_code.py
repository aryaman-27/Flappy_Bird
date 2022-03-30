import pygame
from time import sleep

class Pillar:
    def __init__(self, fb_game):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, 20, 600)
        self.rect.right = 800
        self.color = (255, 255, 0)

    def update(self):
        self.rect.x -= 1

    def draw_pillar(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
