import pygame 
from enum import Enum 
import geometry

class Ship:

    def __init__(self,img,width, height) :
        self.sprite = pygame.sprite.Sprite()
        self.img = pygame.image.load(img).convert_alpha()  
        self.img = pygame.transform.scale(self.img, (80,80))
        self.sprite.image = self.img
        self.sprite.rect = self.img.get_rect()
        self.sprite.rect.top = height -10 - self.img.get_height()
        self.sprite.rect.left = (width/2) - (self.img.get_width()/2)
        self.colliderCirc = (
                                geometry.Circle(geometry.Point(40,30),20),
                                geometry.Circle(geometry.Point(20,60),20),
                                geometry.Circle(geometry.Point(60,60),20)
                            )

    def movleft (self , dist):             
        if self.sprite.rect.left > 0 :
            self.sprite.rect.left -= dist 

    def movright (self , dist , width):        
        if self.sprite.rect.left + self.sprite.rect.width < width:
            self.sprite.rect.left += dist

    def collider (self,circle):
        for x in self.colliderCirc:
            circaux = geometry.Circle(
                                        geometry.Point( self.sprite.rect.left + x.center.x,
                                                        self.sprite.rect.top + x.center.y),
                                        x.radius
                                     )
            if circaux.collider(circle):
                return True
        return False     

    def dawCircles (self):
        for x in self.colliderCirc:            
            pygame.draw.circle(self.sprite.image, (255,0,0), (x.center.x,x.center.y), x.radius, 1)

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
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = img


        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale (self.img , (20,20))
        self.xposition = xposition 
        self.yposition = yposition
        self.direction = Direction.RIGHT 
        
        self.maxdistomov = 700
        self.maxdistreco = 0  


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
            if self.xposition + middlewidth + dist > width or self.maxdistreco > self.maxdistomov:
                self.moveDown(height , dist  *2 )
                self.direction = Direction.LEFT    
                self.maxdistreco = 0                        
            else:
                self.moveRight(width , dist)
                self.maxdistreco += dist
        
        elif self.direction == Direction.LEFT:
            if self.xposition - middlewidth - dist < 0 or self.maxdistreco > self.maxdistomov:
                self.moveDown(height,dist * 2)
                self.direction = Direction.RIGHT   
                self.maxdistreco = 0              
            else:
                self.moveLeft(width,dist)
                self.maxdistreco += dist

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

  