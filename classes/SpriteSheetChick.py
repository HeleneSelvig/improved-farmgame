# importerer pygame-biblioteket
import pygame as pg

# lager en klasse for kyllingens spritesheet som fungerer på lik måte som SpriteSheet-klassen


class SpriteSheetChick():
    # konstruktør
    def __init__(self, image):
        self.sheet = image

    # metode som henter kun det bildet vi skal bruke fra spritesheetet
    def get_image(self, frame, width, height, scale, direction):
        if direction == "up":
            y = 38
        if direction == "right":
            y = 38+62
        if direction == "down":
            y = 38+124
        if direction == "left":
            y = 38+184
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame*48 + 11), y, width, height))
        image = pg.transform.scale(image, (width * scale, height * scale))

        return image
