import pygame
from  time import sleep

class Bird:
    def __init__(self, fb_game):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('bird_image.png')
        self.image_rect = self.image.get_rect()
        self.bird_direction = 0
        self.up_counter = 0
        self.initial_location = [200, 200]
        self.location = [200, 200]
        self.bird_out_of_screen = False

    def draw_bird(self):
        self.screen.blit(self.image, (self.location))

    def move_bird(self):
        if self.bird_direction == 1 and self.up_counter < 20:
            self.location[1] -= 1.5
            self.up_counter += 1

        elif self.bird_direction == 1 and self.up_counter >= 20 and self.up_counter < 30:
            self.location[1] -= 0.75
            self.up_counter += 1

        else:
            self.up_counter = 0
            self.bird_direction = 0
            self.location[1] += 1.5
        return

    def start_moving_up(self):
        self.bird_direction = 1
        self.up_counter = 0
        return

    def bird_detect(self):
        if self.location[1] >= self.screen_rect.bottom or self.location[1] <= self.screen_rect.top:
            self.bird_out_of_screen = True

    def reset_bird(self):
        self.location[1] = self.initial_location[1]

