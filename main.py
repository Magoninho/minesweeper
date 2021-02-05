import pygame
from pygame.locals import *
from settings import *

from grid import *
from cell import *
from flag import *


# output : True

class Game:
    def __init__(self, title, width, height):
        self.title = pygame.display.set_caption(title)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.done = False  # game loop condition
        self.is_game_over = False
        self.score = 0
        self.have_won = False

    def setup(self):
        """
        Function for class instances and other stuff
        """
        self.flag = Flag(self)

        # gets the grid from the Grid class
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

        available = []  # an array to receive all positions available
        # get all positions in grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # appending all positions available in the grid
                available.append([i, j])

        # picks a random position FROM the available array

        for pos in range(self.grid[0][0].bombas_total):
            random_index = random.randrange(len(available))
            random_x = available[random_index][0]
            random_y = available[random_index][1]

            self.grid[random_x][random_y].set_bomb()
            available.remove([random_x, random_y])

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].check_neighbours(self.grid)

    def mouse_update(self, button):
        """
        gets the coordinates of the array where the mouse is
        """
        spots = []
        conditions = []

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                pos = self.grid[i][j].get_mouse_pos()
        if button == 1:
            self.grid[pos[0]][pos[1]].reveal()

            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if not self.grid[i][j].bomba:
                        # the spots that doesn't have bombs
                        spots.append([i, j])
                        conditions.append(self.grid[i][j].revelada)
            if all(conditions):
                for i in range(len(self.grid)):
                    for j in range(len(self.grid[i])):
                        if self.grid[i][j].bomba:
                            if not self.grid[i][j].flag_enabled:
                                self.grid[i][j].enable_flag()
                self.win()

        if button == 3:
            self.grid[pos[0]][pos[1]].enable_flag()

    def update(self):
        pass

    def gameover(self):
        if self.is_game_over:
            text = font.render(
                "u lost lmao", False, (RED))
            self.screen.blit(text, (self.width // 5, self.height // 3))

    def draw_win_text(self):
        text2 = font.render(
            "you won!!!!!!!!!!!!!!!!!!!!", False, (BLUE))
        self.screen.blit(text2, (self.width // 5, self.height // 3))

    def win(self):
        self.have_won = True
        print("ganhaste")

    def draw(self):
        self.screen.fill(BLACK)

        """
        draws the Cell objects individually
        """

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].draw_cell()
                self.grid[i][j].draw_number()

        self.gameover()

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
