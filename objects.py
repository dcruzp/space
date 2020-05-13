import pygame 
from enum import Enum 

class Ship:

    def __init__(self,img,width, height) :
        self.img = pygame.image.load(img).convert_alpha()  
        self.img = pygame.transform.scale(self.img, (80,80))       
        self.xposition = (width/2) - (self.img.get_width()/2)
        self.yposition = height -20 - self.img.get_height()
       

    def movleft (self , dist , width):        
        padding = self.img.get_width()/2
        if  self.xposition-padding - dist >= 0:
            self.xposition = self.xposition - dist

    def movright (self , dist , width):
        padding = self.img.get_width()/2 
        if self.xposition + padding + dist <= width:
            self.xposition = self.xposition + dist    



class Shoot:
    def __init__ (self , img , ship):
        self.img = pygame.image.load(img).convert_alpha() 
        self.img = pygame.transform.scale(self.img , (5,10))
        self.xposition = ship.xposition - self.img.get_width()/2 + ship.img.get_width() /2
        self.yposition = ship.yposition - self.img.get_height()/2
        self.timemove = 2
        self.timemovecurr = 0 

    def movup (self, dist):
        padding = self.img.get_height()/2

        self.timemovecurr += 1 

        if self.timemovecurr == self.timemove and self.yposition - padding - dist>= 0:
            self.yposition =  self.yposition - dist  
            self.timemovecurr = 0             

    

class Direction (Enum):
    LEFT = 0 
    Up = 1 
    RIGHT = 2
    DOWN = 3



class ShipEnemy :
    def __init__(self, img , xposition , yposition):
        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale (self.img , (20,20))
        self.xposition = xposition 
        self.yposition = yposition
        self.direction = Direction.RIGHT 


    def moveRight( self, width , dist ):
        if self.xposition  + dist  < width :
            self.xposition += dist

    def moveLeft (self , width , dist ):
        if self.xposition -  dist > 0 : 
            self.xposition -= dist   

    def moveDown(self , height , dist):
        if self.yposition + self.img.get_height()/2 + dist <= height:
            self.yposition += dist        

    def nextMove (self, height , width ,dist):        
        middlewidth = self.img.get_width()/2

        
        if self.direction == Direction.RIGHT:
            if self.xposition + middlewidth + dist > width:
                self.moveDown(height , dist  *2 )
                self.direction = Direction.LEFT                            
            else:
                self.moveRight(width , dist)
        
        elif self.direction == Direction.LEFT:
            if self.xposition - middlewidth - dist < 0:
                self.moveDown(height,dist * 2)
                self.direction = Direction.RIGHT                 
            else:
                self.moveLeft(width,dist)

    def shoot (self ):
        shoot = shootEnemy('img/spaceshoot.png' , (self.xposition, self.yposition + self.img.get_height()))
        return shoot
                    
                                
class shootEnemy:
    def __init__ (self , img , position):
        self.img = pygame.image.load(img).convert_alpha() 
        self.img = pygame.transform.scale (self.img , (10,10))
        self.xposition = position [0]
        self.yposition = position [1]
        self.stepmove = 0 
        self.totaltimemove = 2


    def moveDown (self , height , dist):
        middleheight = self.img.get_height()/2
        self.stepmove = self.stepmove + 1
        if self.yposition + middleheight + dist <= height and self.stepmove == self.totaltimemove:
            self.stepmove = 0 
            self.yposition += dist     

