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

#henter inn bjeffe-lyd
barking = pg.mixer.Sound("lyd/dog.ogg")
play_barking = False
#henter inn kakle-lyd
cackling = pg.mixer.Sound("lyd/chicken.ogg")
play_cackling = False
#henter inn wooshe-lyd
woosh = pg.mixer.Sound("lyd/woosh.mp3")


#global hoyballer, lyn, pug, chick, honsehus
#lager en tekst dersom hunden vinner som kan vises til skjerm med hvit skrift og blå bakgrunn
textPug = font.render("Pug vinner! trykk enter", True, WHITE,BLUE)
#finner rektangelet rundt teksten
textRectPug = textPug.get_rect()
#setter midten til tekstens rektangel = midten av hele skjermen
textRectPug.center = (WIDTH // 2, HEIGHT // 2)


#lager tekst dersom kyllingen vinner
textChick = font.render("Kylling vinner! trykk enter", True, WHITE,BLUE)
#finner rektangelet rundt teksten
textRectChick = textChick.get_rect()
#setter midten til tekstens rektangel = midten av hele skjermen
textRectChick.center = (WIDTH // 2, HEIGHT // 2)


def gameplayer():
    global hoyballer, lyn, pug, chick, honsehus
    #lager en metode som sjekker kollisjon mellom kyllingen og hønsehuset, altså om kyllingen vinner
    def collisionChickHonsehus(chick, honsehus):
        #henter den globale variabelen som sier om kakle-lyd kan spilles
        global play_cackling
        #sjekker om kyllingens x-verdi kolliderer med hønsehusets x-verdi
        if chick.x + chick.size - 11 >= honsehus.x and chick.x + 38 <= honsehus.x + honsehus.w:
            #sjekker om kyllingens y-verdi kolliderer med hønsehusets y-verdi
            if chick.y + chick.size >= honsehus.y and chick.y + 38 <= honsehus.y + honsehus.h:
                #pug skal bli borte dersom kylling vinner
                pug.hidden = True
                
                #stopper bakgrunnsmusikk
                pg.mixer.music.stop()
                #spiller kakle-lyd så lenge den ikke allerede spilles (dette gjør at den bare spilles én gang og ikke oppå seg selv)
                if not play_cackling:
                    #sier at kakle-lyden kan spilles
                    play_cackling = True
                    #spiller kaklelyd
                    cackling.play()
                   
        
                #skriver vinnertekst for kyllingen
                surface.blit(textChick, textRectChick)
         



    #lager en metode som sjekker kollisjon mellom hunden og kyllingen, altså om hunden vinner
    def collisionPugChick(pug, chick):
        #henter den globale variabelen som sier om bjeffe-lyd kan spilles
        global play_barking
        #sjekker om kyllingens x-verdi kolliderer med hundens x-verdi
        if chick.x + chick.size >= pug.x and chick.x <= pug.x + pug.size:
            #sjekker om kyllingens y-verdi kolliderer med hundens y-verdi
            if chick.y + chick.size >= pug.y and chick.y <= pug.y + pug.size:
                #kylling blir borte dersom hunden vinner
                chick.hidden = True
                
                #stopper bakgrunnsmusikk
                pg.mixer.music.stop()
                #hvis bjeffing ikke allerede spilles (dette gjør at den bare spilles én gang og ikke oppå seg selv)
                if not play_barking:
                    #sier at bjeffe-lyden kan spilles
                    play_barking = True
                    #spiller bjeffelyd
                    barking.play()
                    
                
                #skriver vinnertekst for hunden
                surface.blit(textPug, textRectPug)
                



    #lager en metode som sjekker kollisjon mellom hunden og hønsehuset
    def collisionPugHonsehus(pug, honsehus):
        #lager et nytt rektangel rundt hunden med de skalerte x- og y-verdiene
        ny_rect = pg.Rect(pug.x + pug.vx, pug.y + pug.vy, pug.size * pug.scale, pug.size * pug.scale)
        
        #sjekker for kollisjon mellom hund og hønsehus (colliderect sjekker om rektanglene overlapper noe sted)
        if pg.Rect.colliderect(ny_rect, honsehus.RectangleRect):
            #hvis hunden treffer overnfra eller nedenfra skal fart i y-retning stoppe
            if pug.direction in ("up", "down"):
                pug.vy = 0
            #hvis hunden treffer fra siden skal fart i x-retning stoppe
            if pug.direction in ("left", "right"):
                pug.vx = 0




    #metode som sjekker kollisjon mellom lynene og karakterene
    def collisionLynChickPug(lyn, chick, pug):
        #lager et nytt rektangel rundt hunden med de skalerte x- og y-verdiene
        ny_rect = pg.Rect(pug.x + pug.vx, pug.y + pug.vy, pug.size * pug.scale, pug.size * pug.scale)
        
        #lager et nytt rektangel rundt kyllingen med de skalerte x- og y-verdiene
        ny_rect2 = pg.Rect(chick.x + chick.vx, chick.y + chick.vy, chick.size * chick.scale, chick.size * chick.scale)
        
        #sjekker om hunden kolliderer med et av lynene
        for lynet in lyn:
            if pg.Rect.colliderect(ny_rect, lynet.RectangleRect):
                #stopper wooshe-lyd om det spilles fra før av
                woosh.stop()
                #spiller wooshelyd
                woosh.play()
                
                #dersom det er kollisjon skal hundens fart øke i den retningen den beveger seg i
                if pug.direction == "up":
                    pug.vy = -10
                elif pug.direction == "down":
                    pug.vy = 10
                elif pug.direction == "left":
                    pug.vx = -10
                elif pug.direction == "right":
                    pug.vx = 10
        
            
            #sjekker om kyllingen kolliderer med et av lynene
            if pg.Rect.colliderect(ny_rect2, lynet.RectangleRect):
                #stopper wooshe-lyd om det spilles fra før av
                woosh.stop()
                #spiller wooshelyd
                woosh.play()
                #dersom det er kollisjon skal kyllingens fart øke i den retningen den beveger seg i
                if chick.direction == "up":
                    chick.vy = -10
                elif chick.direction == "down":
                    chick.vy = 10
                elif chick.direction == "left":
                    chick.vx = -10
                elif chick.direction == "right":
                    chick.vx = 10
            




    #lager en metode for kollisjon mellom høyballene og karakterene
    def collisionHoyballPugChick(hoyballer,pug,chick):
        #lager et nytt rektangel rundt hunden med de skalerte x- og y-verdiene
        ny_rect = pg.Rect(pug.x + pug.vx, pug.y + pug.vy, pug.size * pug.scale, pug.size * pug.scale)
        
        #lager et nytt rektangel rundt kyllingen med de skalerte x- og y-verdiene
        ny_rect2 = pg.Rect(chick.x + chick.vx, chick.y + chick.vy, chick.size * chick.scale, chick.size * chick.scale)
        
        
        
        #går gjennom alle høyballene
        for hoyball in hoyballer:
            #sjekker for kollisjon mellom hund og høyballene
            if pg.Rect.colliderect(ny_rect, hoyball.RectangleRect):
                #hvis hunden treffer ovenfra eller nedenfra skal fart i y-retning stoppe
                if pug.direction in ("up", "down"):
                    pug.vy = 0
                #hvis hunden treffer fra siden skal fart i x-retning stoppe
                if pug.direction in ("left", "right"):
                    pug.vx = 0
            
            #sjekker for kollisjon mellom kylling og høyballene
            if pg.Rect.colliderect(ny_rect2, hoyball.RectangleRect):
                #hvis kyllingen treffer ovenfra eller nedenfra skal fart i y-retning stoppe
                if chick.direction in ("up", "down"):
                    chick.vy = 0
                #hvis kyllingen treffer fra siden skal fart i x-retning stoppe
                if chick.direction in ("left", "right"):
                    chick.vx = 0


    #tegner høyballene
    for hoyball in hoyballer:
        hoyball.draw()

    #tegner lyn
    for lynet in lyn:
        lynet.draw()
    
    
    #sjekker kollisjon mellom kylling og hønsehus
    collisionChickHonsehus(chick, honsehus)
    #sjekker kollisjon mellom pug og kylling
    collisionPugChick(pug, chick)
    #sjekker kollisjon mellom pug og hønsehus
    collisionPugHonsehus(pug, honsehus)
    #sjekker kollisjon mellom karakterene og høyballene
    collisionHoyballPugChick(hoyballer,pug,chick)
    #sjekker kollisjon mellom lyn og karakterer
    collisionLynChickPug(lyn,chick,pug)
    
    
    #tegner hønsehus
    honsehus.draw()
    

    
    #så lenge høna ikke har tapt skal den vises og oppdateres
    if not chick.hidden:
        #oppdaterer posisjonen
        chick.update()
        #sier at kyllingen kan bevege seg så lenge hunden er med i spillet
        if not pug.hidden:
            #beveger seg
            chick.move()
        #tegner høne til skjermen
        chick.draw()
    #hvis høna vinner skal den stå stille
    if pug.hidden:
        chick.vx = 0
        chick.vy = 0
    
    
    #så lenge hunden ikke har tapt skal den vises og oppdateres
    if not pug.hidden:
        #oppdaterer posisjonen
        pug.update()
        #sier at hunden kan bevege seg så lenge kyllingen er med i spillet
        if not chick.hidden:
            #beveger seg
            pug.move()
        #tegner hunden til skjermen
        pug.draw()
    #hvis hunden vinner skal den stå stille
    if chick.hidden:
        pug.vx = 0
        pug.vy = 0
