import pygame 
from enum import Enum 
import geometry
import os

class Ship:

    def __init__(self,img,width, height) :
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image =  pygame.transform.scale(pygame.image.load(img).convert_alpha(),(80,80))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.top = height -10 - self.sprite.image.get_height()
        self.sprite.rect.left = (width/2) - (self.sprite.image.get_width()/2)
        self.shoots = [] 
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
                                                        self.sprite.rect.top + x.center.y 
                                                      ),
                                        x.radius
                                     )
            if circaux.collider(circle):
                return True
        return False     

    def dawCircles (self):
        for x in self.colliderCirc:            
            pygame.draw.circle(self.sprite.image, (255,0,0), (x.center.x,x.center.y), x.radius, 1)

    def appendShoot (self):
        shoot = Shoot(os.path.join('sources','img','shoot.png'),self.sprite.rect.left + self.sprite.rect.width/2,self.sprite.rect.top)         
        self.shoots.append(shoot)


class Shoot:
    def __init__ (self , img , x , y):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(),(4,8))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.top = y - self.sprite.image.get_height()/2
        self.sprite.rect.left = x - self.sprite.image.get_width()/2 
        self.colliderCirc = (
                                geometry.Circle(geometry.Point(2,4),2),
                            )
        self.timemove = 2
        self.timemovecurr = 0 

    def movup (self, dist):      

        self.timemovecurr += 1 

        if self.timemovecurr == self.timemove and self.sprite.rect.top - dist>= 0:
            self.sprite.rect.top =  self.sprite.rect.top - dist  
            self.timemovecurr = 0             

    def dawCircles (self):
        for x in self.colliderCirc:            
            pygame.draw.circle(self.sprite.image, (0,255,0), (x.center.x,x.center.y), x.radius, 1)
    

class Direction (Enum):
    LEFT = 0 
    Up = 1 
    RIGHT = 2
    DOWN = 3



class ShipEnemy :

    def __init__(self, img , xposition , yposition):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(),(30,30))        
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.top = yposition 
        self.sprite.rect.left = xposition
        self.colliderCirc = (
                                geometry.Circle(geometry.Point(15,15),12),
                            )
        self.direction = Direction.RIGHT        

    def moveRight( self, width , dist ):
        if self.sprite.rect.left  + dist  < width :
            self.sprite.rect.left += dist

    def moveLeft (self , width , dist ):
        if self.sprite.rect.left -  dist > 0 : 
            self.sprite.rect.left  -= dist   

    def nextMove (self, height , width ,dist):           

        if self.direction == Direction.RIGHT:
            if self.sprite.rect.left + self.sprite.rect.width + dist > width:                
                self.direction = Direction.LEFT                                       
            else:
                self.moveRight(width , dist)                
        
        elif self.direction == Direction.LEFT:
            if self.sprite.rect.left - dist < 0 :                
                self.direction = Direction.RIGHT                             
            else:
                self.moveLeft(width,dist)
                
    def collider (self,circle):
        for x in self.colliderCirc:
            circaux = geometry.Circle(
                                        geometry.Point( self.sprite.rect.left + x.center.x,
                                                        self.sprite.rect.top + x.center.y 
                                                      ),
                                        x.radius
                                     )
            if circaux.collider(circle):
                return True
        return False 
               
    def dawCircles (self):
        for x in self.colliderCirc:            
            pygame.draw.circle(self.sprite.image, (0,255,0), (x.center.x,x.center.y), x.radius, 1)                

           
                                
class shootEnemy:
    def __init__ (self , img , x , y):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.transform.scale (pygame.image.load(img).convert_alpha()  , (6,10))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.left = x - self.sprite.rect.width
        self.sprite.rect.top = y - self.sprite.rect.height
        self.colliderCirc = (
                                geometry.Circle(geometry.Point(2,4),2),
                            )

        self.stepmove = 0 
        self.totaltimemove = 2


    def moveDown (self , height , dist):
        self.stepmove = self.stepmove + 1
        if self.sprite.rect.top + self.sprite.rect.height  + dist <= height and self.stepmove == self.totaltimemove:
            self.stepmove = 0 
            self.sprite.rect.top += dist     

    def collider (self,circle):
        for x in self.colliderCirc:
            circaux = geometry.Circle(
                                        geometry.Point( self.sprite.rect.left + x.center.x,
                                                        self.sprite.rect.top + x.center.y 
                                                      ),
                                        x.radius
                                     )
            if circaux.collider(circle):
                return True
        return False          

  