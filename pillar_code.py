import pygame
import  random
from time import sleep

class Pillar:
    def __init__(self, fb_game, location_counter):
        self.location_counter = location_counter
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        upper_pillar_height = random.randint(70, 530)
        lower_pillar_height = upper_pillar_height + 70
        self.upper_rect = pygame.Rect(0, 0, 40, upper_pillar_height)
        self.lower_rect = pygame.Rect(0, 0, 40, self.screen_rect.bottom - lower_pillar_height)
        self.set_initial_location()
        self.lower_rect.top = lower_pillar_height
        self.color = (0, 255, 0)
        self.border_colour = (0, 100, 0)

    def move(self):
        self.upper_rect.x -= 1
        self.lower_rect.x -= 1
        if self.upper_rect.right == 0 and self.lower_rect.right == 0:
            self.reset_pillar()

    def draw_pillar(self):
        pygame.draw.rect(self.screen, self.color, self.upper_rect)
        pygame.draw.rect(self.screen, self.border_colour, self.upper_rect, 3)
        pygame.draw.rect(self.screen, self.color, self.lower_rect)
        pygame.draw.rect(self.screen, self.border_colour, self.lower_rect, 3)

    def reset_pillar(self):
        upper_pillar_height = random.randint(70, 530)
        lower_pillar_height = upper_pillar_height + 70
        self.upper_rect = pygame.Rect(0, 0, 40, upper_pillar_height)
        self.lower_rect = pygame.Rect(0, 0, 40, self.screen_rect.bottom - lower_pillar_height)
        self.upper_rect.right = self.screen_rect.right
        self.lower_rect.right = self.screen_rect.right
        self.lower_rect.top = lower_pillar_height

    def check_collision(self, bird):
        bird_rect = pygame.Rect(bird.location[0], bird.location[1], bird.image_rect.w, bird.image_rect.h)
        if (self.upper_rect.colliderect(bird_rect) or self.lower_rect.colliderect(bird_rect)):
            return True
        else:
            return False

    def set_initial_location(self):
        self.upper_rect.right = 275 * self.location_counter
        self.lower_rect.right = 275 * self.location_counter




