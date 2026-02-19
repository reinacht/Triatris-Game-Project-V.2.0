import random
import pygame
from ..Triangles.Main_Triangle import *

# POSITION
class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

# MAIN NEXT_SHAPE
class NEXT_SHAPE:
    def __init__(self, screen, colors, color_schema, color_id, condition, index, index_t):
        self.screen = screen
        self.colors = colors
        self.color = colors
        self.color_schema = color_schema
        self.color_id = color_id
        self.con = None
        self.index = index
        self.index_t = index_t
        
        self.conditions ={0 : condition}
        self.condition = 0

        # POSISI MOVE NANTI
        self.column_offset = 0
        self.row_offset = 0
        self.move(6, 0)


    # movesets
    def move(self, column, row):
        self.column_offset += column
        self.row_offset += row

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

    # draw cell triangle yah bub
    def draw_triangle(self):
        if self.color_schema == 4: # if rainbowww
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)
            pygame.draw.polygon(self.screen, self.colors[val_schema][val_color], self.triangle)

        else:
            val_color = self.color_id
            pygame.draw.polygon(self.screen, self.colors[val_color], self.triangle)


    # draw cell rect yah bub
    def draw_rectangle(self, column, row, size):
        x = column * size + 1
        y = row * size + 1
        w = size - 1
        h = size - 1 
        
        if self.color_schema == 4: # if player select rainbow schema
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)

            tiles_rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(self.screen, self.colors[val_schema][val_color], tiles_rect)
        
        else: # if not
            val_color = self.color_id
        
            tiles_rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(self.screen, self.colors[val_color], tiles_rect)

        
    def draw_shape(self):
        if self.index == 0:
            if self.index_t == 0:
                self.draw_t1()

            elif self.index_t == 1:
                self.draw_t2()

            elif self.index_t == 2:
                self.draw_t3()

            elif self.index_t == 3:
                self.draw_t4()

        elif self.index == 1:
            self.draw_2t()

        elif self.index == 2:
            self.draw_2t1r()

        elif self.index == 3:
            self.draw_minitz()

        elif self.index == 4:
            self.draw_p()

        elif self.index == 5:
            self.draw_r()

        elif self.index == 6:
            self.draw_tz()

        elif self.index == 7:
            self.draw_o()

        elif self.index == 8:
            self.draw_gs()

 
    def draw_gs(self):
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


    def draw_t1(self):
        size = 35
        self.con = self.get_cell_position()
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column 
            row = position.row
            
            self.column = column
            self.row = row

        if self.condition == 0:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t1(column, row, size)

        elif self.condition == 1:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t2(column, row, size)

        elif self.condition == 2:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t3(column, row, size)

        elif self.condition == 3:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t4(column, row, size)
        self.array_states.append(self.triangle_state)


        # make triangle
        self.triangle = [self.sudut1, self.sudut2, self.sudut3]
        if self.color_schema == 4:
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)
            pygame.draw.polygon(self.screen, self.color[val_schema][val_color], self.triangle)

        else:
            val_color = self.color_id
            pygame.draw.polygon(self.screen, self.color[val_color], self.triangle)


    def draw_t2(self):
        size = 35
        self.con = self.get_cell_position()
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column 
            row = position.row 
            
            self.column = column
            self.row = row

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
        if self.color_schema == 4:
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)
            pygame.draw.polygon(self.screen, self.color[val_schema][val_color], self.triangle)
        else:
            val_color = self.color_id
            pygame.draw.polygon(self.screen, self.color[val_color], self.triangle)

    def draw_t3(self):
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
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t3(column, row, size)

        elif self.condition == 1:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t4(column, row, size)

        elif self.condition == 2:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t1(column, row, size)

        elif self.condition == 3:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t2(column, row, size)
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

    def draw_t4(self):
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
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t4(column, row, size)

        elif self.condition == 1:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t1(column, row, size)

        elif self.condition == 2:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t2(column, row, size)

        elif self.condition == 3:
            self.sudut1, self.sudut2, self.sudut3, self.triangle_state = self.t3(column, row, size)
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

    def draw_2t(self):
        size = 35
        self.con = self.get_cell_position()
        TRIANGLES = Triangle(self.screen, self.colors, self.color_schema)
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column
            row = position.row
            
            self.column = column
            self.row = row

            # kalau kondisinya 1 bub
            if self.condition == 0:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state= TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                self.array_states.append(self.triangle_state)
    

            # kalau kondisinya 2 bub
            elif self.condition == 1:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                self.array_states.append(self.triangle_state)


            # kalau kondisinya 3 bub
            elif self.condition == 2:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                self.array_states.append(self.triangle_state)


            # kalau kondisinya 4 bub
            elif self.condition == 3:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                self.array_states.append(self.triangle_state)

    def draw_2t1r(self):
        size = 35
        self.con = self.get_cell_position()
        TRIANGLES = Triangle(self.screen, self.colors, self.color_schema)
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column
            row = position.row
            
            self.column = column
            self.row = row

            # kalau kondisinya 1 bub
            if self.condition == 0:
                if cell == 1:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                self.array_states.append(self.triangle_state)
    

            # kalau kondisinya 2 bub
            elif self.condition == 1:
                if cell == 0:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                self.array_states.append(self.triangle_state)


            # kalau kondisinya 3 bub
            elif self.condition == 2:
                if cell == 1:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                self.array_states.append(self.triangle_state)


            # kalau kondisinya 4 bub
            elif self.condition == 3:
                if cell == 2:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                else:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()   
                self.array_states.append(self.triangle_state)    


    def draw_p(self):
        size = 35
        self.con = self.get_cell_position()
        TRIANGLES = Triangle(self.screen, self.colors, self.color_schema)
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column
            row = position.row
            
            self.column = column
            self.row = row

            # kalau kondisinya 1 atau 3 bub
            if self.condition == 0 or self.condition == 2:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 3:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 4:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 7:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)


            # kalau kondisinya 2 atau 4 bub
            elif self.condition == 1 or self.condition == 3:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 2:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 5:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 7:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)


    def draw_r(self):
        size = 35
        self.con = self.get_cell_position()
        TRIANGLES = Triangle(self.screen, self.colors, self.color_schema)
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column
            row = position.row
            
            self.column = column
            self.row = row

            if cell == 0 or cell == 2:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            elif cell == 1 or cell == 5:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            elif cell == 6 or cell == 10:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            elif cell == 9 or cell == 11:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            else:
                self.draw_rectangle(column, row, size)
                self.triangle_state = 10

            self.array_states.append(self.triangle_state)                


    def draw_tz(self):
        size = 35
        self.con = self.get_cell_position()
        TRIANGLES = Triangle(self.screen, self.colors, self.color_schema)
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column
            row = position.row
            
            self.column = column
            self.row = row

            # kalau kondisinya 1 bub
            if self.condition == 0:
                if cell == 0 or cell == 5:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 4 or cell == 11:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()
                    
                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)

            # kalau kondisinya 2 bub
            elif self.condition == 1:
                if cell == 0 or cell == 2:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 10 or cell == 11:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)

            # kalau kondisinya 3 bub
            elif self.condition == 2:
                if cell == 0 or cell == 7:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 6 or cell == 11:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)

            # kalau kondisinya 4 bub
            elif self.condition == 3:
                if cell == 0 or cell == 1:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 9 or cell == 11:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)


    def draw_minitz(self):
        size = 35
        self.con = self.get_cell_position()
        TRIANGLES = Triangle(self.screen, self.colors, self.color_schema)
        self.array_states = []

        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column
            row = position.row
            
            self.column = column
            self.row = row

            # kalau kondisinya 1 bub
            if self.condition == 0:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 2:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()
                    
                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)

            # kalau kondisinya 2 bub
            elif self.condition == 1:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 2:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)

            # kalau kondisinya 3 bub
            elif self.condition == 2:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 2:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)

            # kalau kondisinya 4 bub
            elif self.condition == 3:
                if cell == 0:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                elif cell == 2:
                    self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                    self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                    self.draw_triangle()

                else:
                    self.draw_rectangle(column, row, size)
                    self.triangle_state = 10

                self.array_states.append(self.triangle_state)


    def draw_o(self):
        size = 35
        self.con = self.get_cell_position()
        TRIANGLES = Triangle(self.screen, self.colors, self.color_schema)
        self.array_states = []

        # kondisinya cmn 1 bub yahyayha, jadi forloop aja gas=usah id=f
        for cell in range(len(self.con)):
            position = self.con[cell]
            column = position.column 
            row = position.row 
            
            self.column = column
            self.row = row

            if cell == 0:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            elif cell == 2:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            elif cell == 6:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            elif cell == 8:
                self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(column, row, size)
                self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                self.draw_triangle()

            else:
                self.draw_rectangle(column, row, size)
                self.triangle_state = 10

            self.array_states.append(self.triangle_state)


     # four triangles yah
    def t1(self, column, row, size):
        # P1
        X = (column + 1) * size - 1
        Y = row * size + 1
        self.sudut1 = (X, Y) 

        # P2
        X = column * size + 1
        Y = (row + 1) * size - 1
        self.sudut2 = (X, Y) 

        # P3
        X = (column + 1) * size - 1
        Y = (row + 1) * size - 1
        self.sudut3 = (X, Y) 
        self.triangle_state = 1

        return self.sudut1, self.sudut2, self.sudut3, self.triangle_state


    def t2(self, column, row, size):
        # P1
        X = column * size + 1
        Y = row * size + 1
        self.sudut1 = (X, Y) 

        # P2
        X = column * size + 1
        Y = (row + 1) * size - 1
        self.sudut2 = (X, Y) 

        # P3
        X = (column + 1) * size - 1
        Y = (row + 1) * size - 1
        self.sudut3 = (X, Y) 
        self.triangle_state = 2

        return self.sudut1, self.sudut2, self.sudut3, self.triangle_state

    def t3(self, column, row, size):
        # P1
        X = column * size + 1
        Y = row * size + 1
        self.sudut1 = (X, Y) 

        # P2
        X = (column + 1) * size - 1
        Y = row * size + 1
        self.sudut2 = (X, Y) 

        # P3
        X = column * size + 1
        Y = (row + 1) * size - 1
        self.sudut3 = (X, Y) 
        self.triangle_state = 9

        return self.sudut1, self.sudut2, self.sudut3, self.triangle_state

    def t4(self, column, row, size):
        # P1
        X = column * size + 1
        Y = row * size + 1
        self.sudut1 = (X, Y) 

        # P2
        X = (column + 1) * size - 1
        Y = row * size + 1
        self.sudut2 = (X, Y) 

        # P3
        X = (column + 1) * size - 1
        Y = (row + 1) * size - 1
        self.sudut3 = (X, Y)
        self.triangle_state = 8

        return self.sudut1, self.sudut2, self.sudut3, self.triangle_state