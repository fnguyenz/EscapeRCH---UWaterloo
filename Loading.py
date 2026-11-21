import pygame
from pygame.locals import *

#BackgroundLoading
InstructionsPage = pygame.image.load('Images/Backgrounds/InstructionsPage2.png')
InstructionsPageAlt = pygame.transform.scale(InstructionsPage, (1250,750)) #1
backbutton = pygame.Rect(0,0,200,100)

VitelliClass = pygame.image.load('Images/Backgrounds/VitelliClass.jpg')
VitelliClassAlt = pygame.transform.scale(VitelliClass, (1250,750))         #2

Outside103105 = pygame.image.load('Images/Backgrounds/Outside103105.jpg')
Outside103105Alt = pygame.transform.scale(Outside103105, (1250,750))      #3

TiredKidClass = pygame.image.load('Images/Backgrounds/TiredKidClass.jpg')
TiredKidClassAlt = pygame.transform.scale(TiredKidClass, (1250,750))     #4

Hallway103 = pygame.image.load('Images/Backgrounds/103Hallway.jpg')
Hallway103Alt = pygame.transform.scale(Hallway103, (1250,750))           #5

Hallway105 = pygame.image.load('Images/Backgrounds/105Hallway.jpg')
Hallway105Alt = pygame.transform.scale(Hallway105, (1250,750))           #6

CentreRoom = pygame.image.load('Images/Backgrounds/CenterRoom.jpg')
CentreRoomAlt = pygame.transform.scale(CentreRoom, (1250,750))          #7

Centre1012 = pygame.image.load('Images/Backgrounds/Centre1012.jpg')
Centre1012Alt = pygame.transform.scale(Centre1012, (1250,750))          #8

Centre1315 = pygame.image.load('Images/Backgrounds/Centre1315.jpg')
Centre1315Alt = pygame.transform.scale(Centre1315, (1250,750))          #9

Outside110112 = pygame.image.load('Images/Backgrounds/Outside-110-112.jpg')
Outside110112Alt = pygame.transform.scale(Outside110112, (1250,750))

Classroom110 = pygame.image.load('Images/Backgrounds/Classroom110.jpg')
Classroom110Alt = pygame.transform.scale(Classroom110, (1250,750))

Classroom112 = pygame.image.load('Images/Backgrounds/Classroom112.jpg')
Classroom112Alt = pygame.transform.scale(Classroom112, (1250,750))

Hallway110 = pygame.image.load('Images/Backgrounds/110Hallway.jpg')
Hallway110Alt = pygame.transform.scale(Hallway110, (1250,750))

Hallway112 = pygame.image.load('Images/Backgrounds/112Hallway.jpg')
Hallway112Alt = pygame.transform.scale(Hallway112, (1250,750))

Elevator = pygame.image.load('Images/Backgrounds/Elevator.jpg')
ElevatorAlt = pygame.transform.scale(Elevator, (1250,750))

SketchyGuy = pygame.image.load('Images/Backgrounds/SktechyGuy-Closeup.jpg')
SketchyGuyAlt = pygame.transform.scale(SketchyGuy, (1250,750))

TiredKidSad = pygame.image.load('Images/Backgrounds/TiredKid-Tired.jpg')
TiredKidSadAlt = pygame.transform.scale(TiredKidSad, (1250,750))

TiredKidHappy = pygame.image.load('Images/Backgrounds/TiredKid-Happy.jpg')
TiredKidHappyAlt = pygame.transform.scale(TiredKidHappy, (1250,750))

VendingMachine = pygame.image.load('Images/Backgrounds/VendingMachine.jpg')
VendingMachineAlt = pygame.transform.scale(VendingMachine, (1250,750))

