# importerer pygame-biblioteket
import pygame as pg

# Konstanter
WIDTH = 1000  # bredden til vinduet
HEIGHT = 600 # høyden til vinduet
SIZE = (WIDTH, HEIGHT) # størrelsen til vinduet

BLUE = (80,210,240)
WHITE = (255,255,255)

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

#henter font og skriftstørrelse
font = pg.font.SysFont("Arial",48)

def endscreen():
    textEnd = font.render("Spillet er over", True, WHITE,BLUE)
    textEnd2 = font.render("Trykk space for å spille igjen, enter for å avslutte", True, WHITE, BLUE)
    textRectEnd = textEnd.get_rect()
    textRectEnd2 = textEnd2.get_rect()
    textRectEnd.center = (WIDTH // 2, HEIGHT // 2 - 40)
    textRectEnd2.center = (WIDTH // 2, HEIGHT // 2 + 40)
    
    surface.blit(textEnd, textRectEnd)
    surface.blit(textEnd2, textRectEnd2)
    
