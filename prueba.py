import pygame 
from pygame.locals import * 
import objects
import os 
import geometry


pygame.init() 
w,h = 800,640

pantalla = pygame.display.set_mode((w,h),0,32)

RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)


ship = objects.Ship(os.path.join('sources','img','mejora de la nave.png'),w,h)
shipenemy = objects.ShipEnemy(os.path.join('sources','img','enemyShip.png'),10,10)

mouse = x,y = (10,10)
c = geometry.Circle(geometry.Point(x,y),2)

ship.dawCircles()

killenemy = False

reloj = pygame.time.Clock()
while(True):

    for eventos in pygame.event.get(): # esto es para manejar los eventos 
        if eventos.type == pygame.QUIT:
            exit()
        if eventos.type == pygame.KEYDOWN:
            if eventos.key == pygame.K_SPACE:
                ship.appendShoot()

    pulsada = pygame.key.get_pressed() # esto es para el control de la nave 
    if pulsada[pygame.K_LEFT]:
        ship.movleft(4)
    if pulsada[pygame.K_RIGHT]:
        ship.movright(4,w)
    
        

    mouse = pygame.mouse.get_pos()
    c.center.x  = mouse[0]
    c.center.y  = mouse[1]
    c.radius = 2 
   
    
    

    if not killenemy :
        shipenemy.nextMove(h,w,4)

    if ship.collider(c):
        print('Hubo una colicion ')


    reloj.tick(100)
    pantalla.fill(BLACK)
    pantalla.blit(ship.sprite.image, ship.sprite.rect)    
    pantalla.blit(shipenemy.sprite.image , shipenemy.sprite.rect)    
    pygame.draw.circle(pantalla, BLUE, (c.center.x ,c.center.y), c.radius, 1)
    for x in ship.shoots:        
        x.movup(4)           
        pantalla.blit(x.sprite.image , x.sprite.rect)
        for circ in x.colliderCirc:
            aux = geometry.Circle(geometry.Point(circ.center.x + x.sprite.rect.left, circ.center.y + x.sprite.rect.top),circ.radius )
            if shipenemy.collider(aux):
                ship.shoots.remove(x)
                print('le dio a la nave enemiga')
                killenemy = True
        if x.sprite.rect.top < 10:
            ship.shoots.remove(x) 

    pygame.display.update()               
