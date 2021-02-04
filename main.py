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

        for bomb_to_set in range(self.grid[0][0].bombas_total):
            random_x = random.randrange(0, len(self.grid[1]))
            random_y = random.randrange(0, len(self.grid))

            # setting a random place to be a bomb
            self.grid[random_x][random_y].set_bomb()

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].check_neighbours(self.grid)

    def update(self):
        """
        gets the coordinates of the array where the mouse is
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pos = self.grid[i][j].get_mouse_pos()
                self.grid[pos[0]][pos[1]].revelada = True

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


pygame.init()
game = Game("Minesweeper", 400, 400)  # make this responsive later

game.setup()
while not game.done:
    game.event_loop()
    game.update()
    game.draw()
