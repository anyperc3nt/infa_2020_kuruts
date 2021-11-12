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

def draw(name,x,y,rot=0):
    """функция отрисовки объекта на экран"""
    if name == "player":
        pygame.Surface.blit(screen,pygame.transform.rotate(textures.ball1, rot),(x,y))

def update():
    pygame.display.update()
    screen.fill(textures.BACKG)
