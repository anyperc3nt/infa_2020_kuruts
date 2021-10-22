import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

import textures
import settings

def draw(mas, surface):
    """функция отрисовки объектов на экран
    
    mas - массив из названий объектов, их координат на экране и угла поворота
    screen - игровое окно

    mas[0] - название
    mas[1] - х
    mas[2] - у
    mas[3] - угол поворота
    
    """
    surface_prev=surface
    surface.fill(textures.TRANSPARENT)
    pygame.Surface.blit(surface, pygame.set_alpha(surface_prev,settings.motionblurforce), (0,0))
    for object in mas:
        if object[0] == "player":
            pygame.surface.blit(surface,pygame.transform.rotate(textures.ball1, mas[3]),(object[1],object[2]))
            
    pass
