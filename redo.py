import pygame as pg
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
GREY = (105, 105, 105)
MAROON = (23, 26, 41)


FPS = 60

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 16

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

TITLE = "CLOSE THE GAP"

pg.display.set_caption("CLOSE THE GAP") 

FONT_NAME = 'arial'
vec = pg.math.Vector2

bgimg = pg.image.load("images/bgimg.png").convert()
bgimg = pg.transform.scale(bgimg, (800, 600))

definition = pg.image.load("images/definition.png").convert_alpha()
congratz = pg.image.load("images/congratz.png").convert_alpha()


titlescreen = pg.image.load("images/titlescreen.png").convert()
latina = pg.image.load("images/lscreen.png").convert()
whitewoman = pg.image.load("images/wwscreen.png").convert()
asianamerican = pg.image.load("images/aascreen.png").convert()
whitemale = pg.image.load("images/wmscreen.png").convert()
nativehi = pg.image.load("images/nhscreen.png").convert()
amindian = pg.image.load("images/aiscreen.png").convert()
afam = pg.image.load("images/afascreen.png").convert()


pg.font.init()
default_font = pg.font.get_default_font()
font_renderer = pg.font.Font(default_font, 30)

space_KEY= pg.K_SPACE

# To create a surface containing `Some Text`

class SnowFlake():
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos 

    def fall(self, speed):
        self.y_pos += speed

    def draw(self):
        pg.draw.rect(screen, WHITE, (self.x_pos, self.y_pos, 5, 5), 1)



