import pygame
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Flag(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(
            img_folder, "flag.png")).convert_alpha()
        self.rect = self.image.get_rect()
    
    def draw(self):
        pass