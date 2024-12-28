# importerer pygame-biblioteket
import pygame as pg

# Konstanter
WIDTH = 1000  # bredden til vinduet
HEIGHT = 600  # høyden til vinduet
SIZE = (WIDTH, HEIGHT)  # størrelsen til vinduet

BLUE = (80, 210, 240)
WHITE = (255, 255, 255)

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# henter font og skriftstørrelse
font = pg.font.SysFont("Arial", 48)


def startscreen():
    textInfo = font.render("Trykk mellomrom for å starte", True, WHITE, BLUE)
    textInfo2 = font.render(
        "hund: piltaster, kylling: wasd", True, WHITE, BLUE)
    textRectInfo = textInfo.get_rect()
    textRectInfo2 = textInfo2.get_rect()
    textRectInfo.center = (WIDTH // 2, HEIGHT // 2 - 40)
    textRectInfo2.center = (WIDTH // 2, HEIGHT // 2 + 40)

    surface.blit(textInfo, textRectInfo)
    surface.blit(textInfo2, textRectInfo2)
