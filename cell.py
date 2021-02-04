import pygame
from settings import *
import random


class Cell:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.i = x // TILESIZE
        self.j = y // TILESIZE
        self.revelada = False
        self.bomba = False
        self.bombas_total = 8
        self.bombs_around = 0
        self.flag_enabled = False

    def reveal(self):
        self.revelada = True
        
        if self.bombs_around == 0:
            self.flood()

    def check_neighbours(self, grid):
        """
        This function will count how many bombs there is around a particular cell
        """
        if self.bomba:
            self.bombs_around = -1
            return

        total = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                i = self.i + x
                j = self.j + y
                if i > -1 and i < len(grid) and j > -1 and j < len(grid[1]):
                    neighbor = grid[i][j]

                    if neighbor.bomba:
                        total += 1
                        # debug
                        # print("ao redor de: ", self.i, self.j,
                        #       "tem uma bomba na posição: ", i, j, "total: ", total)
        self.bombs_around = total

    def flood(self):
        for x in range(-1, 2):
            for y in range(-1, 2):
                i = self.i + x
                j = self.j + y
                if i > -1 and i < len(self.game.grid) and j > -1 and j < len(self.game.grid[1]):
                    neighbor = self.game.grid[i][j]

                    if not neighbor.revelada:
                        neighbor.reveal()
                        
    def enable_flag(self):
        self.flag_enabled = not self.flag_enabled
        

    def draw_number(self):
        font = pygame.font.Font("data/JetBrainsMono-Bold.ttf", 24)
        if self.bombs_around > 0 and self.revelada:
            text = font.render(
                str(self.bombs_around), False, (0, 0, 0))
            self.game.screen.blit(text, (self.x + 12, self.y))

    def set_bomb(self):
        """
        This function will turn this cell into a cell with a bomb 
        (just to keep organized)
        """
        self.bomba = True

    def draw_cell(self):

        pygame.draw.rect(
            self.game.screen, WHITE, (self.x, self.y, TILESIZE - 1, TILESIZE - 1))

        if self.revelada:
            if self.bomba:
                pygame.draw.rect(
                    self.game.screen, RED, (self.x + 10, self.y + 10, TILESIZE - 23, TILESIZE - 23))
        else:
            pygame.draw.rect(
                self.game.screen, GRAY, (self.x, self.y, TILESIZE - 1, TILESIZE - 1))

    def get_mouse_pos(self):
        mouse = pygame.mouse.get_pos()

        return [mouse[0] // TILESIZE, mouse[1] // TILESIZE]
