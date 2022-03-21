import pygame

class Bird:
    def __init__(self, fb_game):
        self.screen = fb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('bird_image.png')
        self.image_rect = self.image.get_rect()
        self.moving_up = False

    def draw_bird(self):
        self.screen.blit(self.image, (200, 200))

    def move_bird(self):
        if self.moving_up:
            for n in range(20):
                self.image_rect.x -= 1



