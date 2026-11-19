import pygame, sys
from pygame.locals import *
from Loading import *

pygame.init()
clock = pygame.time.Clock()

#Creating the Window
WINDOWWIDTH = 1250
WINDOWHEIGHT = 750

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Local Test9')


#Primary buttons
Green_right = pygame.Rect(1150,200,100,100)
Green_left = pygame.Rect(0,200,100,100)
Green_down = pygame.Rect(575,650,100,100)
Green_up = pygame.Rect(575,0,100,100)

#Extra buttons
Green_left2 = pygame.Rect(0,500,100,100)
Green_leftcentre = pygame.Rect(0, 325,100,100)
Green_right2 = pygame.Rect(1150,500,100,100)
Green_rightcentre = pygame.Rect(1150, 325,100,100)

#Arrow Sprites


#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#General Fonts (Mainly just for title screen stuff right now)
basicFont = pygame.font.SysFont(None, 48)
MapFont = pygame.font.SysFont(None, 24)
TitleFont = pygame.font.SysFont(None, 100)

Title_text = TitleFont.render('Escape RCH', True, RED, BLACK)
Title_rect = Title_text.get_rect(center=(625,150))

play_text = basicFont.render('Play', True, WHITE, BLACK) #creates text object
play_textRect = play_text.get_rect(center=(625,375))

Instruction_text = basicFont.render('How to Play', True, WHITE, BLACK)
Instruction_rect = Instruction_text.get_rect(center = (625, 450))

