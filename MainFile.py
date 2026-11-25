import pygame, sys
from pygame.locals import *
from Loading import *
from Dialogue import *

pygame.init()
clock = pygame.time.Clock()

#Creating the Window
WINDOWWIDTH = 1250
WINDOWHEIGHT = 750

OldWW = 1250
OldWH = 750

gameSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), pygame.RESIZABLE)
windowSurface = pygame.Surface((1250, 750))
pygame.display.set_caption('MainFile')


#Primary buttons
Green_right = pygame.Rect(1150,250,100,100)
Green_left = pygame.Rect(0,250,100,100)
Green_down = pygame.Rect(575,650,100,100)
Green_up = pygame.Rect(575,0,100,100)

#Extra buttons
Green_left2 = pygame.Rect(0,500,100,100)
Green_leftcentre = pygame.Rect(0, 325,100,100)
Green_right2 = pygame.Rect(1150,500,100,100)
Green_rightcentre = pygame.Rect(1150, 325,100,100)

GreenButtons = [Green_right, Green_left, Green_down, Green_up, Green_left2, Green_leftcentre, Green_right2, Green_right2]

#Interaction Buttons
SketchyGuyButton = pygame.Rect(700, 225, 150, 400)
VendingMachineButton = pygame.Rect(0, 200, 250, 550)
TiredKidButton = pygame.Rect(800, 400, 200, 100)
IttisakButton = pygame.Rect(150, 275, 125, 400)

#Dialogue Buttons
DialogueBox = pygame.Rect(475, 450, 600, 300)
DialogueBox.midtop = (625,450)
DiaL1 = pygame.Rect(425,550,200,100)
DiaR1 = pygame.Rect(700,550,200,100)

DialogueButtons = [DialogueBox, DiaL1, DiaR1]
DialogueButtonsAlt = [DialogueBox, DiaL1, DiaR1]

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
Title_rect = Title_text.get_rect(center=(WINDOWWIDTH/2,WINDOWHEIGHT/5))

play_text = basicFont.render('Play', True, WHITE, BLACK) #creates text object
play_textRect = play_text.get_rect(center=(WINDOWWIDTH/2,WINDOWHEIGHT/2))

Instruction_text = basicFont.render('How to Play', True, WHITE, BLACK)
Instruction_rect = Instruction_text.get_rect(center = (WINDOWWIDTH/2, (WINDOWHEIGHT/(5/3))))

current_screen = 'Start_Screen'
map = None
Monster = True
Money = False
Keys = False

TiredKid = False

