import pygame
import math
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

import model
import graphics
import settings

pygame.init()

FPS = settings.FPS
Xscreensize=settings.Xscreensize
Yscreensize=settings.Yscreensize
screen = pygame.display.set_mode((Xscreensize, Yscreensize))

#########################код контроллера
pygame.display.update()
clock = pygame.time.Clock()
finished = False

#model.init()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            #model.handler
            pass
        elif event.type == pygame.KEYDOWN:
            print(event.key)
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEMOTION:
            pass       
    
    #model.tick()
    pygame.display.update()
    #screen.fill(backg)

pygame.quit()