import pygame
import  random
from time import sleep

class Pillar:
    def __init__(self, fb_game):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.upper_pillar_y = random.randint(0, 770)
        self.lower_pillar_y = self.upper_pillar_y + 30
        self.upper_rect = pygame.Rect(0, 0, 20, self.upper_pillar_y)
        self.lower_rect = pygame.Rect(0, 0, 20, 600 - self.lower_pillar_y)
        self.upper_rect.right = 800
        self.lower_rect.right = 800
        self.lower_rect.top = self.lower_pillar_y
        self.color = (255, 255, 0)

    def update(self):
        self.upper_rect.x -= 1
        self.lower_rect.x -= 1

    def draw_pillar(self):
        pygame.draw.rect(self.screen, self.color, self.upper_rect)
        pygame.draw.rect(self.screen, self.color, self.lower_rect)


