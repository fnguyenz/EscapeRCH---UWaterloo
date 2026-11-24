import pygame, sys
from pygame.locals import *
from Loading import *
from Dialogue import *

pygame.init()
clock = pygame.time.Clock()

#Creating the Window
WINDOWWIDTH = 1250
WINDOWHEIGHT = 750

windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Local Test13')


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

#Dialogue Buttons
DialogueBox = pygame.Rect(475, 450, 600, 300)
DialogueBox.midtop = (625,450)
DiaL1 = pygame.Rect(425,550,200,100)
DiaR1 = pygame.Rect(700,550,200,100)

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

Dialogue = False
TiredKid = False


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

            basicFont = pygame.font.SysFont(None, int(WINDOWHEIGHT/15.625))
            TitleFont = pygame.font.SysFont(None, int(WINDOWHEIGHT/7.5))

            Title_text = TitleFont.render('Escape RCH', True, RED, BLACK)
            play_text = basicFont.render('Play', True, WHITE, BLACK)
            Instruction_text = basicFont.render('How to Play', True, WHITE, BLACK)
            
            Title_rect = Title_text.get_rect(center=(int(WINDOWWIDTH/2),int(WINDOWHEIGHT/5)))
            play_textRect = play_text.get_rect(center=(int(WINDOWWIDTH/2),int(WINDOWHEIGHT/2)))
            Instruction_rect = Instruction_text.get_rect(center = (int(WINDOWWIDTH/2), int(WINDOWHEIGHT/(5/3))))

            for name in BackgroundList:
                BackgroundList[name] = pygame.transform.scale(OriginalBackgroundList[name], event.size)

            for screen in MapListOriginal:
                MapList[screen] = pygame.transform.scale(MapListOriginal[screen], (WINDOWWIDTH/5, WINDOWHEIGHT/3.75))
            MapFont = pygame.font.SysFont(None, int(WINDOWHEIGHT/31.25))

            for arrow in range(len(ArrowsOriginal)):
                Arrows[arrow] = pygame.transform.scale(ArrowsOriginal[arrow], (int(WINDOWWIDTH/12.5), int(WINDOWHEIGHT/7.5)))

            for GreenButton in range(len(GreenButtons)):
                GreenButtons[GreenButton].size = (int(WINDOWWIDTH/12.5), int(WINDOWHEIGHT/7.5))
            Green_right.midright = (WINDOWWIDTH, int(WINDOWHEIGHT/3))

            Green_left.midleft = (0, WINDOWHEIGHT/3)
            Green_down.midbottom = (WINDOWWIDTH/2, WINDOWHEIGHT)
            Green_up.midtop = (WINDOWWIDTH/2, 0)
            Green_left2.midleft = (0, int(WINDOWHEIGHT/1.5))
            Green_leftcentre.midleft = (0, WINDOWHEIGHT/2)
            Green_right2.midright = (WINDOWWIDTH, int(WINDOWHEIGHT/1.5))
            Green_rightcentre.midright = (WINDOWWIDTH, WINDOWHEIGHT/2)

            backbutton.size = (int(WINDOWWIDTH/6.25), int(WINDOWHEIGHT/7.5))

            SketchyGuyButton.size = (int(WINDOWWIDTH*0.12), int(WINDOWHEIGHT/1.875))
            SketchyGuyButton.topleft = (int(WINDOWWIDTH*0.56), int(WINDOWHEIGHT*0.3))

            VendingMachineButton.size = (int(WINDOWWIDTH/5), int(WINDOWHEIGHT/(750/550)))
            VendingMachineButton.topleft = (0, int(WINDOWHEIGHT/3.75))

            TiredKidButton.size = (int(WINDOWWIDTH*0.16), int(WINDOWHEIGHT/7.5))
            TiredKidButton.topleft = (int(WINDOWWIDTH*0.64), int(WINDOWHEIGHT*0.5333))



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
                elif TiredKidButton.collidepoint(event.pos):
                    current_screen = 'TiredKidSad'
                    D = 0

            elif current_screen == 'TiredKidSad':
                if TiredKid == False:
                    if DiaL1.collidepoint(event.pos) and D == 2:
                        D = 3
                    elif DialogueBox.collidepoint(event.pos) and D == 3:
                            D = 2
                    elif DiaR1.collidepoint(event.pos) and D == 2:
                        D = 4

                    elif DialogueBox.collidepoint(event.pos) and D != 2 and D != 3 and D!=6:
                        D +=1

                    elif (not DialogueBox.collidepoint(event.pos) and event.button == 1) or (DialogueBox.collidepoint(event.pos) and D == 6):
                        if D == 6:
                            TiredKid = True
                        current_screen = 'TiredKidClass'
                else:
                    if DiaL1.collidepoint(event.pos) and D == 0 and Monster == True:
                        D = 1
                        current_screen = 'TiredKidHappy'
                    elif DiaL1.collidepoint(event.pos) and D == 0 and Monster == False:
                        D = 3
                    elif DiaR1.collidepoint(event.pos) and D == 0:
                        D = 2
                    elif (not DialogueBox.collidepoint(event.pos)) or (DialogueBox.collidepoint(event.pos) and D!=0):
                        current_screen = 'TiredKidClass'

            elif current_screen == 'TiredKidHappy':
                if (not DialogueBox.collidepoint(event.pos)) or (DialogueBox.collidepoint(event.pos) and D!=0):
                    current_screen = 'TiredKidClass'

            elif current_screen == '103Hallway':
                if Green_leftcentre.collidepoint(event.pos):
                    current_screen = 'Outside103105'
                    map = 0

                elif Green_rightcentre.collidepoint(event.pos):
                    current_screen = 'Elevator'

                elif SketchyGuyButton.collidepoint(event.pos):
                    current_screen = 'SketchyGuy'

                elif VendingMachineButton.collidepoint(event.pos):
                    current_screen = 'VendingMachine'
        
            elif current_screen == 'VendingMachine':
                if Green_leftcentre.collidepoint(event.pos):
                    current_screen = '103Hallway'
                    map = 2

            elif current_screen == 'Elevator':
                if Green_leftcentre.collidepoint(event.pos):
                    current_screen = '103Hallway'
                    map = 2

            elif current_screen == 'SketchyGuy':
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    current_screen = '103Hallway'
                    map = 2

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
        windowSurface.blit(Arrows[2], Green_down)

    elif current_screen == 'TiredKidSad':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        pygame.draw.rect(windowSurface, GREEN, DiaL1)
        if TiredKid == False:
            windowSurface.blit(TiredKidDialogueAlt1[D], DialogueBox)
        else:
            windowSurface.blit(TiredKidDialogueAlt2[D], DialogueBox)

    elif current_screen == 'TiredKidHappy':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(TiredKidDialogueAlt2[D], DialogueBox)

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
        
    elif current_screen == 'Classroom110':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[2], Green_down)
        
    elif current_screen == 'Classroom112':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[2], Green_down)

    elif current_screen == 'Hallway110':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[1], Green_leftcentre)
        
    elif current_screen == 'Hallway112':
        windowSurface.blit(BackgroundList[current_screen], (0,0))
        windowSurface.blit(Arrows[0], Green_rightcentre)
    
    if current_screen != 'Start_Screen' and current_screen != 'InstructionsPage' and current_screen != 'VitelliClass':
        windowSurface.blit(MapList[current_screen], (0, 0))
        MapText = MapFont.render(MapNames[map], True, WHITE)
        MapTextRect = MapText.get_rect(topleft=(0,(WINDOWHEIGHT/3.75)+10))
        windowSurface.blit(MapText, MapTextRect)

    pygame.display.update()
    clock.tick(60)