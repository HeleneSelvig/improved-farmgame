# importerer pygame-biblioteket
import pygame as pg

#lager en klasse for hundens spritesheet
class SpriteSheetPug():
    #konstruktør
    def __init__(self, image):
        self.sheet = image
    
    #metode som henter kun det bildet vi skal vise fra spritesheetet
    def get_image(self, frame, width, height, scale, direction):
        #sier at om figuren beveger seg opp skal vi bruke den øverste rekken med bilder
        if direction == "up":
            y = height*0
        #om figuren beveger seg til høyre skal vi bruke rekke nummer 2 med bilder
        if direction == "right":
            y = height*1
        #om figuren beveger seg ned skal vi bruke rekke nummer 3 med bilder
        if direction == "down":
            y = height*2
        #om figuren beveger seg til venstre skal vi bruke rekke nummer 4 med bilder
        if direction == "left":
            y = height*3
        #lager et surface til bildet
        image = pg.Surface((width, height)).convert_alpha()
        #tegner kun det bildet fra spritesheetet vi vil ha (frame*width gir det bildet bortover vi vil ha)
        image.blit(self.sheet, (0,0), ((frame * width), y, width, height))
        #skalerer bildet til størrelsen vi vil ha
        image = pg.transform.scale(image, (width * scale, height * scale))
    
        #returnerer den skalerte versjonen av bildet vi skal vise
        return image
