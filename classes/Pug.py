# importerer pygame-biblioteket
import pygame as pg

from classes.Character import Character

# Konstanter
WIDTH = 1000  # bredden til vinduet
HEIGHT = 600 # høyden til vinduet

#lager en klasse for pug-karakteren som arver av karakter-klassen
class Pug(Character):
    #konstruktør
    def __init__(self, x, y, image, direction, size, scale, sprite_sheet):
        super().__init__(x, y, image, direction, size, scale, sprite_sheet)
        # sier at karakteren ikke er skjult, og den skal derfor vises - bruker dette lengre ned i programmet
        self.hidden = False
        
    
    #metode som gjør at karakteren kan bevege seg
    def move(self):
        #gir fart = 0 her slik at figuren står stille når ingen knapper trykkes
        self.vx = 0
        self.vy = 0
       
        #henter inn status på tastaturknappene - om de blir trykket på
        keys  = pg.key.get_pressed()
        
        #sjekker om venstre piltast trykkes på
        if keys[pg.K_LEFT]:
            #setter karakterens retning til å gå mot venstre
            self.direction = "left"
            #gir kollisjon med venstre vegg
            if self.x > 0:
                #gir fart mot venstre
                self.vx = -4
        
        #elif gjør at den ikke kan gå på skrå, men også at vi kun har én direction-verdi lagret om gangen
        #sjekker om høyre piltast trykkes på
        elif keys[pg.K_RIGHT]:
            #setter karakterens retning til å gå mot høyre
            self.direction = "right"
            #gir kollisjon med høyre vegg
            if self.x + self.size + 11 < WIDTH:
                #gir fart mot høyre
                self.vx = 4
        
        #sjekker om piltast opp trykkes på
        elif keys[pg.K_UP]:
            #setter karakterens retning til å gå opp
            self.direction = "up"
            #gir kollisjon med toppen
            if self.y + 11 > 0:
                #gir fart oppover
                self.vy = -4
        
        #sjekker om piltast ned trykkes på
        elif keys[pg.K_DOWN]:
            #setter karakterens retning til å gå ned
            self.direction = "down"
            #gir kollisjon med bunnen
            if self.y + self.size + 16 < HEIGHT:
                #gir fart nedover
                self.vy = 4
 