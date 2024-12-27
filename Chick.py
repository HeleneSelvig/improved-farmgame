# importerer pygame-biblioteket
import pygame as pg

from Character import Character

# Konstanter
WIDTH = 1000  # bredden til vinduet
HEIGHT = 600 # høyden til vinduet

#lager en klasse for kylling-karakteren som arver av karakter-klassen
class Chick(Character):
    #konstruktør
    def __init__(self, x, y, image, direction, size, scale, sprite_sheet):
        super().__init__(x, y, image, direction, size, scale, sprite_sheet)
        self.hidden = False
    
    #metode for kyllingens bevegelse
    def move(self):
        self.vx = 0
        self.vy = 0
       
        #henter inn status på tastaturknappene - om de blir trykket på
        keys = pg.key.get_pressed()
        
        #sjekker om knappen "a" blir trykket på
        if keys[pg.K_a]:
            self.direction = "left"
            #gir kollisjon med venstre vegg
            if self.x > 0:
                #gir fart mot venstre
                self.vx = -4
        
        #sjekker om knappen "d" blir trykket på
        elif keys[pg.K_d]:
            self.direction = "right"
            #gir kollisjon med høyre vegg
            if self.x + self.size + 11 < WIDTH:
                #gir fart mot høyre
                self.vx = 4
        
        #sjekker om knappen "w" blir trykket på
        elif keys[pg.K_w]:
            self.direction = "up"
            #gir kollisjon med toppen
            if self.y + 11 > 0:
                #gir fart oppover
                self.vy = -4
        
        #sjekker om knappen "s" blir trykket på
        elif keys[pg.K_s]:
            self.direction = "down"
            #gir kollisjon med bunnen
            if self.y + self.size + 22 < HEIGHT:
                #gir fart nedover
                self.vy = 4
