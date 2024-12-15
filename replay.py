# hatman animasjon av z11z11 hentet fra https://opengameart.org/content/man-walking-animation


import pygame as pg
import sys

# Konstanter
WIDTH = 1000  
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
FPS = 60


BLUE = (80,210,240)
WHITE = (255,255,255)


pg.init()
surface = pg.display.set_mode(SIZE)

clock = pg.time.Clock()

backgroundImg = pg.image.load("bilder/gress.png")
backgroundImg = pg.transform.scale(backgroundImg, (SIZE))

font = pg.font.SysFont("Arial",48)


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



hatman = Character(200, 300, "bilder/hatman.png")
honsehus = Rektangel(600,300,50,50,"bilder/honsehus.png", 4)

def gameRun():
    
    def collision(hatman, honsehus):
        if hatman.x + hatman.w >= honsehus.x and hatman.x <= honsehus.x + honsehus.w:
            if hatman.y + hatman.h >= honsehus.y and hatman.y <= honsehus.y + honsehus.h:
                hatman.hidden = True
                
                textPug = font.render("Du vinner! trykk enter for å fortsette", True, WHITE,BLUE)
                textRectPug = textPug.get_rect()
                textRectPug.center = (WIDTH // 2, HEIGHT // 2)
                
                surface.blit(textPug, textRectPug)
    
    
    if not hatman.hidden:
        hatman.update()
        hatman.move()
        hatman.draw()
        
    honsehus.draw()
    
    pg.draw.rect(surface, (255,0,0), pg.Rect(hatman.x, hatman.y, hatman.w, hatman.h), 3)
    pg.draw.rect(surface, (255,0,0), pg.Rect(honsehus.x, honsehus.y, honsehus.w, honsehus.h), 3)
    
    collision(hatman, honsehus)






"""
def gameOver():
    global run
    
    keys  = pg.key.get_pressed()
    if keys[pg.K_RETURN]:
        run = False"""



def infoScreen():
    textInfo = font.render("Trykk mellomrom for å starte", True, WHITE,BLUE)
    textInfo2 = font.render("beveg deg med piltaster", True, WHITE, BLUE)
    textRectInfo = textInfo.get_rect()
    textRectInfo2 = textInfo2.get_rect()
    textRectInfo.center = (WIDTH // 2, HEIGHT // 2 - 40)
    textRectInfo2.center = (WIDTH // 2, HEIGHT // 2 + 40)
    
    surface.blit(textInfo, textRectInfo)
    surface.blit(textInfo2, textRectInfo2)

def endScreen():
    textEnd = font.render("Spillet er over", True, WHITE,BLUE)
    textEnd2 = font.render("Trykk space for å spille igjen, enter for å avslutte", True, WHITE, BLUE)
    textRectEnd = textEnd.get_rect()
    textRectEnd2 = textEnd2.get_rect()
    textRectEnd.center = (WIDTH // 2, HEIGHT // 2 - 40)
    textRectEnd2.center = (WIDTH // 2, HEIGHT // 2 + 40)
    
    surface.blit(textEnd, textRectEnd)
    surface.blit(textEnd2, textRectEnd2)
    

run = True
start = True
game = False
gameover = False

# Spill-løkken
while run:
    clock.tick(FPS)
    
    while start:
        surface.blit(backgroundImg, (0,0))
        infoScreen()
         
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                start = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game = True
                    start = False
       
        pg.display.flip()
    
    
    while game:
        surface.blit(backgroundImg, (0,0))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                game = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    game = False
                    gameover = True
                
        
        gameRun()
        

        
        pg.display.flip()
        
        
    
    
    while gameover:
        surface.blit(backgroundImg, (0,0))
        endScreen()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                gameover = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    hatman.x = 200
                    hatman.y = 300
                    honsehus.x = 600
                    honsehus.y = 300
                    hatman.hidden = False
                    game = True
                    gameover = False
                    
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    gameover = False
                    run = False
        
        pg.display.flip()
        


# Avslutter pygame
pg.quit()
sys.exit()



# funksjon newgame som kaller nytt spill hver gang vi kjører start, putte hele game_version inni der
