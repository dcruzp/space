import pygame 
from pygame.locals import * 
import objects
import os 
import geometry

pygame.init() 
w,h = 800,640

pantalla = pygame.display.set_mode((w,h),0,32)

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)


ship = objects.Ship(os.path.join('sources','img','mejora de la nave.png'),w,h)

mouse = x,y = (10,10)
c = geometry.Circle(geometry.Point(x,y),2)


# esto es para dibujar en la superficie de la nave
#circle1  = geometry.Circle(geometry.Point(40,30),20)
#circle2  = geometry.Circle(geometry.Point(20,60),20)
#circle3  = geometry.Circle(geometry.Point(60,60),20)
#pygame.draw.circle(ship.sprite.image, RED, (circle1.center.x,circle1.center.y), circle1.radius, 1)
#pygame.draw.circle(ship.sprite.image, RED, (circle2.center.x,circle2.center.y), circle2.radius, 1)
#pygame.draw.circle(ship.sprite.image, RED, (circle3.center.x,circle3.center.y), circle3.radius, 1)
ship.dawCircles()
# aqui se acaba

#circles = (circle1,circle2,circle3)

#def colition (circs , mous):
#   for x in circs:
#        if x.collider(mous):
#            return True
#    return False 


reloj = pygame.time.Clock()
while(True):

    #circle1  = geometry.Circle(geometry.Point(ship.sprite.rect.left+ 40,ship.sprite.rect.top + 30),20)
    #circle2  = geometry.Circle(geometry.Point(ship.sprite.rect.left+ 20,ship.sprite.rect.top + 60),20)
    #circle3  = geometry.Circle(geometry.Point(ship.sprite.rect.left+ 60,ship.sprite.rect.top + 60),20)

    #circles = (circle1,circle2,circle3)

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed() 
    if pulsada[pygame.K_LEFT]:
        ship.movleft(4)
    if pulsada[pygame.K_RIGHT]:
        ship.movright(4,w)

    mouse = pygame.mouse.get_pos()
    c.center.x  = mouse[0]
    c.center.y  = mouse[1]
    c.radius = 2 
   
    
    if ship.collider(c):
        print('Hubo una colicion ')


    reloj.tick(60)
    pantalla.fill(BLACK)

    '''
    circle  = geometry.Circle((10,10),10)
    pygame.draw.circle(ship.sprite.image, RED, circle.center, circle.radius, 1)
    '''

    pantalla.blit(ship.sprite.image, ship.sprite.rect)
    pygame.draw.rect(pantalla , RED , ship.sprite.rect,1)
    pygame.draw.circle(pantalla, BLUE, (c.center.x ,c.center.y), c.radius, 1)
    pygame.display.update()               
