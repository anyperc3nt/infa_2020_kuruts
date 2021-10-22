import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

import settings

Xbound=settings.Xmodelbound
Ybound=settings.Ymodelbound
a0=settings.playeracceleration
v0=settings.playervelocity

dt=1

#########################внутренние функции модели


#########################классы


#########################основные функции модели
def init():
    global player
    #player = myplayer(Xbound/2,Ybound/2,15)

def tick():
    pass

def keydownhandler(key):
    if key == 97:
        pass

def keyuphandler(key):
    pass

def handler():
    pass
