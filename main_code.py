import sys

import pygame
from  bird_code import Bird
from  time import sleep

class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption('Flappy Bird')
        self.background = pygame.image.load('Flappy_bird_background.png')
        self.bird = Bird(self)

    def run_game(self):
        while True:
            self.check_events()
            self.bird.move_bird()
            self.update_screen()
            sleep(0.01)
            self.bird.bird_direction = 0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.bird_direction = 1
                    self.bird.move_bird()

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.draw_bird()
        pygame.display.flip()

if __name__ == '__main__':
    fb = FlappyBird()
    fb.run_game()