import pygame
import sys
from utils.Games_Class import *
from utils.Grid_and_Colors_Class import *
import random
from pathlib import Path
import utils.db_weg as db_weg

# dinamis yh
BASE_DIR = Path(__file__).resolve().parent

# inisiasi
icon_game = pygame.image.load(f"{BASE_DIR}/assets/img/icon_game.png")
pygame.display.set_icon(icon_game)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Triatris")
screen = pygame.display.set_mode((821, 810)) # width, height : x y
clock = pygame.time.Clock()
running = True
GAME_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(GAME_UPDATE, 500)


# inisisaasi var penting oi
vol = 1
vol_process = "OFF"
PAUSE = 1
stateGO = 0
difficulty = "EASY"

# take the score from sqlite
def take_score():
    # konnektion zur der DB
    path_db = db_weg.get_db_path()

    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Skoren ORDER BY id DESC LIMIT 1")
        rows = cursor.fetchone()
        print(rows)
        
        if rows != None:
            h_score = int(rows[1])   
        else:
            h_score = 0

    except sqlite3.OperationalError:
        h_score = 0

    conn.close()
    return h_score

h_score = take_score()

# kumpulan warna yah
color_screen_main_menu = (68, 183, 255)
color_screen_games = (60, 85, 120)
color_btn_ghost = (68, 183, 255)
color_schema = 1
colors = Colors().get_colors(color_schema)
score_ct = "White"
menu_c = (255, 212, 0)
menu_ct = (255, 255, 255) # WHITE
reset_c = (255, 0, 94)
reset_ct = (255, 255, 255) # WHITE
COLOR_EPILEPSI = [
    (255, 0, 0),      # merah nyala
    (0, 255, 0),      # hijau neon
    (0, 0, 255),      # biru elektrik
    (255, 255, 0),    # kuning neon
    (255, 0, 255),    # magenta nyetrum
    (0, 255, 255),    # cyan neon
    (255, 255, 255),  # putih maksimal
    (255, 128, 0),    # oranye neon  
    (255, 20, 147),   # pink nyala banget
    (128, 0, 255),    # ungu neon
]
COLOR_EPILEPSI_RAINBOW_SURFACE = [
    (255, 0, 0, 120),      # merah nyala
    (0, 255, 0, 20),       # hijau neon
    (0, 0, 255, 70),       # biru elektrik
    (255, 255, 0, 55),     # kuning neon
    (255, 0, 255, 67),     # magenta nyetrum
    (0, 255, 255, 89),     # cyan neon
    (255, 255, 255, 150),  # putih maksimal
    (255, 128, 0, 180),    # oranye neon  
    (255, 20, 147, 124),   # pink nyala banget
    (128, 0, 255, 77),     # ungu neon
]

# kumpulan sound
volume = 1
pygame.mixer.music.load(f"{BASE_DIR}/assets/audio/bgm3.mp3")   
pygame.mixer.music.play(-1) 
merged_sfx = pygame.mixer.Sound(f"{BASE_DIR}/assets/audio/shaped_merged.ogg")
row_sfx = pygame.mixer.Sound(f"{BASE_DIR}/assets/audio/row_completed2.ogg")
rowd_sfx = pygame.mixer.Sound(f"{BASE_DIR}/assets/audio/row_down.ogg")
click_sfx = pygame.mixer.Sound(f"{BASE_DIR}/assets/audio/click.ogg")
rotations_sfx = pygame.mixer.Sound(f"{BASE_DIR}/assets/audio/rotations.ogg")
go_sfx = pygame.mixer.Sound(f"{BASE_DIR}/assets/audio/game_over.ogg")
audio = [merged_sfx, row_sfx, rowd_sfx, click_sfx, rotations_sfx, go_sfx]

# kumpulan FONT
font_SIZE_LIKE_YOUR_DIH = pygame.font.Font(None, 21)
font = pygame.font.Font(None, 35)
fontS = pygame.font.Font(None, 28)
fontXS = pygame.font.Font(None, 15)
fontXSS = pygame.font.Font(None, 14)
fontH1 = pygame.font.Font(None, 77)
fontPaddingH1 = pygame.font.Font(None, 77)
fontH2 = pygame.font.Font(None, 65)
fontGO = pygame.font.Font(None, 99)

