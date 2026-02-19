import pygame
import random
from .Main_Triangle import Triangle

# TRIANGLE2 OBJECT
class Triangle2(Triangle):
    def __init__(self, screen, colors, color_schema):
        super().__init__(screen, colors, color_schema)
    
    # draw
    def draw_shape(self):
        size = 35
        self.con = self.get_cell_position()
        self.array_states = []

        # POSSISI BRPYAH
        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column 
            row = position.row 
            
            self.column = column
            self.row = row

        # CEK DULU DIA ROTASINYA DEFAULT GA
        # 3 TITIK SEGITIGA (P1, P2, P3) DGN MASING MASING X Y
        if self.condition == 0:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t2(column, row, size)

        elif self.condition == 1:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t3(column, row, size)

        elif self.condition == 2:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t4(column, row, size)

        elif self.condition == 3:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t1(column, row, size)
        self.array_states.append(self.triangle_state)


        # make triangle
        self.triangle = [self.sudut1, self.sudut2, self.sudut3]

        # if not rainbowww
        if self.color_schema == 4:
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)
            pygame.draw.polygon(self.screen, self.color[val_schema][val_color], self.triangle)

        # if rainbowww rubyysysss
        else:
            val_color = self.color_id
            pygame.draw.polygon(self.screen, self.color[val_color], self.triangle)