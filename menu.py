import pygame 
import pygame_menu

pygame.init() 
screen = pygame.display.set_mode((600,400))


def sef_difficulty (value,difficulty):
    pass 

def start_the_game ():
    pass 

mytheme = pygame_menu.themes.Theme(background_color = (0,0,0),title_background_color=(0, 0, 0,50))

myfont = pygame_menu.font.FONT_8BIT

menu = pygame_menu.Menu(300,400,'Welcome' , theme=mytheme )

menu.add_text_input('Name :', default='daniel')
menu.add_selector('Difficulty :' , [('hard',1), ('Easy',2)], onchange =sef_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)