import pygame
import random
from ..Triangles.Main_Triangle import *

# POSITION
class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

# MAIN PARALLELOGRAM OBJECT (JAJAR GENJANG)
class Ghost_Shape:
    def __init__(self, screen, colors, color_schema):
        # VARISBLE YG DUBUTHUKNAN BUB
        self.screen = screen
        self.colors = colors
        self.color_schema = color_schema
        self.color_id = 8
        self.condition = 0
        self.con = None

        # POSISI MOVE NANTI
        self.column_offset = 0
        self.row_offset = 0
        self.move(3, 0)

        # EMPAT KONDISI JAJAR GENJANG
        self.conditions = {
            0 : [Position(0, 0)],
            1 : [Position(0, 0)],
            2 : [Position(0, 0)],
            3 : [Position(0, 0)]
        }
    
    # posisinya bub
    def get_cell_position(self):
        old_position = self.conditions[self.condition]
        new_position = []

        for p in old_position:
            new_column = p.column + self.column_offset
            new_row = p.row + self.row_offset

            temp_array = Position(new_column, new_row)
            new_position.append(temp_array)

        return new_position


    # movesets
    def move(self, column, row):
        self.column_offset += column
        self.row_offset += row


    # draw cell rect yah bub
    def draw_rectangle(self, column, row, size):
        x = column * size + 1
        y = row * size + 1
        w = size - 1
        h = size - 1 
        
        tiles_rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(self.screen, "White", tiles_rect)

        
    # draw 
    def draw_shape(self):
        size = 35
        self.con = self.get_cell_position()
        self.array_states = [0]

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column
            row = position.row
            
            self.column = column
            self.row = row
            self.draw_rectangle(column, row, size)
                    