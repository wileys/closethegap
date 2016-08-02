def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()




PURPLE = (51, 0, 102)
MAG = (153, 0, 0)
light_PURPLE = (76, 0, 153)
light_MAG = (204, 0, 0)
def game_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            print (event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(WHITE)
        largeText = pygame.font.Font(default_font, 100)   
        TextSurf,TextRect = text_objects("Close The Gap", largeText) 
        TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
        screen.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        if 150+150 > mouse[0] > 150 and 450+75 > mouse[1] > 450:
            pygame.draw.rect(screen, light_PURPLE, (150,450,150,75))
        else:
            pygame.draw.rect(screen, PURPLE, (150,450,150,75))

        if 500+150 > mouse[0] > 500 and 450+75 > mouse[1] > 450:
            pygame.draw.rect(screen, light_MAG, (500,450,150,75))
        else:
            pygame.draw.rect(screen, MAG,(500,450,150,75)

        # pygame.screen.update()
        # clock.tick(15)