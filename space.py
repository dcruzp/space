import pygame
import random 
from pygame.locals import * 
import sys

from sys import flags
from objects import * 

pygame.init()

''' esto son las variables gloables del juego ''' 
SIZE =  WIDTH ,HEIGHT = (1080,720)
BLACK = (0,0,0)

shoots = []
enemyshoots = []
shipEnemy = [] 

''' Esta es la inicializacion de juego'''
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('My Game')

ship = Ship("img/testIMG.png" , WIDTH , HEIGHT)




def addshoot ():
    s = Shoot ("img/shoot.png" , ship) 
    shoots.append(s)


def creatEnemy ():
    xpost = 25 
    ypost = 25
    for y in range (5):
        for x in range (10):
            shipenemy = ShipEnemy("img/ship.bmp" , (x+1)*xpost , (y+1)*ypost)
            shipEnemy.append(shipenemy)


creatEnemy()

running = True 

while running:
    screen.fill(BLACK)

    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        ship.movleft(5,WIDTH)
    if key_pressed[pygame.K_RIGHT]:
        ship.movright(5 ,WIDTH)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False 
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                addshoot()
                

    ''' esto es para el disparo de las naves enemigas '''
    

    screen.blit(ship.img,(ship.xposition,ship.yposition))
    

    for shipE in shipEnemy:
        shipE.nextMove(HEIGHT , WIDTH,5)
        screen.blit(shipE.img, (shipE.xposition,shipE.yposition))



    for shoot in shoots :
        shoot.movup(5)        
        screen.blit(shoot.img , (shoot.xposition,shoot.yposition))
        if (shoot.yposition < 10 ): 
            shoots.remove(shoot)

    for enemyshoot in enemyshoots:
        enemyshoot.moveDown(HEIGHT,5)
        screen.blit(enemyshoot.img , (enemyshoot.xposition , enemyshoot.yposition))
        if enemyshoot.yposition > HEIGHT -10:
            enemyshoots.remove(enemyshoot)

              
    
    pygame.display.update() 
    pygame.time.delay (20)

pygame.quit()

