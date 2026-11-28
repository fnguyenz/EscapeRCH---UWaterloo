import pygame

#TiredKidDialogue

TiredKidDia1 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia1.png')
TiredKidDia15 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia1.5.png')
TiredKidDiaQ1 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDiaQ1.png')
TiredKidDia3 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia3.png')
TiredKidDia4 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia4.png')
TiredKidDia45 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia4.5.png')
TiredKidDia5 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia5.png')
TiredKidDiaQ2 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDiaQ2.png')
TiredKidDia6 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia6.png')
TiredKidDia7 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia7.png')
TiredKidDia8 = pygame.image.load('Images/Dialogue/TiredKid/TiredKidDia8.png')
#Pendar Dialogue!
PendarDia1 = pygame.image.load('Images/Dialogue/BlockingPeeps/PendarDialogue1.png')

TiredKidDialogue1 = [TiredKidDia1, TiredKidDia15, TiredKidDiaQ1, TiredKidDia3, TiredKidDia4, TiredKidDia45, TiredKidDia5, PendarDia1]
TiredKidDialogueAlt1 = []
for image in TiredKidDialogue1:
    scaled_image = pygame.transform.scale(image, (600, 300))
    TiredKidDialogueAlt1.append(scaled_image)

TiredKidDialogue2 = [TiredKidDiaQ2, TiredKidDia6, TiredKidDia7, TiredKidDia8]
TiredKidDialogueAlt2 = []
for image in TiredKidDialogue2:
    scaled_image = pygame.transform.scale(image, (600, 300))
    TiredKidDialogueAlt2.append(scaled_image)

#SketchyKid