OriginalBackgroundList = {'InstructionsPage': InstructionsPage, 'VitelliClass': VitelliClass, 'Outside103105': Outside103105, 'TiredKidClass': TiredKidClass, '103Hallway': Hallway103, '105Hallway': Hallway105, 'CentreRoom': CentreRoom, 'Centre1012': Centre1012, 'Centre1315': Centre1315, 'Outside110112': Outside110112, 'Classroom110': Classroom110, 'Classroom112': Classroom112, 'Hallway110': Hallway110, 'Hallway112': Hallway112, 'Elevator': Elevator, 'SketchyGuy': SketchyGuy, 'TiredKidSad': TiredKidSad, 'TiredKidHappy': TiredKidHappy, 'VendingMachine': VendingMachine}
BackgroundList = {'InstructionsPage': InstructionsPageAlt, 'VitelliClass': VitelliClassAlt, 'Outside103105': Outside103105Alt, 'TiredKidClass': TiredKidClassAlt, '103Hallway': Hallway103Alt, '105Hallway': Hallway105Alt, 'CentreRoom': CentreRoomAlt, 'Centre1012': Centre1012Alt, 'Centre1315': Centre1315Alt, 'Outside110112': Outside110112Alt, 'Classroom110': Classroom110Alt, 'Classroom112': Classroom112Alt, 'Hallway110': Hallway110Alt, 'Hallway112': Hallway112Alt, 'Elevator': ElevatorAlt, 'SketchyGuy': SketchyGuyAlt, 'TiredKidSad': TiredKidSadAlt, 'TiredKidHappy': TiredKidHappyAlt, 'VendingMachine': VendingMachineAlt}






#MapLoading
MapLength = 250
MapWidth = 200

Outside103105Map = pygame.image.load('Images/maps/outside103and105map.png')             #0

TiredKidClassMap = pygame.image.load('Images/maps/105map.png')                          #1

Hallway103Map = pygame.image.load('Images/maps/103hallwaymap.png')                      #2

Hallway105Map = pygame.image.load('Images/maps/105hallwaymap.png')                      #3

CentreMap = pygame.image.load('Images/maps/centremap.png')                               #4

CentreMapDown = pygame.image.load('Images/maps/centredownmap.png')                       #5

CentreMapUp = pygame.image.load('Images/maps/centreupnmap.png')                           #6

Classroom110Map = pygame.image.load('Images/maps/110map.png')                          #7

Classroom112Map = pygame.image.load('Images/maps/112map.png')                          #8

Outside110112Map = pygame.image.load('Images/maps/outside110and112map.png')            #9

Hallway110Map = pygame.image.load('Images/maps/110hallwaymap.png')                     #10

Hallway112Map = pygame.image.load('Images/maps/112hallwaymap.png')                     #11

MapListOriginal = {'Outside103105': Outside103105Map, 'TiredKidClass': TiredKidClassMap, '103Hallway': Hallway103Map, '105Hallway': Hallway105Map, 'CentreRoom': CentreMap, 'Centre1012': CentreMapUp, 'Centre1315': CentreMapDown, 'Classroom110': Classroom110Map, 'Classroom112': Classroom112Map, 'Outside110112': Outside110112Map, 'Hallway110': Hallway110Map, 'Hallway112': Hallway112Map, 'Elevator': Hallway103Map, 'SketchyGuy': Hallway103Map, 'VendingMachine': Hallway103Map, 'TiredKidSad': TiredKidClassMap, 'TiredKidHappy': TiredKidClassMap}
MapList = {}
for screen in MapListOriginal:
    MapList[screen] = pygame.transform.scale(MapListOriginal[screen], (MapLength, MapWidth))

MapNames= ['Outside 103 and 105', 'Classroom 105', 'Hallway 103', 'Hallway 105', 'Centre', 'Centre, 103 and 105', 'Centre, 110 and 112', 'Classroom 110', 'Classrooom 112', 'Outside 110 and 112', 'Hallway 110', 'Hallway 112']





#Arrow Loading
GreenRightPic = pygame.image.load('Images/Sprites/GreenRightPic.png')  #0
GreenLeftPic = pygame.image.load('Images/Sprites/GreenLeftPic.png')    #1
GreenDownPic = pygame.image.load('Images/Sprites/GreenDownPic.png')     #2
GreenUpPic = pygame.image.load('Images/Sprites/GreenUpPic.png')         #3

ArrowsOriginal = [GreenRightPic, GreenLeftPic, GreenDownPic, GreenUpPic]
Arrows = [GreenRightPic, GreenLeftPic, GreenDownPic, GreenUpPic]
for arrow in range(len(ArrowsOriginal)):
    Arrows[arrow] = pygame.transform.scale(ArrowsOriginal[arrow], (100,100))

