import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

#import main
import settings
import textures
#main.screen

def init():
    global screen
    screen = pygame.display.set_mode((settings.Xscreensize, settings.Yscreensize))
    pygame.display.update()
    textures.init()

def draw(name,scale,x,y,rot=0):
    """функция отрисовки объекта на экран"""
    if name == "player":
        
        tex=pygame.transform.rotate(textures.ball1, rot)
        tex=pygame.transform.smoothscale(tex, (int(pygame.Surface.get_width(tex)*scale),int(pygame.Surface.get_height(tex)*scale)))
        pygame.Surface.blit(screen,tex,(x-int(pygame.Surface.get_width(tex)/2),y-int(pygame.Surface.get_height(tex)/2)))

def update():
    pygame.display.update()
    screen.fill(textures.BACKG)
