import pygame 
from pygame.locals import * 
import time

from time import gmtime 

RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init() 
w,h = 640, 240
screen = pygame.display.set_mode((w,h))
running = True 

img = pygame.image.load('img/player1 copia.png')
img.convert()
rect = img.get_rect()

rect.center = w//2, h//2
moving = False

BLUE = (0,0,255)

font = pygame.font.SysFont(None,15)
img1 = font.render('daniel',True , BLUE)
r = img1.get_rect()



t0 = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    t0 = time.time() - t0
    
    img1 = font.render(str(t0),True,BLUE)
    screen.fill(GRAY)
    screen.blit(img, rect)
    screen.blit(img1, (2, h - img1.get_height()))
    pygame.display.update()

pygame.quit()
