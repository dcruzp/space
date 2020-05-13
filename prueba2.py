import pygame , sys 
from pygame.locals import * 

pygame.init () 

FPS = 30 
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600), 0, 32) 
pygame.display.set_caption('animation') 

WHITE = (255, 255, 255) 
BLACK = (  0,   0,   0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 180) 
RED  = (255,   0,   0) 

image  = pygame.image.load('image.png') 
imagex = 360 
imagey = 260 
direction = 'left' 

font_obj = pygame.font.Font('freesansbold.ttf', 32) 
text_surface_obj = font_obj.render('Hello World!', True, GREEN, BLUE) 
text_rect_obj = text_surface_obj.get_rect() 
text_rect_obj.center = (200, 150) 

while True:
    screen.fill(WHITE) 
    #pygame.draw.polygon(screen, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0,106))) 

    #pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4) 
    #pygame.draw.line(screen, BLUE, (120, 60), (60, 120)) 
    #pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4) 

    #pygame.draw.circle(screen, BLUE, (300, 50), 20, 0) 

    #pygame.draw.ellipse(screen, RED, (100, 150, 40,80), 1) 

    #pygame.draw.rect(screen,RED, (200, 150, 100, 50)) 

    #screen.blit(text_surface_obj, text_rect_obj) 

    #if direction == 'right': 
    #    imagex += 5 
    #    if imagex == 360: 
    #        direction = 'down' 
    #elif direction == 'down': 
    #    imagey += 5 
    #    if imagey == 260: 
    #        direction = 'left' 
    #elif direction == 'left': 
    #    imagex -= 5 
    #    if imagex == 20: 
    #        direction = 'up' 
    #elif direction == 'up': 
    #    imagey -= 5 
    #    if imagey == 20: 
    #        direction = 'right' 
    

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit() 
        elif event.type == pygame.KEYDOWN: 
            #if event.key == pygame.K_w:
            #    print("Player move up!")   
            #elif event.key == pygame.K_a: 
            #    print("Player moved left!") 
            #elif event.key == pygame.K_s: 
            #    print("Player moved down!") 
            #elif event.key == pygame.K_d: 
            #    print("Player moved right!")
            if event.key == pygame.K_UP:
                if imagey > 20:
                    imagey -= 5
            if event.key ==pygame.K_DOWN:
                if imagey < 260: 
                    imagey += 5    
            if event.key == pygame.K_LEFT:
                if imagex > 20:
                    imagex -= 5
            if event.key == pygame.K_RIGHT:
                if imagex < 360:
                    imagex += 5  
                                          
    screen.blit(image, (imagex, imagey)) 

    pygame.display.update() 
    fpsClock.tick(FPS)        