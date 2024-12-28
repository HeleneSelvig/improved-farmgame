# importerer pygame-biblioteket
import pygame as pg
# importerer sys som hjelper med å lukke spillet
import sys
# importerer randint fra random-biblioteket
from random import randint

from functions.gamemaker import gamemaker
from functions.gameplayer import gameplayer
from functions.startscreen import startscreen
from functions.endscreen import endscreen

# Konstanter
WIDTH = 1000  # bredden til vinduet
HEIGHT = 600  # høyden til vinduet
SIZE = (WIDTH, HEIGHT)  # størrelsen til vinduet

BLUE = (80, 210, 240)
WHITE = (255, 255, 255)


# Initiere pygame
pg.init()

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)


# henter inn bakgrunnsbilde (med dimensjoner 384 × 224)
backgroundImg = pg.image.load("bilder/gress.png")
# skalerer bakgrunnsbilde til ønsket størrelse
backgroundImg = pg.transform.scale(backgroundImg, (WIDTH, HEIGHT))


# laster inn musikkfilen
pg.mixer.music.load("lyd/gamemusic.ogg")
# spiller musikken (-1 ganger gir at den loopes evig)
pg.mixer.music.play(loops=-1)
# setter musikkvolumet (verdi mellom 0 og 1)
pg.mixer.music.set_volume(0.5)


run = True
start = True
game = False
gameover = False


# Spill-løkken
while run:

    while start:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                start = False
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game = True
                    gamemaker()
                    start = False

        # legger bakgrunnsbilde på skjermen
        surface.blit(backgroundImg, (0, 0))

        startscreen()

        pg.display.flip()

    while game:
        surface.blit(backgroundImg, (0, 0))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                game = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    game = False
                    gameover = True

        gameplayer()

        # Etter vi har tegner alt, "flipper" vi displayet
        pg.display.flip()

    while gameover:
        surface.blit(backgroundImg, (0, 0))
        endscreen()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                gameover = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_version = randint(1, 5)
                    gamemaker()
                    game = True
                    gameover = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    gameover = False
                    run = False

        pg.display.flip()


# Avslutter pygame når spilløkken ikke lenger kjøres
pg.quit()
# hjelper med å avslutte spillet
# gir en melding om "process ended with exit code 0", som betyr at alt gikk som det skulle
sys.exit()
