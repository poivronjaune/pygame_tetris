from position import Position
import pygame
from config import *
from colors import Colors
from position import Position

class Block:
    def __init__(self, id):
        self.id = id # Each block has a fixed color based on it's id
        self.cells = {}
        self.cell_size = CELL_SIZE
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x = 0, offset_y = 0):
        #tiles = self.cells[self.rotation_state]
        tiles = self.get_cell_positions()
        for tile in tiles:
            x = tile.column * self.cell_size + BORDER_WIDTH + GRID_PADDING + offset_x
            y = tile.row * self.cell_size + BORDER_WIDTH + GRID_PADDING + offset_y
            w = self.cell_size - BORDER_WIDTH
            h = self.cell_size - BORDER_WIDTH
            tile_rect = pygame.Rect(x, y, w, h )
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)
