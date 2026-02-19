import Shapes
import random
from utils.Grid_and_Colors_Class import *
from Shapes import Triangle
from pathlib import Path
import sqlite3
import utils.db_weg as db_weg

# dinamis yh
BASE_DIR = Path(__file__).resolve().parent

# game object
class Games:
    def __init__(self, screen, color, grid, color_schema, audio, difficulty, h_score):
        self.screen = screen
        self.color = color
        self.color_schema = color_schema
        self.grid = grid
        self.temp_grid = grid
        self.difficulty = difficulty
        self.count_shape = 1
        self.current_shape = self.get_random_shape()
        self.next_shape = self.get_random_shape()
        self.NEW_STATES = None
        self.state_change = 0
        self.yeay = 0
        self.completed_lol = 0
        self.score = 0
        self.merged_sfx = audio[0]
        self.row_sfx = audio[1]
        self.rowd_sfx = audio[2]
        self.click_sfx = audio[3]
        self.rotations_sfx = audio[4]
        self.go_sfx = audio[5]
        self.bebek = False
        self.down = ""
        self.right = ""
        self.left = ""
        self.bocil_crypto = "Ronald"
        self.h_score = int(h_score)
         
        self.GO_STATE = False
        self.GO_text = ""

    # dapetin shapes random dlu cinta
    def get_random_shape(self):
        triangles = [
            Shapes.Triangle1(self.screen, self.color, self.color_schema), 
            Shapes.Triangle2(self.screen, self.color, self.color_schema), 
            Shapes.Triangle3(self.screen, self.color, self.color_schema), 
            Shapes.Triangle4(self.screen, self.color, self.color_schema),
            ]
        self.rand_triangle = random.randint(0, 3)
        rand_triangle = triangles[self.rand_triangle]
        
        self.SHAPES = [
            rand_triangle,
            Shapes.TwoTriangles(self.screen, self.color, self.color_schema),
            Shapes.TwoTriangles_OneRect(self.screen, self.color, self.color_schema),
            Shapes.MiniTrapezoid(self.screen, self.color, self.color_schema),
            Shapes.Parallelograms(self.screen, self.color, self.color_schema),
            Shapes.Rhombus(self.screen, self.color, self.color_schema),
            Shapes.Trapezoid(self.screen, self.color, self.color_schema),
            Shapes.Octagon(self.screen, self.color, self.color_schema),
            Shapes.Ghost_Shape(self.screen, self.color, self.color_schema)
            ]
        
        # pilih difficulty
        if self.difficulty == "EASY":
            list_debug = [self.SHAPES[0], self.SHAPES[1], self.SHAPES[2], self.SHAPES[3]]
            self.index_rand = random.randint(0, 3)
            self.SHAPE = list_debug[self.index_rand]

        elif self.difficulty == "HARD":
            self.index_rand = random.randint(0, 7)

            # kikir ghostblocknya
            if self.count_shape == 2:
                self.index_rand = 8
            self.SHAPE = self.SHAPES[self.index_rand]
            
        return self.SHAPE

    # draw shapenya di grid, tapi ga naruh nilainya di dalam array grid itu, jdiny dia cmn ngisi nilai di array grid klw collision atau di luar kotak. lihat fungshi is_inside, is_collision dan lock_shape yah beb
    def draw(self):
        self.grid.draw_tiles() 
        self.current_shape.draw_shape()

    # moveset
    def rotation_move(self): 
        # tuk pastiin biar ga -1
        if self.current_shape.condition == 3 or self.current_shape.condition == -1:
            self.current_shape.condition = 0
        else:
            self.current_shape.condition += 1

        # cek anune, logic collision and cell insidenya
        if self.is_not_collision() == False or self.cell_inside() == False:
            self.current_shape.condition -= 1
            if self.current_shape.condition == -1:
                self.current_shape.condition = 3


    def down_move(self):
        self.down = "Y"
        self.current_shape.move(0, 1)

        # cek anune, logic collision and cell insidenya
        if self.is_not_collision() == False or self.cell_inside() == False:
            self.current_shape.move(0, -1)
            self.lock_shape()
            self.down = "N"

        # reset var
        if self.bocil_crypto == "Timothy":
            self.bocil_crypto = "Ronald"

        self.down = "N"


    def right_move(self):
        self.right = "Y"
        self.current_shape.move(1, 0)

        # cek anune, logic collision and cell insidenya
        if self.is_not_collision() == False or self.cell_inside() == False:
            self.current_shape.move(-1, 0)

            # klw udah merged, langsung dilock blocknya ywh
            if self.bocil_crypto == "Timothy":
                self.lock_shape()
                self.bocil_crypto = "Ronald"

            self.right = "N"
        self.right = "N"


    def left_move(self):
        self.left = "Y"
        self.current_shape.move(-1, 0)

        # cek anune, logic collision and cell insidenya
        if self.is_not_collision() == False or self.cell_inside() == False:
            self.current_shape.move(1, 0)

            # klw udah merged, langsung dilock blocknya ywh
            if self.bocil_crypto == "Timothy":
                self.lock_shape()
                self.bocil_crypto = "Ronald"

            self.left = "N"
        self.left = "N"


    # shape logic di dalam g
    def is_inside(self, column, row):
        if column >= 0 and column < 13 and row >= 0 and row < 23:
            return True
        return False

    # shape logic di dalam g
    def cell_inside(self):
        tiles = self.current_shape.get_cell_position() 
        for j, tile in enumerate(tiles):
            if self.is_inside(tile.column, tile.row) == False:
                return False
        return True


    def is_not_collision(self):
        # klw ghost shape true smua
        if self.count_shape == 3 and self.difficulty == "HARD":
            return True

        # assign state utk movesetnya nyaww!~
        D = ""
        R = ""
        L = ""
        tiles = self.current_shape.get_cell_position()

        # klw udah merged, langsung di-lock blocknya ywh (hny bwleh sekali merged hehehe biar setia kek ak dn dia)
        if self.bebek == True:
            self.bebek = False
            self.bocil_crypto = "Timothy"
            return False
        
        # khusus bug khusus yah aowkwow cmn 2 line doang utk nyelesain bugnya, pdhl udar mikir 3 jam an
        if self.cell_inside() == False:
            return False
        
        # cek coll 1, kalau ada yg ga 10 artine ada shape bertabrakan dan gabisa merged langsung di-lock
        for j, tile in enumerate(tiles):
            state = self.current_shape.array_states[j]

            if self.is_empty(tile.row, tile.column) == False:
                if state + self.grid.grid[tile.row][tile.column] != 10:
                    return False


        # cek coll 2, kalau ada shape triangle dilakukan logic yawh, bisa ga merged
        for j, tile in enumerate(tiles):
            if self.is_empty(tile.row, tile.column) == False: 

                # ambil state shapenya
                state = self.current_shape.array_states[j]
                if state in [9, 8, 2, 1]: # hanya bisa merged kalau 9821 (triangles)
                   
                    list_kombinasi = [state, self.grid.grid[tile.row][tile.column]]

                    # nah ikii, logic utama kalau ketemu triangles, dia ngecek dl movesetnya dan kombinasi yg tersedia yawh
                    if (list_kombinasi[0] == 9 and list_kombinasi[1] == 1 or list_kombinasi[0] == 8 and list_kombinasi[1] == 2) and self.down == "Y":
                        D = "D"

                    elif (list_kombinasi[0] == 9 and list_kombinasi[1] == 1 or list_kombinasi[0] == 2 and list_kombinasi[1] == 8) and self.right == "Y":
                        R = "R"

                    elif (list_kombinasi[0] == 8 and list_kombinasi[1] == 2 or list_kombinasi[0] == 1 and list_kombinasi[1] == 9) and self.left == "Y":
                        L = "L"
                    
                    # kalau ada yg ke assign berarti ada block yg merged dan anu, di grid yg join itu akan di assign 10 ywah dan di grid state juga 10 yawh
                    if D == "D" or R == "R" or L == "L": 
                        self.grid.grid[tile.row][tile.column] = 10
                        self.current_shape.array_states[j] = 10
                        self.NEW_STATES = self.current_shape.array_states

                        self.yeay = 1

                        
                # kalau loopnya abis sesuai panjang statenya
                if j+1 == len(self.current_shape.array_states):
                    # perbarui statenya yahhhhhhh kalau new statesnya ada                           
                    if self.NEW_STATES != None:
                        self.current_shape.array_states = self.NEW_STATES # buat temp state yawh

        # cek coll 3 (final), dia ngecek apakah ada yg merged? kalau ada yg merged itu berarti self.yeay == 1, maka langsung play sfx, turunkan sekali tuk merged dan langsung false dengan self.bebel = True
        for j, tile in enumerate(tiles):
            if self.is_empty(tile.row, tile.column) == False:
                if self.yeay == 1:
                    self.temp = self.current_shape.array_states
                    self.yeay -= 1
                    self.merged_sfx.play()
                    self.bebek = True
                    return True
                
                return False 
               
        return True

    
    # tuk cek kosong g
    def is_empty(self, row, column):
        if row > 22:
            row = 22
        if column > 12:
            column = 12

        if self.grid.grid[row][column] == 0:
            return True
        return False

    # menguncinta
    def lock_shape(self):
        cell = 0
        # kalau ada state bru dri merged td, maka diupdate statenya ioi
        if self.NEW_STATES != None:
            self.current_shape.array_states = self.temp

        # dia buat anu looping tuk cek state gridnya dan digambar sesuai anune, sesuai state
        for state in self.current_shape.array_states:
            position = self.current_shape.con[cell]
            cell += 1

            # check bentuknya dan gambar di grid yawhs 
            if state == 1:
                self.grid.grid[position.row][position.column] = 1
                self.grid.grid_colors[position.row][position.column] = self.current_shape.color_id

            elif state == 2:
                self.grid.grid[position.row][position.column] = 2
                self.grid.grid_colors[position.row][position.column] = self.current_shape.color_id

            elif state == 9:
                self.grid.grid[position.row][position.column] = 9
                self.grid.grid_colors[position.row][position.column] = self.current_shape.color_id

            elif state == 8:
                self.grid.grid[position.row][position.column] = 8
                self.grid.grid_colors[position.row][position.column] = self.current_shape.color_id

            else:
                self.grid.grid[position.row][position.column] = 10
                self.grid.grid_colors[position.row][position.column] = self.current_shape.color_id
    
        # reset state baru tuk merged itu loh + namabahin skorenya
        if self.NEW_STATES != None:
            self.NEW_STATES = None
            self.score += 21

        # kalau block ghostnya udah jalan, dia reset lagi biar ghostnya munvul again
        if self.count_shape == 3:
            self.count_shape = 0

        # assign shape baru wah
        self.current_shape = self.next_shape
        self.count_shape += 1
        self.next_shape = self.get_random_shape()
        self.score += 7
        self.rowd_sfx.play()
        
        # klw go, dia write ke .txt tpi cek skorenya dl
        if self.game_over() == True:
            self.GO_STATE = True
            if self.score > self.h_score:
                # with open(f"{BASE_DIR}/Shapes/Triangles/score.txt", "w+") as f:
                #     f.write(str(self.score))
                #     f.seek(0)
                self.save_score(str(self.score))

        # check rows setiap lock shape
        self.check_rows()

    # iki susah amat lo buat next shapenya, jadi nextshapenya harus class baru karena class kompleks gabisa dicoopy python
    def show_next_shape(self):
        self.DISPLAY_NEXT_SHAPE = Shapes.NEXT_SHAPE(self.screen, self.color, self.color_schema, color_id=self.next_shape.color_id, condition=self.next_shape.conditions[0], index=self.index_rand, index_t=self.rand_triangle)
        self.DISPLAY_NEXT_SHAPE.move(9, 3)
        self.DISPLAY_NEXT_SHAPE.draw_shape()

    # logic utk row completednya yaawh
    def check_rows(self):
        for i, row in enumerate(self.grid.grid):
            if sum(row) == 130:
                self.grid.grid.pop(i)
                self.grid.grid.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                self.grid.grid_colors.pop(i)
                self.grid.grid_colors.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                self.completed_lol += 1
                self.score += 130
                self.row_sfx.play()

    # GO JAJAJAJJAJAJA
    def game_over(self):
        tiles = self.current_shape.get_cell_position()

        # klw block spawn yg sekrng itu tabrakan di atas ya GO dong ioi
        for j, tile in enumerate(tiles):
            if self.is_empty(tile.row, tile.column) == False: 
                self.GO_text = "GAME OVER"
                return True
            
    # sqlite command funktion
    def save_score(self, score):
        # konnektion zur der DB
        path_db = db_weg.get_db_path()

        conn = sqlite3.connect(path_db)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Skoren (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                score text
            )
        """)
        cursor.execute(
            "INSERT INTO Skoren (score) VALUES (?)", 
            (score,)
        )

        conn.commit()
        conn.close()

