import pygame
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Flag(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            img_folder, "flag.png")).convert_alpha(), (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
    
    def draw(self, screen, x, y):
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, self.rect)
