import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1250
WINDOWHEIGHT = 750

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('RCH Beginnings')

InstructionsPage = pygame.image.load('InstructionsPage.png')
InstructionsPage = pygame.transform.scale(InstructionsPage, (1250,750))
backbutton = pygame.Rect(0,0,200,100)

VitelliClass = pygame.image.load('VitelliClass.jpg')
VitelliClass = pygame.transform.scale(VitelliClass, (1250,750))

Outside103105 = pygame.image.load('Outside103105.jpg')
Outside103105 = pygame.transform.scale(Outside103105, (1250,750))

Hallway103 = pygame.image.load('103Hallway.jpg')
Hallway103 = pygame.transform.scale(Hallway103, (1250,750))

Hallway105 = pygame.image.load('105Hallway.jpg')
Hallway105 = pygame.transform.scale(Hallway105, (1250,750))

CentreRoom = pygame.image.load('CenterRoom.jpg')
CentreRoom = pygame.transform.scale(CentreRoom, (1250,750))

Centre1012 = pygame.image.load('Centre1012.jpg')
Centre1012 = pygame.transform.scale(Centre1012, (1250,750))

Centre1315 = pygame.image.load('Centre1315.jpg')
Centre1315 = pygame.transform.scale(Centre1315, (1250,750))

Outside110112 = pygame.image.load('Outside-110-112.jpg')
Outside110112 = pygame.transform.scale(Outside110112, (1250,750))

Hallway110 = pygame.image.load('110Hallway.jpg')
Hallway110 = pygame.transform.scale(Hallway110, (1250,750))

Hallway112 = pygame.image.load('112Hallway.jpg')
Hallway112 = pygame.transform.scale(Hallway112, (1250,750))


 
Green_right = pygame.Rect(1150,350,100,100)
Green_left = pygame.Rect(0,350,100,100)
Green_down = pygame.Rect(575,650,100,100)
Green_up = pygame.Rect(575,0,100,100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)
TitleFont = pygame.font.SysFont(None, 100)

Title_text = TitleFont.render('Escape RCH', True, RED, BLACK)
Title_rect = Title_text.get_rect(center=(625,150))

play_text = basicFont.render('Play', True, WHITE, BLACK) #creates text object
play_textRect = play_text.get_rect(center=(625,375))

Instruction_text = basicFont.render('How to Play', True, WHITE, BLACK)
Instruction_rect = Instruction_text.get_rect(center = (625, 450))

