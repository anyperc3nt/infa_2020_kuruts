import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *

TRANSPARENT = (0,0,0,0)
BACKG = (50, 50, 70)

WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

def make_transp(scr):
    """делает surface прозрачным"""
    scr1 = scr.convert_alpha()
    scr1.fill(TRANSPARENT)
    return scr1

def init():
    global ball1
    ball1 = make_transp(pygame.Surface((70,70)))
    circle(ball1, BLUE, (35, 35), 35)

