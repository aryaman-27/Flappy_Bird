import pygame
from  time import sleep

class Bird:
    def __init__(self, fb_game):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('bird_image.png')
        self.image_rect = self.image.get_rect()
        self.bird_direction = 0

        self.location = [200, 200]

    def draw_bird(self):
        self.screen.blit(self.image, self.location)

    def move_bird(self):
        if self.bird_direction == 1:
            for n in range(20):
                self.location[1] -= 1
                sleep(0.01)
                self.draw_bird()
                pygame.display.flip()

        else:
            self.location[1] += 1