class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT_NAME)
        self.score = 0
        self.level_number = 1

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        if self.level_number == 1:
            p5 = Platform(0, 500, 50, 100)
            p2 = Platform(50, 550, 800, 50)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.coins = pg.sprite.Group()
            c1 = Coin(120,520)
            c2 = Coin(190, 520)
            c3 = Coin(260, 520)
            c4 = Coin(330, 520)
            c5 = Coin(400, 520)
            c6 = Coin(470, 520)
            c7 = Coin(540, 520)
            c8 = Coin(610, 520)
            c9 = Coin(680, 520)
            c10 = Coin(750, 520)
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)

        
        if self.level_number == 2:
            p2 = Platform(370, 300, 150, 20)
            p3 = Platform(595, 425, 110, 20)
            p4 = Platform(145, 425, 150, 20)
            p5 = Platform(0, 500, 50, 100)
            p6 = Platform(750, 500, 50, 100)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p6)
            self.platforms.add(p6)
            self.coins = pg.sprite.Group()
            c1 = Coin(390,270)
            c2 = Coin(470, 270)
            c3 = Coin(250, 390)
            c4 = Coin(290, 320)
            c5 = Coin(170, 390)#1
            c6 = Coin(600, 390)
            c7 = Coin(680, 390)
            c8 = Coin(80, 425)
            c9 = Coin(560, 320)
            c10 = Coin(765, 470)
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)


        if self.level_number == 3:
            p4 = Platform(260, 300, 80, 20)#3rd platform
            p5 = Platform(400, 425, 80, 20)#4th platform 
            p3 = Platform(120, 425, 80, 20) #2nd platform 
            p2 = Platform(0, 500, 50, 100) #1st
            p6 = Platform(750,500,50,100) #6th
            p7 = Platform(625,500,80,20)#5th platform
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p6)
            self.platforms.add(p6)
            self.all_sprites.add(p7)
            self.platforms.add(p7)
            self.coins = pg.sprite.Group()
            c1 = Coin(290,260) #3rd 
            c2 = Coin(395, 300)#4th
            c3 = Coin(125, 385)#1st
            c4 = Coin(200, 300)#2nd
            c5 = Coin(415, 390)#5th
            c6 = Coin(500, 350)#6th
            c7 = Coin(625, 450)#7th
            c8 = Coin(670, 400)#8th
            c9 = Coin(175, 385)#9th
            c10 = Coin(775, 450)#10th
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)



        if self.level_number == 4:
            p2 = Platform(265, 320, 80, 20)
            p3 = Platform(440, 175, 100, 20)
            p4 = Platform(115, 400, 70, 20)
            p5 = Platform(0, 500, 50, 100)
            p6 = Platform(750, 500, 50, 100)
            p7 = Platform (600, 425, 100, 20)
            p8 = Platform (285, 100, 40, 20)
            p9 = Platform (500, 355, 100, 20)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p6)
            self.platforms.add(p6)
            self.all_sprites.add(p7)
            self.platforms.add(p7)
            self.all_sprites.add(p8)
            self.platforms.add(p8)
            self.all_sprites.add(p9)
            self.platforms.add(p9)
            self.coins = pg.sprite.Group()
            c1 = Coin(290, 70)#4 upper coin
            c2 = Coin(475, 140)#7
            c3 = Coin(290, 280)#3
            c4 = Coin(170, 370)#2
            c5 = Coin(360, 170)#5
            c6 = Coin(610, 295)#6
            c7 = Coin(645, 395)#9
            c8 = Coin(100,370)#1
            c9 = Coin(565, 230)#8
            c10 = Coin(765, 460)#10
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)


        if self.level_number == 5:
            p2 = Platform(150, 510, 30, 20)
            p3 = Platform(450, 345, 70, 20)
            p4 = Platform(630, 100, 30, 20)
            p5 = Platform(0, 500, 50, 100)
            p6 = Platform(750, 500, 50, 100)
            p7 = Platform(300, 430, 50, 20)
            p8 = Platform(540, 200, 50, 20)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p6)
            self.platforms.add(p6)
            self.all_sprites.add(p7)
            self.platforms.add(p7)
            self.all_sprites.add(p8)
            self.platforms.add(p8)
            self.coins = pg.sprite.Group()
            c1 = Coin(390,270)
            c2 = Coin(470, 270)
            c3 = Coin(250, 320)
            c4 = Coin(290, 400)
            c5 = Coin(170, 390)
            c6 = Coin(600, 190)
            c7 = Coin(680, 90)
            c8 = Coin(80, 425)
            c9 = Coin(560, 320)
            c10 = Coin(765, 470)
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)


       

        if self.level_number == 6:
            p2 = Platform(350, 300, 30, 20)
            p3 = Platform(575, 425, 50, 20)
            p4 = Platform(185, 425, 30, 20)
            p5 = Platform(0, 500, 50, 100)
            p6 = Platform(750, 500, 50, 100)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p6)
            self.platforms.add(p6)
            self.coins = pg.sprite.Group()
            c1 = Coin(360,270)
            c2 = Coin(400, 250)
            c3 = Coin(190, 280)
            c4 = Coin(190, 370)#3
            c5 = Coin(775, 400)#10
            c6 = Coin(600, 390)
            c7 = Coin(680, 350)
            c8 = Coin(80, 425)#1
            c9 = Coin(560, 320)
            c10 = Coin(765, 300)
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)


        
        if self.level_number == 7:
            p2 = Platform(370, 300, 70, 20)
            p3 = Platform(575, 305, 50, 20)
            p4 = Platform(185, 425, 20, 20)
            p7 = Platform(185, 250, 20, 20)
            p5 = Platform(0, 500, 50, 100)
            p6 = Platform(750, 500, 50, 100)
            self.all_sprites.add(p2)
            self.platforms.add(p2)
            self.all_sprites.add(p3)
            self.platforms.add(p3)
            self.all_sprites.add(p4)
            self.platforms.add(p4)
            self.all_sprites.add(p5)
            self.platforms.add(p5)
            self.all_sprites.add(p6)
            self.platforms.add(p6)
            self.all_sprites.add(p7)
            self.platforms.add(p7)
            self.coins = pg.sprite.Group()
            c1 = Coin(390,270)#4
            c2 = Coin(430, 220)#5
            c3 = Coin(180, 200)
            c4 = Coin(290, 260)#3
            c5 = Coin(180, 390)#2
            c6 = Coin(775, 450)#7
            c7 = Coin(680, 290)#8
            c8 = Coin(80, 425)#1
            c9 = Coin(560, 250)#6
            c10 = Coin(765, 360)#9
            self.all_sprites.add(c1)
            self.coins.add(c1)
            self.all_sprites.add(c2)
            self.coins.add(c2)
            self.all_sprites.add(c3)
            self.coins.add(c3)
            self.all_sprites.add(c4)
            self.coins.add(c4)
            self.all_sprites.add(c5)
            self.coins.add(c5)
            self.all_sprites.add(c6)
            self.coins.add(c6)
            self.all_sprites.add(c7)
            self.coins.add(c7)
            self.all_sprites.add(c8)
            self.coins.add(c8)
            self.all_sprites.add(c9)
            self.coins.add(c9)
            self.all_sprites.add(c10)
            self.coins.add(c10)

        
        if self.level_number == 8:
            p1 = Platform(0, 530, 800, 70)
            self.all_sprites.add(p1)
            self.platforms.add(p1)


        #white_male_platform = Platform(70, 800, 730, 20)
        self.run()


    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
            hits2 = pg.sprite.spritecollide(self.player, self.coins, True)
            if hits2:
                self.score += 10



        #levels
        if self.player.rect.bottom > HEIGHT:
            self.playing = False 
            pg.time.delay(100)
            self.score = 0

        if self.level_number == 1 and self.score == 100:
                g.level_1_stats()
                # pg.time.delay(5000)
                self.level_number = 2
                self.score = 0
        
        elif self.level_number == 2 and self.score == 100:
                g.level_2_stats()
                self.level_number = 3
                self.score = 0


        elif self.level_number == 3 and self.score == 100:
                g.level_3_stats()
                self.level_number = 4
                self.score = 0

        elif self.level_number == 4 and self.score == 100:
                g.level_4_stats()
                self.level_number = 5
                self.score = 0

        elif self.level_number == 5 and self.score == 100:
                g.level_5_stats()
                self.level_number = 6
                self.score = 0

        elif self.level_number == 6 and self.score == 100:
                g.level_6_stats()
                self.level_number = 7
                self.score = 0

        elif self.level_number == 7 and self.score == 100:
                g.level_7_stats()
                self.level_number = 8
                self.score = 0



        

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        screen.blit(bgimg, [0,0])
        self.all_sprites.draw(self.screen)

        text = font_renderer.render(
            "SCORE: "+ str(self.score), True, BLACK)

        text2 = font_renderer.render(
            "LEVEL: " + str(self.level_number), True, BLACK)

        if g.level_number == 8:
            x = random.randint(0, 800)
            y = 0
            snow_list.append(SnowFlake(x, y))
            for snowflake in snow_list: 
                snowflake.draw()
                snowflake.fall(3)
            screen.blit(congratz, (0, 70))
            screen.blit(definition, (100, 300))
            self.draw_text("You have broken the glass ceiling!! </sexism>", 30, BLACK, WIDTH/2, HEIGHT/4 +50)

        screen.blit(
            text,  # The text to render
            (10,10))  # Where on the destination surface to render said font
        # *after* drawing everything, flip the display

        screen.blit(
            text2,  # The text to render
            (10,50))  # Where on the destination surface to render said font
        # *after* drawing everything, flip the display

        pg.display.flip()


    def show_start_screen(self):
        # game splash/start screen
        pass
    #def show_instructions_screen(self):
        #pass


    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP and event.key == pg.K_SPACE:
                    waiting = False

    # def wait_for_K_SPACE(self):
    #     waiting = True
    #     while waiting:
    #         self.clock.tick(30)

    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 waiting = False
    #                 self.running = False
    #             if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
    #                 waiting = False

    def start_screen(self):
        screen.blit(titlescreen, (0,0))
        pg.display.flip()
        self.wait_for_key()

    def instructions_screen(self):
        self.screen.fill(WHITE)
        self.draw_text("INSTRUCTIONS", 30, BLACK, WIDTH/2, 150)
        self.draw_text("USE LEFT AND RIGHT ARROW KEYS TO MOVE FORWARD AND BACK. ", 24, BLACK, WIDTH/2, 250)
        self.draw_text("USE UP ARROW KEY TO JUMP", 24, BLACK, WIDTH/2, 300)
        self.draw_text("COLLECT ALL OF THE COINS TO MOVE TO THE NEXT LEVEL AND CLOSE THE GAP!", 24, BLACK, WIDTH/2, 350)
        self.draw_text("Press the space key to start.", 24, BLACK, WIDTH/2, 450)
        pg.display.flip()
        self.wait_for_key()

    def level_1_stats(self):
        screen.blit(whitemale, (0,0))
        pg.display.flip()
        self.wait_for_key()
        

    def level_2_stats(self):
        screen.blit(asianamerican, (0,0))
        pg.display.flip()
        self.wait_for_key()

    def level_3_stats(self):
        screen.blit(whitewoman, (0,0))
        pg.display.flip()
        self.wait_for_key()

    def level_4_stats(self):
        screen.blit(nativehi, (0,0))
        pg.display.flip()
        self.wait_for_key()

    def level_5_stats(self):
        screen.blit(afam, (0,0))
        pg.display.flip()
        self.wait_for_key()

    def level_6_stats(self):
        screen.blit(amindian, (0,0))
        pg.display.flip()
        self.wait_for_key()

    def level_7_stats(self):
        screen.blit(latina, (0,0))
        pg.display.flip()
        self.wait_for_key()



    # def go_screen():


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((70, 70))
        if g.level_number ==1:
            sprite = pg.image.load("images/girl.png").convert_alpha()
        if g.level_number ==2:
            sprite = pg.image.load("images/girl2.png").convert_alpha()
        if g.level_number ==3:
            sprite = pg.image.load("images/girl3.png").convert_alpha()
        if g.level_number ==4:
            sprite = pg.image.load("images/girl4.png").convert_alpha()
        if g.level_number ==5:
            sprite = pg.image.load("images/girl5.png").convert_alpha()
        if g.level_number ==6:
            sprite = pg.image.load("images/girl6.png").convert_alpha()
        if g.level_number ==7:
            sprite = pg.image.load("images/girl7.png").convert_alpha()
        if g.level_number ==8:
            sprite = pg.image.load("images/girl8.png").convert_alpha()
        sprite = pg.transform.scale(sprite, (70, 70))

        self.image.set_colorkey((0,0,0))
        self.image.blit(sprite, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(30, 420)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP


    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(MAROON)
        self.image.fill((23, 26, 41))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((24, 24))
        pg.draw.circle(self.image, YELLOW, (12,12), 12, 0)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


g = Game()
g.start_screen()
g.instructions_screen()
speed = 3
snow_list = []




while g.running:  
    g.new()

    screen.blit(bgimg, [0,0])
    pg.display.flip()
    # g.show_go_screen()





pg.quit()
