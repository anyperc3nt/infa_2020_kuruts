import pygame
import math
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

import game_model as model
import game_draw as draw


pygame.init()

FPS = 60
Xbound=800
Ybound=800
screen = pygame.display.set_mode((Xbound, Ybound))

dt=1

def conv_to_screen(x,y,alpha):
    xnew=(x-model.player.x)*math.sin(alpha)-(y-model.player.y)*math.cos(alpha)
    ynew=(x-model.player.x)*math.cos(alpha)+(y-model.player.y)*math.sin(alpha)

    xscreen=xnew*(Xbound/model.Xbound)
    yscreen=ynew*(Ybound/model.Ybound)

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
        elif event.type == pygame.KEYDOWN:
            model.handler("key", event.key, 1, event.x) #последние изменения были здесь
        elif event.type == pygame.KEYUP:
            pass
        elif event.type == pygame.MOUSEMOTION:
            pass       
    
    model.tick()
    pygame.display.update()
    #screen.fill(backg)

pygame.quit()