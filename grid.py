import pygame
from settings import *


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cols = self.width // TILESIZE
        self.rows = self.height // TILESIZE
        self.grid = []
    

    def make_grid(self):
        for i in range(self.cols):
            self.grid.append([])
            for j in range(self.rows):
                self.grid[i].append(0)
        return self.grid
    
