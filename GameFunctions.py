import pygame, sys
from pygame.locals import *

def map_set (map,surface,font):
    surface.blit(MapList[map], (0, 0))
    MapText = font.render(MapNames[map], True, WHITE)
    MapTextRect = MapText.get_rect(topleft=(0,200))
    surface.blit(MapText, MapTextRect)
    return None