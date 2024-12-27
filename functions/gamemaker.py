# importerer pygame-biblioteket
import pygame as pg
# importerer randint og randrange funksjonene fra random-biblioteket
from random import randint

from classes.SpriteSheetPug import SpriteSheetPug
from classes.SpriteSheetChick import SpriteSheetChick
from classes.Pug import Pug
from classes.Chick import Chick
from classes.Rectangle import Rectangle

#henter først spritesheetet med 12 pug-bilder (convert_alpha gjør at bildet bruker samme pixel-format som skjermen)
sprite_sheet_image = pg.image.load("bilder/pug.png").convert_alpha()
#sender spritesheetet gjennom SpriteSheet-klassen, slik at det blir skalert og delt opp i 12 enkeltbilder
sprite_sheet = SpriteSheetPug(sprite_sheet_image)

#henter spritesheetet med 12 kylling-bilder
sprite_sheet_image2 = pg.image.load("bilder/chick.png").convert_alpha()
#skalerer og deler opp spritesheetet i 12 enkeltbilder
sprite_sheet2 = SpriteSheetChick(sprite_sheet_image2)





game_version = randint(1,5)

def gamemaker():
    global hoyballer, lyn, pug, chick, honsehus
    global play_cackling, play_barking
    #lager en tom liste for høyballene
    hoyballer = []
    #lager en tom liste for lynene
    lyn = []

    play_cackling = False
    play_barking = False
    
    pg.mixer.music.play()

    #lager en variabel som tilfeldig sier hvilken av spillversjonene som skal kjøres
    #game_version = randint(1,5)
    #game_version = 5

    #spillversjon 1
    if game_version == 1:
        #lager høyballobjekter
        hoyballer.append(Rectangle(100*8, 50, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*6, 100 + 50, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*4, 100*2 + 50, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*2, 100*3 + 45, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*7, 100*4 + 45, 64, 64, "bilder/hoyball.png", 1.5625))
        
        #lager flere høyballer samtidig, i rekker eller kolonner
        for i in range(2):
            hoyballer.append(Rectangle(100*8 + i*100, 100 + 50, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*6 + i*100, 100*3 + 45, 64, 64, "bilder/hoyball.png", 1.5625))
            
        for i in range(3):
            hoyballer.append(Rectangle(100*4 + i*100, 50, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*2 + i*100, 100*4 + 45, 64, 64, "bilder/hoyball.png", 1.5625))
        
        
        #pug objekt
        pug = Pug(300, 190, "bilder/pug.png", "right", 32, 1.5, sprite_sheet)

        #kylling objekt
        chick = Chick(910, 500, "bilder/chick.png", "left", 26, 1.8, sprite_sheet2)

        #hønsehus objekt
        honsehus = Rectangle(50,40,50,50, "bilder/honsehus.png", 4)
        
        #lyn objekt
        lyn.append(Rectangle(435,375,13,22,"bilder/lyn.png",1.8))
        lyn.append(Rectangle(90,430,13,22,"bilder/lyn.png",1.8))
        lyn.append(Rectangle(835,5,13,22,"bilder/lyn.png",1.8))
        
        
        
        
    #spillversjon 2 
    if game_version == 2:
        #høyballobjekter
        hoyballer.append(Rectangle(100, 100*3, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*2, 100, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*3, 100, 64, 64, "bilder/hoyball.png", 1.5625))

        for i in range(2):
            hoyballer.append(Rectangle(100*3, 100*3 + i*100, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*5, 100*2 + i*100, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*6, 100*3 + i*100, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*8, 100*4 + i*100, 64, 64, "bilder/hoyball.png", 1.5625))

        
        #pug objekt
        pug = Pug(650, 120, "bilder/pug.png", "left", 32, 1.5, sprite_sheet)

        #kylling objekt
        chick = Chick(40, 500, "bilder/chick.png", "right", 26, 1.8, sprite_sheet2)

        #hønsehus objekt
        honsehus = Rectangle(760,40,50,50, "bilder/honsehus.png", 4)

        #lyn objekter
        lyn.append(Rectangle(435,340,13,22,"bilder/lyn.png",1.5))
        lyn.append(Rectangle(630,540,13,22,"bilder/lyn.png",1.5))
        lyn.append(Rectangle(85,75,13,22,"bilder/lyn.png",1.5))
        
        
            

    # spillversjon 3
    if game_version == 3:
        #høyballobjekter
        hoyballer.append(Rectangle(100*3, 100, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*5, 0, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*8, 100*2, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*6, 100*4, 64, 64, "bilder/hoyball.png", 1.5625))
        
        for i in range(2):
            hoyballer.append(Rectangle(100, 100*3 + i*100, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*2, 100 + i*100*3, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*7, 100 + i*100, 64, 64, "bilder/hoyball.png", 1.5625))

        for i in range(3):
            hoyballer.append(Rectangle(100*4, 600-100*(i+1), 64, 64, "bilder/hoyball.png", 1.5625))
            

        #pug objekt
        pug = Pug(100*5 + 30, 100*5 + 30, "bilder/pug.png", "up", 32, 1.7, sprite_sheet)

        #kylling objekt
        chick = Chick(34, 34, "bilder/chick.png", "right", 26, 2, sprite_sheet2)

        #hønsehus objekt
        honsehus = Rectangle(800,400,50,50, "bilder/honsehus.png", 4)

        #lyn objekt
        lyn.append(Rectangle(280,270,13,22,"bilder/lyn.png",2))
        lyn.append(Rectangle(550,200,13,22,"bilder/lyn.png",2))




    #spillversjon 4
    if game_version == 4:
        #høyballobjekter
        hoyballer.append(Rectangle(100*2, 0, 64, 64, "bilder/hoyball.png", 1.5625))
        hoyballer.append(Rectangle(100*5, 100 * 3, 64, 64, "bilder/hoyball.png", 1.5625))
        
        for i in range(2):
            hoyballer.append(Rectangle(100 + i*100, 100*2, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*4 + i*100, 100*4, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*7, 100 * 3 + i * 100, 64, 64, "bilder/hoyball.png", 1.5625))
            hoyballer.append(Rectangle(100*8, 100 * 2 + i * 100, 64, 64, "bilder/hoyball.png", 1.5625))
            
        for i in range(3):
            hoyballer.append(Rectangle(100*4 + i*100, 100, 64, 64, "bilder/hoyball.png", 1.5625))


        #pug objekt
        pug = Pug(100*2.8, 100*3.5, "bilder/pug.png", "right", 32, 1.5, sprite_sheet)

        #kylling objekt
        chick = Chick(910, 34, "bilder/chick.png", "left", 26, 1.8, sprite_sheet2)

        #hønsehus objekt
        honsehus = Rectangle(50,350,50,50, "bilder/honsehus.png", 4)

        #lyn objekt
        lyn.append(Rectangle(230,125,13,22,"bilder/lyn.png",2))
        lyn.append(Rectangle(630,300,13,22,"bilder/lyn.png",2))
        lyn.append(Rectangle(880,480,13,22,"bilder/lyn.png",2))




    #spillversjon 5
    if game_version == 5:
        #høyballobjekter
        hoyballer.append(Rectangle(64*10, 64*5, 64,  64, "bilder/hoyball.png", 1))
        hoyballer.append(Rectangle(64*14 - 5, 64*2, 64,  64, "bilder/hoyball.png", 1))
        
        for i in range(2):
            hoyballer.append(Rectangle(0, 64*3 + 64*i, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64, 64*3 + 64*i, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*2, 64*6 + 64*i, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*5, 64*6 + 64*i, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*3 + i*64, 64*7, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*4, 64*3 + i*64, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*10 + i*64, 64, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*10 + i*64, 64*4, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*8, 64*3 + i*64, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*7, 64*6 + i*64, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*2, i*64, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*13 - 5, 64 + i*64, 64,  64, "bilder/hoyball.png", 1))
            
            
        for i in range(3):
            hoyballer.append(Rectangle(64*4 + i*64, 64*2, 64,  64, "bilder/hoyball.png", 1))
            hoyballer.append(Rectangle(64*13, 64*4 + i*64, 64,  64, "bilder/hoyball.png", 1))
        
        for i in range(4):
            hoyballer.append(Rectangle(64*10 + i*64, 64*7, 64,  64, "bilder/hoyball.png", 1))
            
        
        #pug objekt
        pug = Pug(64*6 * 1.5 + 10, 64*4 * 1.5, "bilder/pug.png", "left", 32, 1.3, sprite_sheet)

        #kylling objekt
        chick = Chick(34, 34, "bilder/chick.png", "down", 26, 1.5, sprite_sheet2)

        #hønsehus objekt
        honsehus = Rectangle( 64*11, 64*5,50,50, "bilder/honsehus.png", 2.54)

        #lyn objekt
        lyn.append(Rectangle(50,450,13,22,"bilder/lyn.png",1.5))
        lyn.append(Rectangle(530,75,13,22,"bilder/lyn.png",1.5))
        lyn.append(Rectangle(64*6 + 20,64*4 + 11,13,22,"bilder/lyn.png",1.5))
        lyn.append(Rectangle(935, 375,13,22,"bilder/lyn.png",1.5))
