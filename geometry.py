import math 

class Point:
    def __init__(self , x = 0, y=0):
        self.x = x 
        self.y = y 

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) +')'    

    def distance (self,p):
        return math.sqrt(abs (self.x - p.x)**2 + abs(self.y - p.y)**2)


class Circle:
    def __init__(self , c=(0,0) , r=0):
        self.center = c
        self.radius = r

    def collider (self, c):
        return self.radius + c.radius > self.center.distance(c.center)
    
    def __str__(self):
        return 'center -> ' + '(' + str(self.center.x) + ',' + str(self.center.y) +')' +  '   ' + 'radius -> ' + str(self.radius) 