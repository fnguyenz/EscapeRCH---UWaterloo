import pygame, sys,
from pygame.locals import *
from GameFunctions import *

pygame.init()
clock = pygame.time.Clock()

#Creating the Window
WINDOWWIDTH = 1250
WINDOWHEIGHT = 750

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('RCH Beginnings')

#Loading all Backgrounds
InstructionsPage = pygame.image.load('Images/InstructionsPage2.png')
InstructionsPage = pygame.transform.scale(InstructionsPage, (1250,750))
backbutton = pygame.Rect(0,0,200,100)

VitelliClass = pygame.image.load('Images/VitelliClass.jpg')
VitelliClass = pygame.transform.scale(VitelliClass, (1250,750))

Outside103105 = pygame.image.load('Images/Outside103105.jpg')
Outside103105 = pygame.transform.scale(Outside103105, (1250,750))

TiredKidClass = pygame.image.load('Images/TiredKidClass.jpg')
TiredKidClass = pygame.transform.scale(TiredKidClass, (1250,750))

Hallway103 = pygame.image.load('Images/103Hallway.jpg')
Hallway103 = pygame.transform.scale(Hallway103, (1250,750))

Hallway105 = pygame.image.load('Images/105Hallway.jpg')
Hallway105 = pygame.transform.scale(Hallway105, (1250,750))

CentreRoom = pygame.image.load('Images/CenterRoom.jpg')
CentreRoom = pygame.transform.scale(CentreRoom, (1250,750))

Centre1012 = pygame.image.load('Images/Centre1012.jpg')
Centre1012 = pygame.transform.scale(Centre1012, (1250,750))

Centre1315 = pygame.image.load('Images/Centre1315.jpg')
Centre1315 = pygame.transform.scale(Centre1315, (1250,750))

Outside110112 = pygame.image.load('Images/Outside-110-112.jpg')
Outside110112 = pygame.transform.scale(Outside110112, (1250,750))

Classroom110 = pygame.image.load('Images/Classroom110.jpg')
Classroom110 = pygame.transform.scale(Classroom110, (1250,750))

Classroom112 = pygame.image.load('Images/Classroom112.jpg')
Classroom112 = pygame.transform.scale(Classroom112, (1250,750))

Hallway110 = pygame.image.load('Images/110Hallway.jpg')
Hallway110 = pygame.transform.scale(Hallway110, (1250,750))

Hallway112 = pygame.image.load('Images/112Hallway.jpg')
Hallway112 = pygame.transform.scale(Hallway112, (1250,750))

#Map Loading
MapLength = 200
MapWidth = 200

Outside103105Map = pygame.image.load('Images/maps/outside103and105map.png')             #0
Outside103105Map = pygame.transform.scale(Outside103105Map, (MapLength,MapWidth))  

TiredKidClassMap = pygame.image.load('Images/maps/105map.png')                          #1
TiredKidClassMap = pygame.transform.scale(TiredKidClassMap, (MapLength,MapWidth))

Hallway103Map = pygame.image.load('Images/maps/103hallwaymap.png')                      #2
Hallway103Map = pygame.transform.scale(Hallway103Map, (MapLength,MapWidth))

Hallway105Map = pygame.image.load('Images/maps/105hallwaymap.png')                      #3
Hallway105Map = pygame.transform.scale(Hallway105Map, (MapLength,MapWidth))

centremap = pygame.image.load('Images/maps/centremap.png')                               #4
centremap = pygame.transform.scale(centremap, (MapLength,MapWidth))

centremapdown = pygame.image.load('Images/maps/centredownmap.png')                       #5
centremapdown = pygame.transform.scale(centremapdown, (MapLength,MapWidth))

centremapup = pygame.image.load('Images/maps/centreupnmap.png')                           #6
centremapup = pygame.transform.scale(centremapup, (MapLength,MapWidth))

classroom110map = pygame.image.load('Images/maps/110map.png')                          #7
classroom110map = pygame.transform.scale(classroom110map, (MapLength,MapWidth))

classrooom112map = pygame.image.load('Images/maps/112map.png')                          #8
classrooom112map = pygame.transform.scale(classrooom112map, (MapLength,MapWidth))

outside110112map = pygame.image.load('Images/maps/outside110and112map.png')            #9
outside110112map = pygame.transform.scale(outside110112map, (MapLength,MapWidth))

