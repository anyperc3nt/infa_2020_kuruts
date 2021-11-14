import pygame
import math
import numpy as np
from pygame.constants import WINDOWHITTEST
from pygame.draw import *

from settings import *

TRANSPARENT = (0,0,0,0)


BACKG = (40, 40, 80)
#BACKG = (0, 0, 0)
BLACKforBM= (0, 0, 0,255-motionblur_force)

WHITE = (255,255,255)
RED = (255, 0, 0)
REDenemy = (255, 100, 100)
BLUE = (0, 0, 255)
LIGHTBLUE = (100,140,255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100,100,100)

def make_transp(scr):
    """делает surface прозрачным"""
    scr1 = scr.convert_alpha()
    scr1.fill(TRANSPARENT)
    return scr1

def init():
    global ball1
    ball1 = make_transp(pygame.Surface((player_r*2*8,player_r*2*8)))
    circle(ball1, LIGHTBLUE, (player_r*8, player_r*8), player_r*8)
    ball1 = pygame.transform.smoothscale(ball1,(player_r*2,player_r*2))

    global ball2
    ball2 = make_transp(pygame.Surface((player_r*2*8,player_r*2*8)))
    circle(ball2, REDenemy, (player_r*8, player_r*8), player_r*8)
    ball2 = pygame.transform.smoothscale(ball2,(player_r*2,player_r*2))

