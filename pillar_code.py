import pygame
import  random
from time import sleep

class Pillar:
    def __init__(self, fb_game, location_counter):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.upper_pillar_y = random.randint(50, 550)
        self.lower_pillar_y = self.upper_pillar_y + 50
        self.upper_rect = pygame.Rect(0, 0, 40, self.upper_pillar_y)
        self.lower_rect = pygame.Rect(0, 0, 40, 600 - self.lower_pillar_y)
        self.upper_rect.right = 250 * location_counter
        self.lower_rect.right = 250 * location_counter
        self.lower_rect.top = self.lower_pillar_y
        self.color = (0, 255, 0)
        self.border_colour = (0, 100, 0)

    def move(self):
        self.upper_rect.x -= 1
        self.lower_rect.x -= 1
        if self.upper_rect.right == 0 and self.lower_rect.right == 0:
            self.upper_rect.right = 800
            self.lower_rect.right = 800

    def draw_pillar(self):
        pygame.draw.rect(self.screen, self.color, self.upper_rect)
        pygame.draw.rect(self.screen, self.border_colour, self.upper_rect, 3)
        pygame.draw.rect(self.screen, self.color, self.lower_rect)
        pygame.draw.rect(self.screen, self.border_colour, self.lower_rect, 3)



