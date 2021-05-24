import pygame
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)

# grid
TILESIZE = 40  # dont change this

# sounds
pygame.mixer.init()
EFFECT = pygame.mixer.Sound('sounds/explosion.ogg')
EFFECT.set_volume(0.2)
TADA = pygame.mixer.Sound('sounds/tada.wav')
TADA.set_volume(0.5)

pygame.font.init()
font = pygame.font.Font("fonts/JetBrainsMono-Bold.ttf", 32)
