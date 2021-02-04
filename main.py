import pygame
from pygame.locals import *
from settings import *

from grid import *
from cell import *


class Game:
    def __init__(self, title, width, height):
        self.title = pygame.display.set_caption(title)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.done = False

    def setup(self):
        """
        Function for class instances and other stuff
        """

        # obtem o array 2D criado na classe Grid
        self.grid = Grid(self.width, self.height).make_grid()

        """
        Instantiating new cells for every place in grid
        """

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = Cell(self, i * TILESIZE, j * TILESIZE)

        """
        All of this code is necessary to make a random position for the bombs
        because if you don't do it this way, a new bomb would appear in the same spot an old bomb was, overwritting it
        """
        random_x = random.sample(
            range(0, len(self.grid)), self.grid[0][0].bombas_total)
        random_y = random.sample(
            range(0, len(self.grid[1])), self.grid[0][0].bombas_total)

        for pos in range(self.grid[0][0].bombas_total):
            self.grid[random_x[pos]][random_y[pos]].set_bomb()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].check_neighbours(self.grid)


    def mouse_update(self, button):
        """
        gets the coordinates of the array where the mouse is
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pos = self.grid[i][j].get_mouse_pos()
        if button == 1:
            self.grid[pos[0]][pos[1]].reveal()
        if button == 3:
            self.grid[pos[0]][pos[1]].enable_flag()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

        """
        draws the Cell objects individually
        """

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].draw_cell()
                self.grid[i][j].draw_number()

        pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.mouse_update(button=3)
                else:
                    self.mouse_update(button=1)


pygame.init()
game = Game("Minesweeper", 400, 400)  # make this responsive later

game.setup()
while not game.done:
    game.event_loop()
    game.update()
    game.draw()