# kumpulan img
# BIG-IMG
footer = pygame.image.load(f"{BASE_DIR}/assets/img/footer.png")
htp_guide = pygame.image.load(f"{BASE_DIR}/assets/img/how to play.png")
block_blue = pygame.image.load(f"{BASE_DIR}/assets/img/block/blue.png")
block_grey = pygame.image.load(f"{BASE_DIR}/assets/img/block/grey.png")
block_yellow = pygame.image.load(f"{BASE_DIR}/assets/img/block/yellow.png")
block_green = pygame.image.load(f"{BASE_DIR}/assets/img/block/green.png")
block_red = pygame.image.load(f"{BASE_DIR}/assets/img/block/red.png")

# FONT-IMG
f_title = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/TRIATRIS.png")
f_start_hover = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/START.png")
f_start_pressed = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/START (1).png")
f_easy_idle = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/EASY.png")
f_easy_hover = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/EASY-1.png")
f_easy_pressed = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/EASY-2.png")
f_hard_idle = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/HARD.png")
f_hard_hover = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/HARD-1.png")
f_hard_pressed = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/HARD-2.png")
f_credit = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/credit.png")
f_color_schema = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/colorschema.png")
f_Highest_Score = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/Highest Score.png")
f_Next_Shape = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/Next Shape.png") # for game page 
f_Score = pygame.image.load(f"{BASE_DIR}/assets/img/Font_img/Score.png") # for game page 

# BUTTON-IMG
hover_bclor1 = "NO KING"
hover_bclor2 = "NO KING"
hover_bclor3 = "NO KING"
hover_bclor4 = "NO KING"
hover_strt = "NO KING"
hover_easy = "NO KING"
hover_hard = "NO KING"
b_color1 = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color1.png")
b_color2 = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color2.png")
b_color3 = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color3.png")
b_color4 = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color4.png")
b_color1_h = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color1_h.png")
b_color2_h = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color2_h.png")
b_color3_h = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color3_h.png")
b_color4_h = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/color4_h.png")
b_container_v = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/container_v.png")
b_plus = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/plus.png")
b_min = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/min.png")
b_volume = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/volume.png")
b_start_btn = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/start_btn.png")
b_next_shape = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/next_shape.png") # for game page 
b_score = pygame.image.load(f"{BASE_DIR}/assets/img/button_img/score.png") # for game page yh

# Gamess lOLL for page 2 (Games)
colors = Colors().get_colors(color_schema)
GRID = Grid(screen, colors, color_schema)
GAMES = Games(screen, colors, GRID, color_schema, audio, difficulty, h_score)

# page apjahhj
current_page_state = 1