current_screen = 'Start_Screen'


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
            print("CLICK:", event.pos) 
            print("CURRENT SCREEN:", current_screen)
            
            if current_screen == 'Start_Screen':
                if play_textRect.collidepoint(event.pos):
                    current_screen = 'VitelliClass'
                    
                elif Instruction_rect.collidepoint(event.pos):
                    current_screen = 'InstructionsPage'
            
            elif current_screen == 'InstructionsPage':
                if backbutton.collidepoint(event.pos):
                    current_screen = 'Start_Screen'
            
            elif current_screen == 'VitelliClass':
                if Green_down.collidepoint(event.pos):
                    current_screen = 'Outside103105'
            
            elif current_screen == 'Outside103105':
                if Green_up.collidepoint(event.pos):
                    current_screen = 'CentreRoom'
                    
                elif Green_left.collidepoint(event.pos):
                    current_screen = '105Hallway'
                    
                elif Green_right.collidepoint(event.pos):
                    current_screen = '103Hallway'
                    
            elif current_screen == '103Hallway':
                if Green_left.collidepoint(event.pos):
                    current_screen = 'Outside103105'
                    
            elif current_screen == '105Hallway':
                if Green_right.collidepoint(event.pos):
                    current_screen = 'Outside103105'
            
            elif current_screen == 'CentreRoom':
                if Green_left.collidepoint(event.pos):
                    current_screen = 'Centre1315'
                    
                elif Green_right.collidepoint(event.pos):
                    current_screen = 'Centre1012'
                    
            elif current_screen == 'Centre1315':
                if Green_up.collidepoint(event.pos):
                    current_screen = 'Outside103105'
                    
                elif Green_left.collidepoint(event.pos):
                    current_screen = '103Hallway'
                    
                elif Green_right.collidepoint(event.pos):
                    current_screen = '105Hallway'
                    
                elif Green_down.collidepoint(event.pos):
                    current_screen = 'CentreRoom'
                
            elif current_screen == 'Centre1012':
                if Green_up.collidepoint(event.pos):
                    current_screen = 'Outside110112'
                    
                elif Green_left.collidepoint(event.pos):
                    current_screen = '110Hallway'
                    
                elif Green_right.collidepoint(event.pos):
                    current_screen = '112Hallway'
                    
                elif Green_down.collidepoint(event.pos):
                    current_screen = 'CentreRoom'
                    
            elif current_screen == 'Outside110112':
                if Green_right.collidepoint(event.pos):
                    current_screen = 'Hallway110'
                
                elif Green_left.collidepoint(event.pos): 
                    current_screen = 'Hallway112'
                    
                elif Green_up.collidepoint(event.pos):
                    current_screen = 'CentreRoom'
                    
            elif current_screen == 'Hallway110':
                if Green_left.collidepoint(event.pos):
                    current_screen = 'Outside110112'
            
            elif current_screen == 'Hallway112':
                if Green_right.collidepoint(event.pos):
                    current_screen = 'Outside110112'
            
    if current_screen == 'Start_Screen':
        windowSurface.fill(BLACK)
        windowSurface.blit(Title_text, Title_rect)
        windowSurface.blit(play_text, play_textRect)
        windowSurface.blit(Instruction_text, Instruction_rect)
        
    elif current_screen == 'InstructionsPage':
        windowSurface.blit(InstructionsPage, (0,0))
    
    elif current_screen == 'VitelliClass':
        windowSurface.blit(VitelliClass, (0,0))
        pygame.draw.rect(windowSurface,GREEN, Green_down)
    
    elif current_screen == 'Outside103105':
        windowSurface.blit(Outside103105, (0,0))
        pygame.draw.rect(windowSurface, GREEN, Green_left)
        pygame.draw.rect(windowSurface, GREEN, Green_right)
        pygame.draw.rect(windowSurface, GREEN, Green_up)
        
    elif current_screen == '103Hallway':
        windowSurface.blit(Hallway103, (0,0))
        pygame.draw.rect(windowSurface, GREEN, Green_left)
        
    elif current_screen == '105Hallway':
        windowSurface.blit(Hallway105, (0,0))
        pygame.draw.rect(windowSurface, GREEN, Green_right)

    elif current_screen == 'CentreRoom':
        windowSurface.blit(CentreRoom, (0,0))
        pygame.draw.rect(windowSurface, GREEN, Green_left)
        pygame.draw.rect(windowSurface, GREEN, Green_right)
        
    elif current_screen == 'Centre1315':
        windowSurface.blit(Centre1315, (0,0))
        pygame.draw.rect(windowSurface, GREEN, Green_left)
        pygame.draw.rect(windowSurface, GREEN, Green_right)
        pygame.draw.rect(windowSurface, GREEN, Green_up)
        pygame.draw.rect(windowSurface, GREEN, Green_down)
        
    elif current_screen == 'Centre1012':
        windowSurface.blit(Centre1012, (0,0))
        pygame.draw.rect(windowSurface, GREEN, Green_left)
        pygame.draw.rect(windowSurface, GREEN, Green_right)
        pygame.draw.rect(windowSurface, GREEN, Green_up)
        pygame.draw.rect(windowSurface, GREEN, Green_down)
        
    elif current_screen == 'Outside110112':
        windowSurface.blit(Outside110112, (0,0))
        pygame.draw.rect(windowSurface,GREEN, Green_up)
        pygame.draw.rect(windowSurface,GREEN,Green_right)
        pygame.draw.rect(windowSurface,GREEN,Green_left)
        
    elif current_screen == 'Hallway110':
        windowSurface.fill(RED) 
        pygame.draw.rect(windowSurface,GREEN,Green_left)
        
    elif current_screen == 'Hallway112':
        windowSurface.blit(Hallway112, (0,0))
        pygame.draw.rect(windowSurface,GREEN,Green_right)
    

    pygame.display.update()