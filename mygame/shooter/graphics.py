import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

#import main
from settings import *
import textures
#main.screen

#layer_prev = pygame.Surface((Xscreensize,Yscreensize))
#layer_curr = pygame.Surface((Xscreensize,Yscreensize))


def init():
    global screen
    screen = pygame.display.set_mode((Xscreensize, Yscreensize))
    pygame.display.update()
    textures.init()

    global layer_prev
    layer_prev = textures.make_transp(pygame.Surface((Xscreensize,Yscreensize)))

    global layer_curr
    layer_curr = layer_prev


def draw(name,scale,x,y,rot=0):
    """функция отрисовки объекта на экран"""
    if name == "player":
        tex=pygame.transform.rotate(textures.ball1, rot)
        tex=pygame.transform.smoothscale(tex, (int(pygame.Surface.get_width(tex)*scale),int(pygame.Surface.get_height(tex)*scale)))
        pygame.Surface.blit(layer_curr,tex,(x-int(pygame.Surface.get_width(tex)/2),y-int(pygame.Surface.get_height(tex)/2)))


def update():
    global layer_curr
    global layer_prev
    """

    screen.fill(textures.BACKG)

    #pygame.Surface.set_alpha(layer_prev, 254)
    pygame.Surface.blit(screen,layer_prev,(0,0))
    pygame.Surface.blit(screen,layer_curr,(0,0))

    pygame.display.update()

    
    pygame.Surface.blit(layer_prev,layer_curr,(0,0))
    layer_curr.fill(textures.TRANSPARENT)
    """
    screen.fill(textures.BACKG)
    
    black = pygame.Surface((Xscreensize,Yscreensize))
    black.fill(textures.BLACK)
    pygame.Surface.set_alpha(black, 50)

    pygame.Surface.blit(layer_prev,black,(0,0))

    pygame.Surface.blit(layer_prev,layer_curr,(0,0))
    pygame.Surface.blit(screen,layer_prev,(0,0))

    pygame.display.update()

    layer_curr = textures.make_transp(pygame.Surface((Xscreensize,Yscreensize)))