current_screen = 'Start_Screen'
map = None

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.VIDEORESIZE:
            windowSurface = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            WINDOWWIDTH, WINDOWHEIGHT = event.size

            for name in BackgroundList:
                BackgroundList[name] = pygame.transform.scale(OriginalBackgroundList[name], event.size)

            for screen in MapListOriginal:
                MapList[screen] = pygame.transform.scale(MapListOriginal[screen], (WINDOWWIDTH/5, WINDOWHEIGHT/3.75))
            MapFont = pygame.font.SysFont(None, int(WINDOWHEIGHT/31.25))

            for arrow in range(len(ArrowsOriginal)):
                Arrows[arrow] = pygame.transform.scale(ArrowsOriginal[arrow], (int(WINDOWWIDTH/12.5), int(WINDOWHEIGHT/7.5)))



        if event.type == MOUSEBUTTONUP:
            
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
                    map = 0
            
            elif current_screen == 'Outside103105':
                if Green_up.collidepoint(event.pos):
                    current_screen = 'CentreRoom'
                    map = 4

                elif Green_left.collidepoint(event.pos):
                    current_screen = '105Hallway'
                    map = 3

                elif Green_right.collidepoint(event.pos):
                    current_screen = '103Hallway'
                    map = 2

                elif Green_left2.collidepoint(event.pos):
                    current_screen = 'TiredKidClass'
                    map = 1
                
            elif current_screen == 'TiredKidClass':
                if Green_down.collidepoint(event.pos):
                    current_screen = 'Outside103105'
                    map = 0

            elif current_screen == '103Hallway':
                if Green_leftcentre.collidepoint(event.pos):
                    current_screen = 'Outside103105'
                    map = 0

            elif current_screen == '105Hallway':
                if Green_rightcentre.collidepoint(event.pos):
                    current_screen = 'Outside103105'
                    map = 0
            
            elif current_screen == 'CentreRoom':
                if Green_leftcentre.collidepoint(event.pos):
                    current_screen = 'Centre1315'
                    map = 5
                    
                elif Green_rightcentre.collidepoint(event.pos):
                    current_screen = 'Centre1012'
                    map = 6

            elif current_screen == 'Centre1315':
                if Green_up.collidepoint(event.pos):
                    current_screen = 'Outside103105'
                    map = 0
                    
                elif Green_leftcentre.collidepoint(event.pos):
                    current_screen = '103Hallway'
                    map = 2

                elif Green_rightcentre.collidepoint(event.pos):
                    current_screen = '105Hallway'
                    map = 3

                elif Green_down.collidepoint(event.pos):
                    current_screen = 'CentreRoom'
                    map = 4
                
            elif current_screen == 'Centre1012': 
                if Green_leftcentre.collidepoint(event.pos): 
                    current_screen = 'Hallway110' 
                    map = 10
                    
                elif Green_rightcentre.collidepoint(event.pos): 
                    current_screen = 'Hallway112' 
                    map = 11

                elif Green_up.collidepoint(event.pos): 
                    current_screen = 'Outside110112' 
                    map = 9
                    
                elif Green_down.collidepoint(event.pos): 
                    current_screen = 'CentreRoom'
                    map = 4
                    
            elif current_screen == 'Outside110112':
                if Green_right.collidepoint(event.pos):
                    current_screen = 'Hallway110'
                    map = 10
                
                elif Green_left.collidepoint(event.pos): 
                    current_screen = 'Hallway112'
                    map = 11
                    
                elif Green_up.collidepoint(event.pos):
                    current_screen = 'CentreRoom'
                    map = 4
                    
                elif Green_right2.collidepoint(event.pos):
                    current_screen = 'Classroom110'
                    map = 7
                
                elif Green_left2.collidepoint(event.pos): 
                    current_screen = 'Classroom112'
                    map = 8

            elif current_screen == 'Classroom110':
                if Green_down.collidepoint(event.pos):
                    current_screen = 'Outside110112'
                    map = 9
                  
            elif current_screen == 'Classroom112':
                if Green_down.collidepoint(event.pos):
                    current_screen = 'Outside110112'
                    map = 9

            elif current_screen == 'Hallway110':
                if Green_leftcentre.collidepoint(event.pos):
                    current_screen = 'Outside110112'
                    map = 9
            
            elif current_screen == 'Hallway112':
                if Green_rightcentre.collidepoint(event.pos):
                    current_screen = 'Outside110112'
                    map = 9
            
    if current_screen == 'Start_Screen':
        windowSurface.fill(BLACK)
        windowSurface.blit(Title_text, Title_rect)
        windowSurface.blit(play_text, play_textRect)
        windowSurface.blit(Instruction_text, Instruction_rect)
        
    elif current_screen == 'InstructionsPage':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
    
    elif current_screen == 'VitelliClass':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[2], Green_down)
    
    elif current_screen == 'Outside103105':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_left)
        windowSurface.blit(Arrows[0], Green_right)
        windowSurface.blit(Arrows[3], Green_up)
        windowSurface.blit(Arrows[1], Green_left2)
        
    elif current_screen == 'TiredKidClass':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == '103Hallway':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        
    elif current_screen == '105Hallway':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenRightPic, Green_rightcentre)

    elif current_screen == 'CentreRoom':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        windowSurface.blit(GreenRightPic, Green_rightcentre)
        
    elif current_screen == 'Centre1315':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        windowSurface.blit(GreenRightPic, Green_rightcentre)
        windowSurface.blit(GreenUpPic, Green_up)
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == 'Centre1012':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        windowSurface.blit(GreenRightPic, Green_rightcentre)
        windowSurface.blit(GreenUpPic, Green_up)
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == 'Outside110112':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenLeftPic, Green_left)
        windowSurface.blit(GreenRightPic, Green_right)
        windowSurface.blit(GreenUpPic, Green_up)
        windowSurface.blit(GreenLeftPic, Green_left2)
        windowSurface.blit(GreenRightPic, Green_right2)
        
    elif current_screen == 'Classroom110':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == 'Classroom112':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenDownPic, Green_down)

    elif current_screen == 'Hallway110':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        
    elif current_screen == 'Hallway112':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(GreenRightPic, Green_rightcentre)
    
    if current_screen != 'Start_Screen' and current_screen != 'InstructionsPage' and current_screen != 'VitelliClass':
        windowSurface.blit(MapList[current_screen], (0, 0))
        MapText = MapFont.render(MapNames[map], True, WHITE)
        MapTextRect = MapText.get_rect(topleft=(0,(WINDOWHEIGHT/3.75)+10))
        windowSurface.blit(MapText, MapTextRect)

    pygame.display.update()
    clock.tick(60)