Hallway110map = pygame.image.load('Images/maps/110hallwaymap.png')                     #10
Hallway110map = pygame.transform.scale(Hallway110map, (MapLength,MapWidth))

hallway112map = pygame.image.load('Images/maps/112hallwaymap.png')                     #11
hallway112map = pygame.transform.scale(hallway112map, (MapLength,MapWidth))

MapList = [Outside103105Map, TiredKidClassMap, Hallway103Map, Hallway105Map, centremap, centremapdown, centremapup, classroom110map, classrooom112map, outside110112map, Hallway110map, hallway112map]
MapNames= ['Outside 103and 105', 'Classroom 105', 'Hallway 103', 'Hallway 105', 'Centre', 'Centre, 103 and 105', 'Centre, 110 and 112', 'Classroom 110', 'Classrooom 112', 'Outside 110 and 112', 'Hallway 110', 'Hallway 112']

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
GreenRightPic = pygame.image.load('Images/GreenRightPic.png')
GreenRightPic = pygame.transform.scale(GreenRightPic,(100,100))

GreenLeftPic = pygame.image.load('Images/GreenLeftPic.png')
GreenLeftPic = pygame.transform.scale(GreenLeftPic,(100,100))

GreenDownPic = pygame.image.load('Images/GreenDownPic.png')
GreenDownPic = pygame.transform.scale(GreenDownPic,(100,100))

GreenUpPic = pygame.image.load('Images/GreenUpPic.png')
GreenUpPic = pygame.transform.scale(GreenUpPic,(100,100))

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#General Fonts (Mainly just for title screen stuff right now)
basicFont = pygame.font.SysFont(None, 48)
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
        windowSurface.blit(InstructionsPage, (0,0))
    
    elif current_screen == 'VitelliClass':
        windowSurface.blit(VitelliClass, (0,0))
        windowSurface.blit(GreenDownPic, Green_down)
    
    elif current_screen == 'Outside103105':
        windowSurface.blit(Outside103105, (0,0))
        windowSurface.blit(GreenLeftPic, Green_left)
        windowSurface.blit(GreenRightPic, Green_right)
        windowSurface.blit(GreenUpPic, Green_up)
        windowSurface.blit(GreenLeftPic, Green_left2)
        
    elif current_screen == 'TiredKidClass':
        windowSurface.blit(TiredKidClass, (0,0))
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == '103Hallway':
        windowSurface.blit(Hallway103, (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        
    elif current_screen == '105Hallway':
        windowSurface.blit(Hallway105, (0,0))
        windowSurface.blit(GreenRightPic, Green_rightcentre)

    elif current_screen == 'CentreRoom':
        windowSurface.blit(CentreRoom, (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        windowSurface.blit(GreenRightPic, Green_rightcentre)
        
    elif current_screen == 'Centre1315':
        windowSurface.blit(Centre1315, (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        windowSurface.blit(GreenRightPic, Green_rightcentre)
        windowSurface.blit(GreenUpPic, Green_up)
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == 'Centre1012':
        windowSurface.blit(Centre1012, (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        windowSurface.blit(GreenRightPic, Green_rightcentre)
        windowSurface.blit(GreenUpPic, Green_up)
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == 'Outside110112':
        windowSurface.blit(Outside110112, (0,0))
        windowSurface.blit(GreenLeftPic, Green_left)
        windowSurface.blit(GreenRightPic, Green_right)
        windowSurface.blit(GreenUpPic, Green_up)
        windowSurface.blit(GreenLeftPic, Green_left2)
        windowSurface.blit(GreenRightPic, Green_right2)
        
    elif current_screen == 'Classroom110':
        windowSurface.blit(Classroom110, (0,0))
        windowSurface.blit(GreenDownPic, Green_down)
        
    elif current_screen == 'Classroom112':
        windowSurface.blit(Classroom112, (0,0))
        windowSurface.blit(GreenDownPic, Green_down)

    elif current_screen == 'Hallway110':
        windowSurface.blit(Hallway110, (0,0))
        windowSurface.blit(GreenLeftPic, Green_leftcentre)
        
    elif current_screen == 'Hallway112':
        windowSurface.blit(Hallway112, (0,0))
        windowSurface.blit(GreenRightPic, Green_rightcentre)
    
    map_set(map,windowSurface,basicFont)
    pygame.display.update()
    clock.tick(60)