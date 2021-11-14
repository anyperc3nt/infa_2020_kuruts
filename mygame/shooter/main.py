import numpy as np
import pygame
import math
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
import random

import model
import graphics
from settings import *


def conv_to_glayer(x,y):
    """функция конвертирует координаты объектов в модели в координаты объектов на графическом слое модели"""
    x+=Xmodelsize/2
    y+=Ymodelsize/2
    return int(x), int(Ymodelsize -y)
    #-y важно, потому что в экране y идет сверху вниз

#########################код 

pygame.init()
graphics.init()
model.init()
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
finished = False

counter_mb = 0

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
            pass
        elif event.type == pygame.MOUSEMOTION:
            model.mousehandler(event.pos[0])

    
    model.tick()
    x1,y1=conv_to_glayer(int(model.player.x),int(model.player.y))
    graphics.draw("player",x1,y1)
    x1,y1=conv_to_glayer(int(model.enemy.x),int(model.enemy.y))
    graphics.draw("enemy",x1,y1)

    #важная вещь, так как я вызываю размытие в движении раз в 1/dt раз
    if counter_mb<int(1/(model.dt+0.00001)):
        counter_mb+=1
    else:
        graphics.motionblur_tick()
        counter_mb=0
    

    graphics.update(int(model.player.x),int(model.player.y),model.player.rot,scale)

pygame.quit()