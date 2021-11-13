import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

from settings import *

dt=1

class myplayer(object):
    """класс объекта, который имеет свой surface для отрисовки и может передвигаться по экране

    surface: принимает surface для использования в качестве текстурки
    x, y , vx, vy: положение объекта на экране и его скорость
    r: радиус коллизии
    type: значение типа, позволяет отличать объекты друг от друга
    """

    def __init__(self):
        """конструктор"""
        self.name="player"
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0 
        self.ay = 0
        self.r = 100
        self.atime=0
    
    def collide(self, objects={}):
        if (abs(self.x)+self.r)>Xmodelsize/2:
            self.x=(Xmodelsize/2-self.r)*np.sign(self.x)
            self.vx*=-1
        if (abs(self.y)+self.r)>Ymodelsize/2:
            self.y=(Ymodelsize/2-self.r)*np.sign(self.y)
            self.vy*=-1
        
        for object in objects:
            if object.name == "block":
                pass

    def frictoin(self):
        "вязкое трение"
        self.vx-=k0*self.vx
        self.vy-=k0*self.vy
    
    def move(self):
        """ускоряется и перемещает себя значение скорости"""
        if(self.atime>0):
            self.vx+=playervelmax/atime*self.ax
            self.atime-=1
        if abs(self.vx)>playervelmax:
            self.vx=np.sign(self.vx)*playervelmax

        if(self.atime>0):
            self.vy+=playervelmax/atime*self.ay
            self.atime-=1
        if abs(self.vy)>playervelmax:
            self.vy=np.sign(self.vy)*playervelmax

        if(self.atime==0):
            self.ax=0
            self.ay=0

        self.x += int(self.vx)
        self.y += int(self.vy)


class block(object):
    "класс препятствия. вообще не факт, что я буду добавлять в игру препятствия, потому что это сложно"
    def __init__(self):
        """конструктор"""
        self.name="block"
        self.x = 0
        self.y = 0
        self.r = 10

def init():
    global player
    player = myplayer()

def tick():
    player.move()
    player.collide()
    player.frictoin()

def keyhandler(key,isdown):
    "down принимает значения true и false"
    if key == 97:
        player.ax=-1
        player.atime=atime
        player.vy*=0.4
    if key == 100:
        player.ax=1
        player.atime=atime
        player.vy*=0.4
    if key == 119:
        player.ay=-1
        player.atime=atime
        player.vx*=0.4
    if key == 115:
        player.ay=1
        player.atime=atime
        player.vx*=0.4


def handler():
    pass
