import pygame as pg
import sys

# Konstanter
WIDTH = 1000  
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60 

pg.init()
surface = pg.display.set_mode(SIZE)

clock = pg.time.Clock()

backgroundImg = pg.image.load("replaybilder/gress.png")
backgroundImg = pg.transform.scale(backgroundImg, (SIZE))


# klasse for karakteren
class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        
        self.characterImg = pg.image.load(image)
        
        #får høyden og bredden til karakteren
        self.characterRect = self.characterImg.get_rect()
        self.h = self.characterRect.height
        self.w = self.characterRect.width
        
        self.vx = 0
        self.vy = 0
        
        self.hidden = False
    
    def draw(self):
        surface.blit(self.characterImg, (self.x, self.y))
        
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
      
      
    def move(self):
        self.vx = 0
        self.vy = 0
        
        keys  = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -10
            
        if keys[pg.K_RIGHT]:
            self.vx = 10
        
        if keys[pg.K_UP]:
            self.vy = -10
            
        if keys[pg.K_DOWN]:
            self.vy = 10

#lager en klasse for rektangler/firkanter
class Rektangel:
    #konstruktør
    def __init__(self, x, y, w, h, image, scale):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.scale = scale
        #henter inn bildet til objektet
        self.rektangelImg = pg.image.load(self.image)
        #skalerer objektet
        self.rektangelImg = pg.transform.scale(self.rektangelImg, (self.w * self.scale, self.h * self.scale))
        #lager et rektangel rundt objektet
        self.rektangelRect = self.rektangelImg.get_rect()
        #henter x- og y-verdien til det skalerte objektet (brukt i kollisjonene)
        self.rektangelRect.x = x
        self.rektangelRect.y = y
        #henter høyden og bredden til det skalerte objektet
        self.h = self.rektangelRect.height
        self.w = self.rektangelRect.width
    
    #metode som tegner objektet
    def draw(self):
        surface.blit(self.rektangelImg, (self.x, self.y))



hatman = Character(200, 300, "replaybilder/hatman.png")
honsehus = Rektangel(600,300,50,50,"replaybilder/honsehus.png", 4)


def collision(hatman, honsehus):
    if hatman.x + hatman.w >= honsehus.x and hatman.x <= honsehus.x + honsehus.w:
        if hatman.y + hatman.h >= honsehus.y and hatman.y <= honsehus.y + honsehus.h:
            hatman.hidden = True
            


run = True

while run:
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
        
    surface.blit(backgroundImg, (0,0))
    
    collision(hatman, honsehus)
        
    if not hatman.hidden:
        hatman.update()
        hatman.move()
        hatman.draw()
    
    honsehus.draw()
    
    pg.draw.rect(surface, (255,0,0), pg.Rect(hatman.x, hatman.y, hatman.w, hatman.h), 3)
    pg.draw.rect(surface, (255,0,0), pg.Rect(honsehus.x, honsehus.y, honsehus.w, honsehus.h), 3)

    pg.display.flip()

pg.quit()
sys.exit()





















"""
def gameOver():
    global run
    if gameover:
        keys  = pg.key.get_pressed()
        if keys[pg.K_RETURN]:
            run = False
            """






"""
setup() = True


def setup():
    
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
        
    surface.blit(backgroundImg, (0,0))
    
    
    
    honsehus.draw()
    
    pg.draw.rect(surface, (255,0,0), pg.Rect(hatman.x, hatman.y, hatman.w, hatman.h), 3)
    pg.draw.rect(surface, (255,0,0), pg.Rect(honsehus.x, honsehus.y, honsehus.w, honsehus.h), 3)

    pg.display.flip()

    
def main_loop():
    while True:
        collision(hatman, honsehus)
        
        if not hatman.hidden:
            hatman.update()
            hatman.move()
            hatman.draw()
            
        
        
        if gameOver():
            break
    
def shut_down():
    while True:
        # Avslutter pygame
        pg.quit()
        sys.exit()



run = True

# Spill-løkken
while run:
    setup()
    main_loop()
    shut_down()
"""






