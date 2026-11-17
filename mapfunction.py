import pygame, sys
from pygame.locals import *

def map_set (map):
    windowSurface.blit(MapList[map], (0, 0))
    MapText = font.render(MapNames[map], True, WHITE)
    MapTextRect = MapText.get_rect(0,200)