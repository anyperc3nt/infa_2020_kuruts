import pygame
import math
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

import model
import graphics
import settings
import textures

pygame.init()

FPS = settings.FPS
Xscreensize=settings.Xscreensize
Yscreensize=settings.Yscreensize
screen = pygame.display.set_mode((Xscreensize, Yscreensize))

layer_0 = textures.make_transp(pygame.Surface((settings.Xscreensize, settings.Yscreensize)))

def conv_to_screen(x,y,alpha):
    xnew=(x-model.player.x)*math.sin(alpha)-(y-model.player.y)*math.cos(alpha)
    ynew=(x-model.player.x)*math.cos(alpha)+(y-model.player.y)*math.sin(alpha)

    xscreen=xnew*(Xscreensize/model.Xbound)
    yscreen=ynew*(Yscreensize/model.Ybound)

    return xscreen, yscreen

#########################код контроллера
pygame.display.update()
clock = pygame.time.Clock()
finished = False

model.init()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            model.keyuphandler(event.key)
        elif event.type == pygame.KEYDOWN:
            model.keydownhandler(event.key)
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEMOTION:
            pass       
    
    model.tick()
    pygame.display.update()
    #screen.fill(backg)

pygame.quit()