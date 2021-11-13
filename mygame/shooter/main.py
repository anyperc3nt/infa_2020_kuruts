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


def conv_to_screen(x,y,rot):
    xnew=(x-model.player.x)*math.sin(rot)-(y-model.player.y)*math.cos(rot)
    ynew=(x-model.player.x)*math.cos(rot)+(y-model.player.y)*math.sin(rot)

    xscreen=xnew*(Xscreensize/model.Xbound)
    yscreen=ynew*(Yscreensize/model.Ybound)

    return xscreen, yscreen

#########################код 
#амогус
a=1
FPS = settings.FPS
Xscreensize=settings.Xscreensize
Yscreensize=settings.Yscreensize

pygame.init()
graphics.init()
model.init()

clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            pass
        elif event.type == pygame.KEYDOWN:
            model.keyhandler(event.key,1)
        elif event.type == pygame.KEYUP:
            model.keyhandler(event.key,0)
        elif event.type == pygame.MOUSEMOTION:
            pass       
    
    model.tick()

    graphics.draw(model.player.name,model.player.x,model.player.y)

    graphics.update()

pygame.quit()