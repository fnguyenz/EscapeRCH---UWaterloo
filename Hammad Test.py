import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1250
WINDOWHEIGHT = 750

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('RCH Beginnings')

#Pretty sure you guys dont have access to these images. Ill figure it out later
Outside110112 = pygame.image.load('Outside-110-112.jpg')
Outside110112 = pygame.transform.scale(Outside110112, (1250,750))

Hallway110 = pygame.image.load('110Hallway.jpg')
Hallway110 = pygame.transform.scale(Hallway110, (1250,750))

Hallway112 = pygame.image.load('112Hallway.jpg')
Hallway112 = pygame.transform.scale(Hallway112, (1250,750))


button_right = True
button_left = True
button_up = False
button_down = False 
Green_right = pygame.Rect(1150,350,100,100)
Green_left = pygame.Rect(0,350,100,100)
Green_down = pygame.Rect(575,0,100,100)
Green_up = pygame.Rect(575,750,100,100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

current_screen = 'Outside110112'


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONUP:
            if current_screen == 'Outside110112':
                if Green_right.collidepoint(event.pos):
                    current_screen = 'Hallway110'
                
                if Green_left.collidepoint(event.pos): 
                    current_screen = 'Hallway112'
                    
            elif current_screen == 'Hallway110':
                if Green_left.collidepoint(event.pos):
                    current_screen = 'Outside110112'
            
            elif current_screen == 'Hallway112':
                if Green_right.collidepoint(event.pos):
                    current_screen = 'Outside110112'
            
            
    if current_screen == 'Outside110112':
        windowSurface.blit(Outside110112, (0,0))
        pygame.draw.rect(windowSurface,GREEN,Green_right)
        pygame.draw.rect(windowSurface,GREEN,Green_left)
        
    elif current_screen == 'Hallway110':
        windowSurface.blit(Hallway110, (0,0))
        pygame.draw.rect(windowSurface,GREEN,Green_left)
        
    elif current_screen == 'Hallway112':
        windowSurface.blit(Hallway112, (0,0))
        pygame.draw.rect(windowSurface,GREEN,Green_right)

    pygame.display.update()
