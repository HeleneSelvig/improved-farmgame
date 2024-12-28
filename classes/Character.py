# importerer pygame-biblioteket
import pygame as pg

# lager en liste som sier hvor mange bilder det er i hver animasjon
animation_steps = 3
# lager en timer som sier hvor ofte animasjonen skal endre
last_update = pg.time.get_ticks()
# i millisekunder
animation_cooldown = 100


# Konstanter
WIDTH = 1000  # bredden til vinduet
HEIGHT = 600  # høyden til vinduet
SIZE = (WIDTH, HEIGHT)  # størrelsen til vinduet
# Lager en overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# klasse for karakterene


class Character:
    # konstruktør
    def __init__(self, x, y, image, direction, size, scale, sprite_sheet):
        self.x = x
        self.y = y
        self.image = image
        self.size = size
        self.scale = scale
        self.sprite_sheet = sprite_sheet

        # laster inn bilde
        self.characterImg = pg.image.load(image)

        # får høyden og bredden til karakteren ved å finne rektangelet rundt karakteren
        self.characterRect = self.characterImg.get_rect()
        self.h = self.characterRect.height
        self.w = self.characterRect.width

        # setter en x- og y-fart til karakteren
        self.vx = 0
        self.vy = 0

        # retning den begynner å peke i
        self.direction = direction
        # lengde siden sist gang animasjonen oppdaterte seg begynner på 0 millisekunder når programmet kjøres
        self.last_update = 0
        # begynner på det første bildet i animasjonen
        self.frame = 0

    # lager en metode som tegner karakteren til skjermen

    def draw(self):
        # tom liste for hvilken frame vi skal vise
        animation_list = []
        # itererer gjennom bildene i animasjonen og legger det til i listen, slik at vi vet hvor langt vi er kommet i animasjonen
        for i in range(animation_steps):
            animation_list.append(self.sprite_sheet.get_image(
                i, self.size, self.size, self.scale, self.direction))

        # henter hvor lang tid det har gått akkurat nå
        current_time = pg.time.get_ticks()
        # oppdaterer seg hvis det har gått lengre tid enn cooldownen
        if current_time - self.last_update >= animation_cooldown:
            # sier at den kun skal endre frames om karakteren beveger seg
            if not (self.vy == 0 and self.vx == 0):
                # sier at vi skal til neste frame
                self.frame += 1
                # oppdaterer tiden slik at cooldown starter på nytt
                self.last_update = current_time
                # hvis vi er på siste frame, starter animasjonen på nytt
                if self.frame >= len(animation_list):
                    self.frame = 0

        # tegner animasjonen til skjerm
        surface.blit(animation_list[self.frame], (self.x, self.y))

    # metode som oppdaterer posisjonen til karakteren

    def update(self):
        self.x += self.vx
        self.y += self.vy
