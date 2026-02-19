import random

# POSITION
class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

# MAIN TRIANGLE OBJECT
class Triangle:
    def __init__(self, screen, colors, color_schema):
        self.screen = screen
        self.color = colors
        self.color_schema = color_schema
        self.color_id = random.randint(1, 7)
        self.con = None
        
        self.conditions = {
            0 : [Position(0, 0)],
            1 : [Position(0, 0)],
            2 : [Position(0, 0)],
            3 : [Position(0, 0)]
        }
        self.condition = 0

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