Blocked = True
Acid = True

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
            MouseX = event.pos[0] * (1250 / gameSurface.get_width())
            MouseY = event.pos[1] * (750 / gameSurface.get_height())

            if current_screen == 'Start_Screen':
                if play_textRect.collidepoint((MouseX, MouseY)):
                    current_screen = 'VitelliClass'
                    
                elif Instruction_rect.collidepoint((MouseX, MouseY)):
                    current_screen = 'InstructionsPage'
            
            elif current_screen == 'InstructionsPage':
                if backbutton.collidepoint((MouseX, MouseY)):
                    current_screen = 'Start_Screen'
            
            elif current_screen == 'VitelliClass':
                if Green_down.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside103105'
                    map = 0
            
            elif current_screen == 'Outside103105':
                if Green_up.collidepoint((MouseX, MouseY)):
                    current_screen = 'CentreRoom'
                    map = 4

                elif Green_left.collidepoint((MouseX, MouseY)):
                    current_screen = '105Hallway'
                    map = 3

                elif Green_right.collidepoint((MouseX, MouseY)):
                    current_screen = '103Hallway'
                    map = 2

                elif Green_left2.collidepoint((MouseX, MouseY)):
                    current_screen = 'TiredKidClass'
                    map = 1
                
            elif current_screen == 'TiredKidClass':
                if Green_down.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside103105'
                    map = 0
                elif TiredKidButton.collidepoint((MouseX, MouseY)):
                    current_screen = 'TiredKidSad'
                    D = 0

            elif current_screen == 'TiredKidSad':
                if TiredKid == False:
                    if DialogueButtonsAlt[1].collidepoint((MouseX, MouseY)) and D == 2:
                        D = 3
                    elif DialogueButtonsAlt[0].collidepoint((MouseX, MouseY)) and D == 3:
                            D = 2
                    elif DialogueButtonsAlt[2].collidepoint((MouseX, MouseY)) and D == 2:
                        D = 4

                    elif DialogueButtonsAlt[0].collidepoint((MouseX, MouseY)) and D != 2 and D != 3 and D!=6:
                        D +=1

                    elif (not DialogueButtonsAlt[0].collidepoint((MouseX, MouseY)) and event.button == 1) or (DialogueButtonsAlt[0].collidepoint((MouseX, MouseY)) and D == 6):
                        if D == 6:
                            TiredKid = True
                        current_screen = 'TiredKidClass'
                else:
                    if DialogueButtonsAlt[1].collidepoint((MouseX, MouseY)) and D == 0 and Monster == True:
                        D = 1
                        current_screen = 'TiredKidHappy'
                    elif DialogueButtonsAlt[1].collidepoint((MouseX, MouseY)) and D == 0 and Monster == False:
                        D = 3
                    elif DialogueButtonsAlt[2].collidepoint((MouseX, MouseY)) and D == 0:
                        D = 2
                    elif (not DialogueButtonsAlt[0].collidepoint((MouseX, MouseY))) or (DialogueButtonsAlt[0].collidepoint((MouseX, MouseY)) and D!=0):
                        current_screen = 'TiredKidClass'

            elif current_screen == 'TiredKidHappy':
                if (not DialogueButtonsAlt[0].collidepoint((MouseX, MouseY))) or (DialogueButtonsAlt[0].collidepoint((MouseX, MouseY)) and D!=0):
                    current_screen = 'TiredKidClass'

            elif current_screen == '103Hallway':
                if Green_leftcentre.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside103105'
                    map = 0

                elif Green_rightcentre.collidepoint((MouseX, MouseY)):
                    current_screen = 'Elevator'

                elif SketchyGuyButton.collidepoint((MouseX, MouseY)):
                    current_screen = 'SketchyGuy'

                elif VendingMachineButton.collidepoint((MouseX, MouseY)):
                    current_screen = 'VendingMachine'
        
            elif current_screen == 'VendingMachine':
                if Green_leftcentre.collidepoint((MouseX, MouseY)):
                    current_screen = '103Hallway'
                    map = 2

            elif current_screen == 'Elevator':
                if Green_leftcentre.collidepoint((MouseX, MouseY)):
                    current_screen = '103Hallway'
                    map = 2

            elif current_screen == 'SketchyGuy':
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    current_screen = '103Hallway'
                    map = 2

            elif current_screen == '105Hallway':
                if Green_rightcentre.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside103105'
                    map = 0
            
            elif current_screen == 'CentreRoom':
                if Green_leftcentre.collidepoint((MouseX, MouseY)):
                    current_screen = 'Centre1315'
                    map = 5
                    
                elif Green_rightcentre.collidepoint((MouseX, MouseY)):
                    current_screen = 'Centre1012'
                    map = 6

            elif current_screen == 'Centre1315':
                if Green_up.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside103105'
                    map = 0
                    
                elif Green_leftcentre.collidepoint((MouseX, MouseY)):
                    current_screen = '103Hallway'
                    map = 2

                elif Green_rightcentre.collidepoint((MouseX, MouseY)):
                    current_screen = '105Hallway'
                    map = 3

                elif Green_down.collidepoint((MouseX, MouseY)):
                    current_screen = 'CentreRoom'
                    map = 4
                
            elif current_screen == 'Centre1012': 
                if Green_leftcentre.collidepoint((MouseX, MouseY)): 
                    current_screen = 'Hallway110' 
                    map = 10
                    
                elif Green_rightcentre.collidepoint((MouseX, MouseY)): 
                    if Blocked == True and Acid == True:
                        current_screen = 'Hallway112BlockedAcid'
                    elif Acid == True:
                        current_screen = 'Hallway112Acid'
                    else:
                        current_screen = 'Hallway112' 
                    map = 11

                elif Green_up.collidepoint((MouseX, MouseY)): 
                    current_screen = 'Outside110112' 
                    map = 9
                    
                elif Green_down.collidepoint((MouseX, MouseY)): 
                    current_screen = 'CentreRoom'
                    map = 4
                    
            elif current_screen == 'Outside110112':
                if Green_right.collidepoint((MouseX, MouseY)):
                    current_screen = 'Hallway110'
                    map = 10
                
                elif Green_left.collidepoint((MouseX, MouseY)): 
                    if Blocked == True and Acid == True:
                        current_screen = 'Hallway112BlockedAcid'
                    elif Acid == True:
                        current_screen = 'Hallway112Acid'
                    else:
                        current_screen = 'Hallway112' 
                    map = 11
                    
                elif Green_up.collidepoint((MouseX, MouseY)):
                    current_screen = 'CentreRoom'
                    map = 4
                    
                elif Green_right2.collidepoint((MouseX, MouseY)):
                    if Blocked == True:
                        current_screen = 'Classroom110Ittisak'
                    else:
                        current_screen = 'Classroom110'
                    map = 7
                
                elif Green_left2.collidepoint((MouseX, MouseY)): 
                    current_screen = 'Classroom112'
                    map = 8

            elif current_screen == 'Classroom110' or current_screen == 'Classroom110Ittisak':
                if Green_down.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside110112'
                    map = 9
                elif IttisakButton.collidepoint((MouseX, MouseY)) and Blocked == True:
                    current_screen = 'Ittisak'

            elif current_screen == 'Ittisak':
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    current_screen = 'Classroom110Ittisak'
                    map = 7
                    
            elif current_screen == 'Classroom112':
                if Green_down.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside110112'
                    map = 9

            elif current_screen == 'Hallway110':
                if Green_leftcentre.collidepoint((MouseX, MouseY)):
                    current_screen = 'Outside110112'
                    map = 9
            
            elif current_screen == 'Hallway112' or current_screen == 'Hallway112BlockedAcid' or current_screen == 'Hallway112Acid':
                if Green_rightcentre.collidepoint((MouseX, MouseY)):
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
        windowSurface.blit(Arrows[2], Green_down)

    elif current_screen == 'TiredKidSad':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        if TiredKid == False:
            windowSurface.blit(TiredKidDialogueAlt1[D], DialogueButtonsAlt[0])
        else:
            windowSurface.blit(TiredKidDialogueAlt2[D], DialogueButtonsAlt[0])

    elif current_screen == 'TiredKidHappy':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(TiredKidDialogueAlt2[D], DialogueButtonsAlt[0])

    elif current_screen == '103Hallway':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)
        windowSurface.blit(Arrows[0], Green_rightcentre)

    elif current_screen == 'Elevator':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)

    elif current_screen == 'SketchyGuy':
        windowSurface.blit(BackgroundList[current_screen], (0,0))

    elif current_screen == 'VendingMachine':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)

    elif current_screen == '105Hallway':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[0], Green_rightcentre)

    elif current_screen == 'CentreRoom':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)
        windowSurface.blit(Arrows[0], Green_rightcentre)
        
    elif current_screen == 'Centre1315':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)
        windowSurface.blit(Arrows[0], Green_rightcentre)
        windowSurface.blit(Arrows[3], Green_up)
        windowSurface.blit(Arrows[2], Green_down)
        
    elif current_screen == 'Centre1012':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)
        windowSurface.blit(Arrows[0], Green_rightcentre)
        windowSurface.blit(Arrows[3], Green_up)
        windowSurface.blit(Arrows[2], Green_down)
        
    elif current_screen == 'Outside110112':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_left)
        windowSurface.blit(Arrows[0], Green_right)
        windowSurface.blit(Arrows[3], Green_up)
        windowSurface.blit(Arrows[1], Green_left2)
        windowSurface.blit(Arrows[0], Green_right2)
        
    elif current_screen == 'Classroom110' or current_screen == 'Classroom110Ittisak':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[2], Green_down)

    elif current_screen == 'Ittisak':
        windowSurface.blit(BackgroundList[current_screen], (0,0))

    elif current_screen == 'Classroom112':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[2], Green_down)

    elif current_screen == 'Hallway110':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)
        
    elif current_screen == 'Hallway112' or current_screen == 'Hallway112BlockedAcid' or current_screen == 'Hallway112Acid':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[0], Green_rightcentre)
    
    if current_screen != 'Start_Screen' and current_screen != 'InstructionsPage' and current_screen != 'VitelliClass':
        windowSurface.blit(MapList[current_screen], (0, 0))
        MapText = MapFont.render(MapNames[map], True, WHITE)
        MapTextRect = MapText.get_rect(topleft=(0,(WINDOWHEIGHT/3.75)+10))
        windowSurface.blit(MapText, MapTextRect)

    scaledSurface = pygame.transform.scale(windowSurface, gameSurface.get_size())
    gameSurface.blit(scaledSurface, (0, 0))
    pygame.display.update()
    clock.tick(60)