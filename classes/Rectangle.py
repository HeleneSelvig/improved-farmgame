# importerer pygame-biblioteket
import pygame as pg

# Konstanter
WIDTH = 1000  # bredden til vinduet
HEIGHT = 600  # høyden til vinduet
SIZE = (WIDTH, HEIGHT)  # størrelsen til vinduet

# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# lager en klasse for rektangler/firkanter


class Rectangle:
    # konstruktør
    def __init__(self, x, y, w, h, image, scale):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.scale = scale
        # henter inn bildet til objektet
        self.RectangleImg = pg.image.load(self.image)
        # skalerer objektet
        self.RectangleImg = pg.transform.scale(
            self.RectangleImg, (self.w * self.scale, self.h * self.scale))
        # lager et Rectangle rundt objektet
        self.RectangleRect = self.RectangleImg.get_rect()
        # henter x- og y-verdien til det skalerte objektet (brukt i kollisjonene)
        self.RectangleRect.x = x
        self.RectangleRect.y = y
        # henter høyden og bredden til det skalerte objektet
        self.h = self.RectangleRect.height
        self.w = self.RectangleRect.width

    # metode som tegner objektet
    def draw(self):
        surface.blit(self.RectangleImg, (self.x, self.y))
