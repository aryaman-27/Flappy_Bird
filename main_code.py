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
        self.bird1 = Bird(self,1)
        self.bird2 = Bird(self,2)
        self.bird3 = Bird(self,3)

    def run_game(self):
        while True:
            self.check_events()
            self.bird1.move_bird()
            self.bird2.move_bird()
            self.bird3.move_bird()
            self.update_screen()
            sleep(0.05)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird1.start_moving_up()
                elif event.key == pygame.K_SLASH:
                        self.bird2.start_moving_up()
                elif event.key == pygame.K_COMMA:
                    self.bird3.start_moving_up()

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.bird1.draw_bird()
        self.bird2.draw_bird()
        self.bird3.draw_bird()
        pygame.display.flip()

if __name__ == '__main__':
    fb = FlappyBird()
    fb.run_game()