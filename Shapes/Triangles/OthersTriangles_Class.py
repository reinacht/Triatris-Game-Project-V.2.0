import random
import pygame
from .Main_Triangle import Triangle


# POSITION
class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


# OTHER TRIANGLE OBJECT
# iniliasisi tuk parentnyahhhs
class ParentThis:
    def __init__(self, screen, colors, color_schema):
        self.screen = screen
        self.colors = colors
        self.color_schema = color_schema
        self.color_id = random.randint(1, 7)
        self.condition = 0
        self.con = None

        # POSISI MOVE NANTI
        self.column_offset = 0
        self.row_offset = 0
        self.move(6, 0)

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

    # draw cell triangle yah bub
    def draw_triangle(self):
        if self.color_schema == 4: # if not rainbowww
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)
            pygame.draw.polygon(self.screen, self.colors[val_schema][val_color], self.triangle)

        else: # if rainbowww rubyysysss
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




# TWO TRIANGLE 
class TwoTriangles(ParentThis):
    def __init__(self, screen, colors, color_schema):
        super().__init__(screen, colors, color_schema)
        self.conditions = {
            0 : [Position(0, 0), Position(1, 0)],
            1 : [Position(1, 0), Position(1, 1)],
            2 : [Position(0, 1), Position(1, 1)],
            3 : [Position(0, 0), Position(0, 1)]
        }
        
    # draw 
    def draw_shape(self):
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



# TWO TRIANGLE + 1 rect
class TwoTriangles_OneRect(ParentThis):
    def __init__(self, screen, colors, color_schema):
        super().__init__(screen, colors, color_schema)
        self.conditions = {
            0 : [Position(0, 0), Position(0, 1), Position(1, 1)],
            1 : [Position(0, 0), Position(1, 0), Position(0, 1)],
            2 : [Position(0, 0), Position(1, 0), Position(1, 1)],
            3 : [Position(1, 0), Position(0, 1), Position(1, 1)]
        }

    # draw 
    def draw_shape(self):
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