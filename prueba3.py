import pygame
from pygame.locals import * 

class Text:
    def __init__(self, text , pos , ** options):
        self.text = text 
        self.pos = pos

        self.fontname = None 
        self.fontsize = 72
        self.fontcolor = pygame.Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render (self):
        self.img = self.font.render(self.text,True,self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw (self):
        App.screen.blit(self.img,self.rect)

class App:

    def __init__(self):
        pygame.init()
        flags = pygame.RESIZABLE
        App.screen = pygame.display.set_mode((640 , 240), flags)
        App.t = Text ('Pygame App', pos = (20,20))

        App.running = True

    def run (self):
        while App.running:
            for event in pygame.event.get() :
                if event.type == pygame.QUIT:
                    App.running = False 

            App.screen.fill(pygame.Color('gray'))
            App.t.draw()
            pygame.display.update()                                

        pygame.quit()


class GameObject:
    def __init__ (self , image , height , speed):
        self.speed = speed
        self.image = image 
        self.pos = image.get_rect().move(0,height)
    def move(self):
        self.pos = self.pos.move(0,self.speed)
        if (self.pos.right > 600):
            self.pos.left = 0     


if __name__ == '__main__':
    App().run()            