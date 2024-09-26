import pygame
from config import *
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = ROWS
        self.num_cols = COLUMNS
        self.cell_size = CELL_SIZE
        self.grid = []
        self.reset_grid()
        self.colors = Colors.get_cell_colors()
        
    def __str__(self):
        result_str = ""
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                result_str += f"{self.grid[row][col]}  "
            result_str += f"\n"

        return result_str

    def reset_grid(self):
        self.grid = [[0 for j in range (self.num_cols)] for i in range(self.num_rows)]

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0 # Why not use the clear_row method?

    def clear_full_rows(self)        :
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cell_value = self.grid[row][col]
                
                x = col*self.cell_size + BORDER_WIDTH + GRID_PADDING
                y = row*self.cell_size + BORDER_WIDTH + GRID_PADDING
                w = self.cell_size - BORDER_WIDTH
                h = self.cell_size - BORDER_WIDTH
                cell_value = self.grid[row][col]
                cell_color = self.colors[cell_value]
                cell_rect = pygame.Rect(x, y, w, h)
                pygame.draw.rect(screen, cell_color, cell_rect)

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        else:
            return False
