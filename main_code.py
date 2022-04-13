import sys

import pygame
from  bird_code import Bird
from pillar_code import Pillar
from  time import sleep

class FlappyBird:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_rect = self.screen.get_rect()

        pygame.display.set_caption('Flappy Bird')
        self.background = pygame.image.load('Flappy_bird_background.png')
        self.bird = Bird(self)
        self.pillar = Pillar(self, 2)
        self.pillar_2 = Pillar(self, 3)
        self.pillar_3 = Pillar(self,4)
        self.pillars = [self.pillar, self.pillar_2, self.pillar_3]

    def run_game(self):
        while True:
            self.check_events()
            self.bird.move_bird()
            for pillar in self.pillars:
                pillar.move()
            collision_status = self.pillar.check_collision(self.bird) or self.pillar_2.check_collision(self.bird) or self.pillar_3.check_collision(self.bird)
            if collision_status:
                sleep(0.5)
                self.initalise_game()
            self.update_screen()
            sleep(0.01)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.start_moving_up()

    def initalise_game(self):
        self.bird.image_rect.topleft = self.bird.initial_location
        self.pillar.upper_rect.right = 275 * 2
        self.pillar.lower_rect.right = 275 * 2
        self.pillar_2.upper_rect.right = 275 * 3
        self.pillar_2.lower_rect.right = 275 * 3
        self.pillar_3.upper_rect.right = 275 * 4
        self.pillar_3.lower_rect.right = 275 * 4

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.bird.draw_bird()
        for pillar in self.pillars:
            pillar.draw_pillar()
        pygame.display.flip()


if __name__ == '__main__':
    fb = FlappyBird()
    fb.run_game()