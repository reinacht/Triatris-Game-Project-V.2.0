

# x = 250
# y = 433
# x_closed = 0
# y_closed = 0
# size = 50
# k = 0
# percent_loading = 0
# start_zeit = pygame.time.get_ticks()

#     if current_page_state == 0:
#         screen.fill(color_screen_games)

#         # colors
#         C_loading_rand1 = random.choice(COLOR_EPILEPSI)
#         C_loading_rand2 = random.choice(COLOR_EPILEPSI)

#         C_loading_rand1 = COLOR_EPILEPSI[4]
#         C_loading_rand2 = COLOR_EPILEPSI[5]

#         C_loading_rand3 = "Black"
#         if C_loading_rand1 == C_loading_rand2:
#             C_loading_rand2 = random.choice(COLOR_EPILEPSI)
    

#         # bar loadingnya
#         bar_rect = pygame.Rect(250, 430, 298, 55)
#         pygame.draw.rect(screen, (255, 255, 255), bar_rect, border_radius=7)
#         pygame.draw.rect(screen, C_loading_rand3, bar_rect, width=5, border_radius=7)


#         # event quit kek biasa maniezz
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#             if event.type == GAME_UPDATE:
#                 print("LOADING")
        
#         # block dropnya oi
#         for i in range(1, 9):
#             clock.tick(120) 
#             loading_block = pygame.Rect(x, y, size, size)
#             percent_loading_text = fontH2.render(f"{int(percent_loading)}%", True, "White")

#             # closed_block = pygame.Rect(x_closed, y_closed, size, size)
#             # pygame.draw.rect(screen, "Purple", closed_block, border_radius=7)

#             # nembus ke kanan
#             if i == 8 and (x > 454 or k == 1):
#                 pygame.draw.rect(screen, C_loading_rand1, loading_block, border_radius=7)
#                 pygame.draw.rect(screen, C_loading_rand2, loading_block, width=7, border_radius=7)
#                 k = 1
#                 x -= size
#                 percent_loading += 1

#                 if x < 250:
#                     k = 0
#                     x += size
    
#             # nembus ke kiri (mulai dari kiri kocak kek bahasa arab)
#             if i == 8 and k == 0:
#                 pygame.draw.rect(screen, C_loading_rand1, loading_block, border_radius=7)
#                 pygame.draw.rect(screen, C_loading_rand2, loading_block, width=7, border_radius=7)
#                 x += size
#                 percent_loading += 1

#             if percent_loading > 100:
#                 percent_loading = 100

#             screen.blit(percent_loading_text, (350, 490))


#         # ketika 100 persen yah sayanggg dan dia draw baru hhehe
#         if percent_loading == 100:
#             end_zeit = pygame.time.get_ticks()
#             delay1 = end_zeit - start_zeit

#             # bar loadingnya
#             bar_rect = pygame.Rect(250, 430, 298, 55)
#             pygame.draw.rect(screen, (255, 255, 0), bar_rect, border_radius=7)
#             pygame.draw.rect(screen, C_loading_rand3, bar_rect, width=5, border_radius=7)
        


#             print(f"time str : {start_zeit}, time end : {end_zeit}")
#             print(f"time delay : {delay1}")


#             # pernah ngga ready?
#             if delay1 >= 6600:
#                 pause_surface = pygame.Surface((821, 810), pygame.SRCALPHA)
#                 pygame.draw.rect(pause_surface, (241, 55, 12, 77), (0, 0, 821, 810))
#                 screen.blit(pause_surface, (0, 0))

#                 next_zeit = pygame.time.get_ticks()
#                 delay2 = next_zeit - start_zeit

#                 if delay1 >= 6900:
#                     current_page_state += 1
#                     pygame.mixer.music.play(-1) 