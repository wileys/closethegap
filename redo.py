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

bgimg = pg.image.load("images/pixelpaper.jpg").convert()
bgimg = pg.transform.scale(bgimg, (800, 600))


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

    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        p2 = Platform(370, 300, 150, 20)
        p3 = Platform(595, 425, 150, 20)
        p4 = Platform(145, 425, 150, 20)
        p5 = Platform(0, 500, 50, 100)
        self.all_sprites.add(p2)
        self.platforms.add(p2)
        self.all_sprites.add(p3)
        self.platforms.add(p3)
        self.all_sprites.add(p4)
        self.platforms.add(p4)
        self.all_sprites.add(p5)
        self.platforms.add(p5)
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
        #game over
        if self.player.rect.bottom > HEIGHT:
            self.playing = False 
            pg.time.delay(100)
        

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
        # *after* drawing everything, flip the display
        pg.display.flip()

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
                if event.type == pg.KEYUP:
                    waiting = False

    def start_screen(self):
        self.screen.fill(WHITE)
        self.draw_text(TITLE, 75, BLACK, WIDTH/2,125)
        self.draw_text("Use left and right arrows keys to move forward and back.", 30, BLACK, WIDTH/2, 400)
        self.draw_text("Use up arrow key to jump.", 30, BLACK, WIDTH/2, 450)
        self.draw_text("Press any key to start!", 30, BLACK, WIDTH/2, HEIGHT/2)
        pg.display.flip()
        self.wait_for_key()

    # def go_screen():


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((70, 70))
        sprite = pg.image.load("images/girl.png").convert_alpha()
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
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

g = Game()
g.start_screen()

while g.running:  
    g.new()
    # g.go_screen()

pg.quit()