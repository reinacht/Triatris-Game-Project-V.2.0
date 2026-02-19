import pygame
import random
from Shapes import Triangle

# grid object
class Grid:
    def __init__(self, screen, colors, select_schema):
        self.rows = 23
        self.columns = 13
        self.grid = []
        self.grid_colors =  []
        self.cells_size = 35
        self.screen = screen
        self.colors = colors
        self.select_schema = select_schema

        # make grid with 23 x 13
        for r in range(self.rows):
            array = []
            for c in range(self.columns):
                array.append(0)
            self.grid.append(array)

        for r in range(self.rows):
            array_c = []
            for c in range(self.columns):
                array_c.append(0)
            self.grid_colors.append(array_c)

    def draw_tiles(self):
        for r in range(self.rows):
            for c in range(self.columns):
                cell_val = 0
                x = c*self.cells_size + 1
                y = r*self.cells_size + 1
                w = self.cells_size - 1
                h = self.cells_size - 1 
                # print(f"x = {x}, y = {y}, w = {w}, h = {h}")

                #if schema rainbow
                if self.select_schema == 4:
                    cell_rect = pygame.Rect(x, y, w, h)
                    pygame.draw.rect(self.screen, self.colors[random.randint(0, 2)][cell_val], cell_rect)

                #if not
                else: 
                    cell_rect = pygame.Rect(x, y, w, h)
                    pygame.draw.rect(self.screen, self.colors[0], cell_rect)


        if True:
            # tuk gambar blocknya yawhh
            TRIANGLES = Triangle(self.screen, self.colors, self.select_schema)
            size = 35
            for r in range(self.rows):
                for c in range(self.columns):
                    # check bentuknya dan gambar di grid yawhs
                    if self.grid[r][c] == 1: 
                        self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t1(c, r, size)
                        self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                        self.draw_fixed_triangle(self.grid_colors[r][c], self.triangle)


                    elif self.grid[r][c] == 2:
                        self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t2(c, r, size)
                        self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                        self.draw_fixed_triangle(self.grid_colors[r][c], self.triangle)
        

                    elif self.grid[r][c] == 9:
                        self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t3(c, r, size)
                        self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                        self.draw_fixed_triangle(self.grid_colors[r][c], self.triangle)


                    elif self.grid[r][c] == 8:
                        self.sudut1, self.sudut2, self.sudut3, self.triangle_state = TRIANGLES.t4(c, r, size)
                        self.triangle = [self.sudut1, self.sudut2, self.sudut3]
                        self.draw_fixed_triangle(self.grid_colors[r][c], self.triangle)


                    elif self.grid[r][c] == 10:
                        self.draw_fixed_rectangle(c, r, size, self.grid_colors[r][c])
        


    # draw di grid yaqh
    def draw_fixed_triangle(self, color_id, triangle):
        if self.select_schema == 4:
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)
            pygame.draw.polygon(self.screen, self.colors[val_schema][val_color], triangle)

        else: 
            val_color = color_id
            pygame.draw.polygon(self.screen, self.colors[val_color], triangle)


    def draw_fixed_rectangle(self, column, row, size, color_id):
        x = column * size + 1
        y = row * size + 1
        w = size - 1
        h = size - 1 
        
        if self.select_schema == 4: # if player select rainbow schema
            val_schema = random.randint(0, 2)
            val_color = random.randint(1, 7)

            tiles_rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(self.screen, self.colors[val_schema][val_color], tiles_rect)
        
        else: # if not
            val_color = color_id
        
            tiles_rect = pygame.Rect(x, y, w, h)
            pygame.draw.rect(self.screen, self.colors[val_color], tiles_rect)



# class color for schemes
class Colors:
    def __init__(self):
        # scheme 1
        self.midnight_blue = (20, 25, 35)
        self.green = (47, 230, 23)
        self.red = (232, 18, 18)
        self.orange = (226, 116, 17)
        self.yellow = (237, 234, 4)
        self.tosca = (0, 125, 120)
        self.cyan = (21, 204, 209)
        self.blue = (13, 64, 216)
        self.white = (255, 255, 255)


        # scheme 2 (neon)
        self.midnight_blue = (20, 25, 35)
        self.sky_aqua = (10, 210, 255)
        self.electric_sapphire = (41, 98, 255)
        self.violet_ray = (149, 0, 255)
        self.hot_fuchsia = (255, 0, 89)
        self.dark_orange = (255, 140, 0)
        self.chartreuse = (180, 230, 0)
        self.aqua_marine = (15, 255, 219)
        self.white = (255, 255, 255)

        # scheme 3 (beuatiful ini yg papa cari)
        self.midnight_blue = (20, 25, 35)
        self.powder_blush = (255, 173, 173)
        self.apricot_cream = (255, 214, 165)
        self.lemon_chiffon = (253, 255, 182)
        self.tea_green = (202, 255, 191)
        self.soft_cyan = (155, 246, 255)
        self.baby_blue_ice = (160, 196, 255)
        self.periwinkle = (189, 178, 255)
        self.white = (255, 255, 255)


    def get_colors(self, selectScheme):
        # scheme2 = [self.dark_grey, self.pearl_aqua1, self.pearl_aqua2, self.tea_green, self.peach_fuzz, self.powder_blush1, self.light_coral, self.grapefruit_pink, self.white]
        # scheme3 = [self.dark_grey, self.lemon_chiffon, self.soft_apricot, self.powder_blush2, self.cherry_blossom, self.cotton_candy, self.rose_kiss1, self.rose_kiss2, self.white]
        scheme1 = [self.midnight_blue, self.green, self.red, self.orange, self.yellow, self.tosca, self.cyan, self.blue, self.white]
        scheme2 = [self.midnight_blue, self.sky_aqua, self.electric_sapphire, self.violet_ray, self.hot_fuchsia, self.dark_orange, self.chartreuse, self.aqua_marine, self.white]
        scheme3 = [self.midnight_blue,  self.powder_blush, self.apricot_cream, self.lemon_chiffon, self.tea_green, self.soft_cyan, self.baby_blue_ice, self.periwinkle, self.white]
        scheme4 = [scheme1, scheme2, scheme3] # rainbow ruby

        colorSchemas = [scheme1, scheme2, scheme3, scheme4]

        return colorSchemas[selectScheme-1]

        # scheme 2
        # self.dark_grey = (26, 31, 40)
        # self.pearl_aqua1 = (132, 227, 200)
        # self.pearl_aqua2 = (168, 230, 207)
        # self.tea_green = (220, 237, 193)
        # self.peach_fuzz = (255, 211, 182)
        # self.powder_blush1 = (255, 170, 165)
        # self.light_coral = (255, 139, 148)
        # self.grapefruit_pink = (255, 116, 128)

        # scheme 3
        # self.dark_grey = (26, 31, 40)
        # self.lemon_chiffon = (252, 243, 196)
        # self.soft_apricot = (252, 219, 190)
        # self.powder_blush2 = (251, 195, 184)
        # self.cherry_blossom = (251, 171, 178)
        # self.cotton_candy = (250, 146, 172)
        # self.rose_kiss1 = (250, 122, 166)
        # self.rose_kiss2 = (249, 98, 160)
        # self.white = (255, 255, 255)
        # self.white = (255, 255, 255)