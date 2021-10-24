import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

Xbound=1000
Ybound=1000
a0=15
v0max=15

dt=1

player

#########################внутренние функции модели
def object_move(object):
    object.x+=object.vx
    object.y+=object.vy


#########################классы

class myplayer(object):
    """

    x, y , vx, vy: положение объекта на экране и его скорость
    r: радиус коллизии
    m - масса
    type: значение типа, позволяет отличать врагов друг от друга  
    angle: угол поворота  

    """
    def __init__(self, x, y, r):
        """конструктор"""
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.angle = 0
        self.r = r

    def move(self):
        """перемещает себя значение скорости"""
        self.vx+=self.ax
        self.vy+=self.ay
        if(math.abs(self.vx)>v0max):
            self.vx=np.sign(self.vx)*v0max   #последние изменения были здесь
        if(math.abs(self.vy)>v0max):
            self.vy=np.sign(self.vy)*v0max
        object_move(self)

def init():
    global player
    player = myplayer(Xbound/2,Ybound/2,15)

def tick():
    pass

def handler(event_type, key="0", down=0, x=0):
    if event_type == "key":
        if key == "a":
            player.ax=-a0