# main 
while running:
    # check page yah
    # kalau menu page yah manis
    if current_page_state == 1:
        # properti
        screen.fill(color_screen_main_menu)
        high_score = fontS.render(f"{h_score}", True, "White")

        # rects - GHOSTINK
        start_btn = pygame.Rect(287, 381, 245, 100)
        c1_btn = pygame.Rect(10, 8, 45, 35)
        c2_btn = pygame.Rect(58, 8, 45, 35)
        c3_btn = pygame.Rect(106, 8, 45, 35)
        c4_btn = pygame.Rect(155, 8, 45, 35)
        easy_btn = pygame.Rect(320, 337, 73, 30)
        hard_btn = pygame.Rect(428, 337, 77, 30)

        # start_btn - GHOSTINK
        pygame.draw.rect(screen, color_btn_ghost, start_btn)

        # color schema btn - GHOSTINK
        pygame.draw.rect(screen, color_btn_ghost, c1_btn, border_radius=13)
        pygame.draw.rect(screen, color_btn_ghost, c2_btn, border_radius=13)
        pygame.draw.rect(screen, color_btn_ghost, c3_btn, border_radius=13)
        pygame.draw.rect(screen, color_btn_ghost, c3_btn, border_radius=13)
 
        # difficulty btn - GHOSTINK
        pygame.draw.rect(screen, color_btn_ghost, easy_btn)
        pygame.draw.rect(screen, color_btn_ghost, hard_btn)

        # highscore
        screen.blit(high_score, (444, 502))

        # volume
        vol_rect = pygame.Rect(770, 25, 27, 27)
        pygame.draw.rect(screen, color_btn_ghost, vol_rect, border_radius=5)

        if vol == -1:
            vol_process = "ON"
            screen.blit(b_container_v, (734, 52))

            vol_up = pygame.Rect(746, 63, 25, 25)
            pygame.draw.rect(screen, "grey", vol_up, border_radius=5)
            screen.blit(b_plus, (750, 67)) 

            vol_down = pygame.Rect(777, 63, 25, 25)
            pygame.draw.rect(screen, "grey", vol_down, border_radius=5)
            screen.blit(b_min, (781, 73)) 


            vol_text = fontXSS.render(f"Music : {int(volume*100)}%", True, (68, 183, 255))
            screen.blit(vol_text, (744, 94))
        else:
            vol_process = "OFF"

        # image
        screen.blit(footer, (0, 647))   
        screen.blit(block_blue, (222, 218))   
        screen.blit(block_grey, (302, 230))   
        screen.blit(block_yellow, (390, 205))   
        screen.blit(block_green, (475, 220))   
        screen.blit(block_red, (558, 202)) 

        # img-f
        screen.blit(f_title, (167, 89)) 
        screen.blit(f_credit, (726, 2)) 
        screen.blit(f_color_schema, (10, 46)) 
        screen.blit(f_Highest_Score, (310, 501)) 

        # img-btn
        screen.blit(b_volume, (774, 24)) 

        # hovering animations use image lol hahahaha
        # color scehmas
        if hover_bclor1 == "NO KING":
            screen.blit(b_color1, (10, 8)) 
        elif hover_bclor1 == "YES KING":
            screen.blit(b_color1_h, (10, 8)) 

        if hover_bclor2 == "NO KING":
            screen.blit(b_color2, (58, 8)) 
        elif hover_bclor2 == "YES KING":
            screen.blit(b_color2_h, (58, 8)) 

        if hover_bclor3 == "NO KING":
            screen.blit(b_color3, (106, 8)) 
        elif hover_bclor3 == "YES KING":
            screen.blit(b_color3_h, (106, 8)) 

        if hover_bclor4 == "NO KING":
            screen.blit(b_color4, (155, 8)) 
        elif hover_bclor4 == "YES KING":
            screen.blit(b_color4_h, (155, 8)) 

        # start
        if hover_strt == "NO KING":
            screen.blit(b_start_btn, (277, 367)) 
        elif hover_strt == "YES KING":
            screen.blit(b_start_btn, (277, 367)) 
            screen.blit(f_start_hover, (324, 416)) 
       
        # difficulty
        if hover_easy == "NO KING":
            screen.blit(f_easy_idle, (320, 341)) 
        elif hover_easy == "YES KING":
            screen.blit(f_easy_hover, (320, 341)) 
            
        if hover_hard == "NO KING":
            screen.blit(f_hard_idle, (426, 341)) 
        elif hover_hard == "YES KING":
            screen.blit(f_hard_hover, (426, 341)) 


    # kalau game page yah manis
    elif current_page_state == 2:
        # color epilepsi khusus tuk color skema 4 ahhaha
        COLOR_RANDOM_EPILEPSI1 = random.choice(COLOR_EPILEPSI)
        COLOR_RANDOM_EPILEPSI2 = random.choice(COLOR_EPILEPSI)
        # kalau COLOR SCHEMANYA 4 gridnya warna warni biar epilepsi ga karuan akwokwowow
        if color_schema == 4:
            screen.fill(COLOR_RANDOM_EPILEPSI1)
        else:
            screen.fill(color_screen_games)

        # ngambil score dan draw
        SCORE = str(GAMES.score)
        GAMES.draw()

        # font text bub
        diff = font.render(f"{difficulty}", True, "White")
        score = fontH2.render(SCORE, True, score_ct)
        back_home = font.render("Back to friends", True, menu_ct)
        reset_riyal = font.render("Reset as friends?", True, reset_ct)

        # draw ini (tes bisa ganti warna yawh)
        SUPERMAN_RECT = pygame.Rect(457, 0, 370, 810)
        DIBAWAH_SUPERMAN_RECT = pygame.Rect(0, 805, 821, 10)
        pygame.draw.rect(screen, color_btn_ghost, SUPERMAN_RECT)
        pygame.draw.rect(screen, COLOR_RANDOM_EPILEPSI2, DIBAWAH_SUPERMAN_RECT)

        # image blit hahahha curang
        # next shape make img awkowowk, kecuali difficulty-nya dinamis
        screen.blit(b_next_shape, (457, 50))
        screen.blit(f_Next_Shape, (490, 30))
        screen.blit(diff, (660, 35)) # diff dinamis
        GAMES.show_next_shape()

        # score make img awkowowk, kecuali skor-nya dinamis
        screen.blit(b_score, (457, 333))
        screen.blit(f_Score, (495, 315))
        screen.blit(score, (501, 370)) # score dinamis

        # how to play kalau newbie lol
        screen.blit(htp_guide, (467, 444))

        # button rill no fek fek (make fungsi dari pygamenya bukan make img akwokwowokwokw)
        # rect untuk button yawg
        menu_btn = pygame.Rect(525, 730, 225, 50)
        reset_btn = pygame.Rect(525, 670, 225, 50)

        pygame.draw.rect(screen, menu_c, menu_btn, border_radius=7)
        pygame.draw.rect(screen, "White", menu_btn, width=5, border_radius=7)
        screen.blit(back_home, (548, 743))

        pygame.draw.rect(screen, reset_c, reset_btn, border_radius=7)
        pygame.draw.rect(screen, "White", reset_btn, width=5, border_radius=7)
        screen.blit(reset_riyal, (535, 684))

        # untuk pause yabub
        if PAUSE == -1:
            go_sfx.play()
            pause_text1 = fontH2.render("PAUSE?", True, (255, 213, 0))
            pause_text2 = font.render("GINI DOANG SKILL LU?", True, (255, 213, 0))
            pause_text3 = font_SIZE_LIKE_YOUR_DIH.render("CUPU! Mainkan gamenya sekarang biar", True, (255, 213, 0))
            pause_text4 = font_SIZE_LIKE_YOUR_DIH.render("ga kena epilepsi", True, (255, 213, 0))
            pause_surface = pygame.Surface((821, 810), pygame.SRCALPHA)
            pause_rect = pygame.Rect(244, 310, 321, 145)

            COLOR_RANDOM_EPILEPSI1 = random.choice(COLOR_EPILEPSI)
            COLOR_RANDOM_EPILEPSI2 = random.choice(COLOR_EPILEPSI)

            pygame.draw.rect(screen, COLOR_RANDOM_EPILEPSI1, pause_rect, border_radius=13)
            pygame.draw.rect(screen, COLOR_RANDOM_EPILEPSI2, pause_rect, width=5, border_radius=13)
            pygame.draw.rect(pause_surface, (241, 55, 12, 77), (0, 0, 821, 810))
            screen.blit(pause_surface, (0, 0))
            screen.blit(pause_text1, (317, 336))
            screen.blit(pause_text2, (266, 380))
            screen.blit(pause_text3, (266, 407))
            screen.blit(pause_text4, (345, 421))


        # untuk game over
        if stateGO == 1:
            # upscore
            h_score = take_score()

            go_sfx.play()
            GO_TEXT = fontGO.render(GAMES.GO_text, True, (255, 45, 241))
            GO_surface = pygame.Surface((821, 810), pygame.SRCALPHA)
            go_rect = pygame.Rect(210, 330, 455, 125)
            GO_TEXT2 = font_SIZE_LIKE_YOUR_DIH.render("KLIK ENTER TUK CONTINUE", True, (255, 213, 0))

            COLOR_RANDOM_EPILEPSI1 = random.choice(COLOR_EPILEPSI)
            COLOR_RANDOM_EPILEPSI2 = random.choice(COLOR_EPILEPSI)

            pygame.draw.rect(GO_surface, (241, 55, 12, 77), (0, 0, 821, 810))
            pygame.draw.rect(screen, COLOR_RANDOM_EPILEPSI1, go_rect, border_radius=13)
            pygame.draw.rect(screen, COLOR_RANDOM_EPILEPSI2, go_rect, width=5, border_radius=13)

            screen.blit(GO_TEXT, (230, 350))
            screen.blit(GO_surface, (0, 0))
            screen.blit(GO_TEXT2, (334, 421))
            GAMES.GO_STATE = True

    # check event yg twejadi bubuww
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # kalau menu page yah manis
        if current_page_state == 1:
            # mouse diteken huh
            if event.type == pygame.MOUSEBUTTONDOWN:
                # klw startt diteken
                if start_btn.collidepoint(event.pos):
                    screen.blit(f_start_pressed, (324, 416)) 
                    current_page_state += 1
                    click_sfx.play()
                    break

                # volume oi
                if vol_rect.collidepoint(event.pos):
                    click_sfx.play()
                    vol *= -1

                if vol_process == "ON":
                    if vol_up.collidepoint(event.pos):
                        volume += 0.1
                        if volume > 1:
                            volume -= 0.1
                        pygame.mixer.music.set_volume(volume)
                        click_sfx.play()

                    if vol_down.collidepoint(event.pos):
                        volume -= 0.1
                        if volume < 0:
                            volume += 0.1
                        pygame.mixer.music.set_volume(volume)
                        click_sfx.play()

                # button colors oi
                for c in [c1_btn, c2_btn, c3_btn, c4_btn]:
                    if c1_btn.collidepoint(event.pos):
                        click_sfx.play()
                        color_schema = 1
                    
                    if c2_btn.collidepoint(event.pos):
                        click_sfx.play()
                        color_schema = 2
                    
                    if c3_btn.collidepoint(event.pos):
                        click_sfx.play()
                        color_schema = 3
                    
                    if c4_btn.collidepoint(event.pos):
                        click_sfx.play()
                        color_schema = 4

                    if easy_btn.collidepoint(event.pos):
                        click_sfx.play()
                        difficulty = "EASY"

                    if hard_btn.collidepoint(event.pos):
                        click_sfx.play()
                        difficulty = "HARD"
     
                    colors = Colors().get_colors(color_schema)
                    GRID = Grid(screen, colors, color_schema)
                    GAMES = Games(screen, colors, GRID, color_schema, audio, difficulty, h_score)


            # hovering yah bub
            if event.type == pygame.MOUSEMOTION:
                if start_btn.collidepoint(event.pos):
                    hover_strt = "YES KING"
                else:
                    hover_strt = "NO KING"
                    
                for c in [c1_btn, c2_btn, c3_btn, c4_btn]:
                    if c1_btn.collidepoint(event.pos):
                        hover_bclor1 = "YES KING"
                    else:
                        hover_bclor1 = "NO KING"
                
                    
                    if c2_btn.collidepoint(event.pos):
                        hover_bclor2 = "YES KING"
                    else:
                        hover_bclor2 = "NO KING"
                
                    
                    if c3_btn.collidepoint(event.pos):
                        hover_bclor3 = "YES KING" 
                    else:
                        hover_bclor3 = "NO KING"
                
                    
                    if c4_btn.collidepoint(event.pos):
                        hover_bclor4 = "YES KING" 
                    else:
                        hover_bclor4 = "NO KING"
                      
                    
                # difficulty
                if easy_btn.collidepoint(event.pos):
                    hover_easy = "YES KING"
                else:
                    hover_easy = "NO KING"

                if hard_btn.collidepoint(event.pos):
                    hover_hard = "YES KING"
                else:
                    hover_hard = "NO KING"
                    

        # kalau game page yah manis
        if current_page_state == 2:
            if GAMES.GO_STATE == True:
                stateGO = 1

            # mouse diteken huh
            if event.type == pygame.MOUSEBUTTONDOWN:
                # klw menu btn diteken
                if menu_btn.collidepoint(event.pos):
                    current_page_state -= 1
                    click_sfx.play()
                    break

                # klw reset duteken
                if reset_btn.collidepoint(event.pos):
                    colors = Colors().get_colors(color_schema)
                    GRID = Grid(screen, colors, color_schema)
                    GAMES = Games(screen, colors, GRID, color_schema, audio, difficulty, h_score)
                    click_sfx.play()
                     
            # hovering yah bub
            if event.type == pygame.MOUSEMOTION:
                if menu_btn.collidepoint(event.pos):
                    menu_c = "White"
                    menu_ct = (255, 212, 0)

                else:
                    menu_c = (255, 212, 0)
                    menu_ct = "White"

                if reset_btn.collidepoint(event.pos):
                    reset_c = "White"
                    reset_ct = (255, 0, 94)

                else:
                    reset_c = (255, 0, 94)
                    reset_ct = "White"

            # key diteken huh
            if event.type == pygame.KEYDOWN:
                GAMES.draw()

                if event.key == pygame.K_UP and PAUSE == 1 and stateGO == 0:
                    GAMES.rotation_move()
                    rotations_sfx.play()
                if event.key == pygame.K_DOWN and PAUSE == 1 and stateGO == 0:
                    GAMES.down_move()
                if event.key == pygame.K_RIGHT and PAUSE == 1 and stateGO == 0:
                    GAMES.right_move()
                if event.key == pygame.K_LEFT and PAUSE == 1 and stateGO == 0:
                    GAMES.left_move()
                    
                # paustad oi
                if event.key == pygame.K_SPACE and stateGO == 0: 
                    click_sfx.play()
                    PAUSE *= -1
                # reset oi
                if event.key == pygame.K_RETURN and PAUSE == 1: 
                    stateGO = 0
                    colors = Colors().get_colors(color_schema)
                    GRID = Grid(screen, colors, color_schema)
                    GAMES = Games(screen, colors, GRID, color_schema, audio, difficulty, h_score)
                    click_sfx.play()

            # klw bukan pause dan bukan game over shapenya gerka yawh oi
            if event.type == GAME_UPDATE and PAUSE == 1 and stateGO == 0:
                GAMES.down_move()

    # update gamenya
    pygame.display.update()

# exiteu
pygame.quit()
sys.exit()