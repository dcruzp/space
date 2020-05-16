import pygame 
from pygame.locals import * 
import objects
import os 
import geometry
from objects import shootEnemy

pygame.init() 
w,h = 800,640

pantalla = pygame.display.set_mode((w,h),0,32)

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)


ship = objects.Ship(os.path.join('sources','img','mejora de la nave.png'),w,h)
shoot = objects.Shoot(os.path.join('sources','img','shoot.png'),ship)
shipenemy = objects.ShipEnemy(os.path.join('sources','img','enemyShip.png'),10,10)

mouse = x,y = (10,10)
c = geometry.Circle(geometry.Point(x,y),2)

ship.dawCircles()
shoot.dawCircles()
shipenemy.dawCircles()

reloj = pygame.time.Clock()
while(True):

    for eventos in pygame.event.get(): # esto es para manejar los eventos 
        if eventos.type == pygame.QUIT:
            exit()

    pulsada = pygame.key.get_pressed() # esto es para el control de la nave 
    if pulsada[pygame.K_LEFT]:
        ship.movleft(4)
    if pulsada[pygame.K_RIGHT]:
        ship.movright(4,w)

    mouse = pygame.mouse.get_pos()
    c.center.x  = mouse[0]
    c.center.y  = mouse[1]
    c.radius = 2 
   
    shoot.movup(4)
    shipenemy.nextMove(h,w,4)

    if ship.collider(c):
        print('Hubo una colicion ')


    reloj.tick(60)
    pantalla.fill(BLACK)
    pantalla.blit(ship.sprite.image, ship.sprite.rect)
    pantalla.blit(shoot.sprite.image , shoot.sprite.rect)
    pantalla.blit(shipenemy.sprite.image , shipenemy.sprite.rect)
    pygame.draw.rect(pantalla , RED , ship.sprite.rect,1)
    pygame.draw.circle(pantalla, BLUE, (c.center.x ,c.center.y), c.radius, 1)
    pygame.display.update()               
