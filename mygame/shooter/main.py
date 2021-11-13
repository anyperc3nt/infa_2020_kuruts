import pygame
import math
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

import model
import graphics
from settings import *

scale=Xscreensize/Xmodelsize

def conv_to_screen(x,y,rot=0):

    """xnew=(x-model.player.x)*math.sin(rot)-(y-model.player.y)*math.cos(rot)
    ynew=(x-model.player.x)*math.cos(rot)+(y-model.player.y)*math.sin(rot)

    xscreen=xnew*(Xscreensize/model.Xbound)
    yscreen=ynew*(Yscreensize/model.Ybound)
"""

    x+=Xmodelsize/2
    xscreen = x*scale

    y+=Ymodelsize/2
    yscreen = y*scale

    return int(xscreen), int(yscreen)

#########################код 

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
            #model.keyhandler(event.key,0)
            pass
        elif event.type == pygame.MOUSEMOTION:
            pass       
    
    model.tick()
    x1,y1=conv_to_screen(model.player.x,model.player.y)
    graphics.draw("player",scale, x1,y1)

    graphics.update()

pygame.quit()