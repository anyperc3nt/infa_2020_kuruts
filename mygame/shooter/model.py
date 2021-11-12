import pygame
import math
import numpy as np
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

from settings import *

dt=100

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
        self.r = 10

    def move(self):
        """перемещает себя значение скорости"""
        self.x += self.vx
        self.y += self.vy
        """self.x += int(self.vx*dt/100)
        self.y += int(self.vy*dt/100)"""

def init():
    global player
    player = myplayer()

def tick():
    player.move()

def keyhandler(key,down):
    "down принимает значения true и false"
    if key == 97:
        player.vx-=10*(-1+down*2)
    if key == 100:
        player.vx+=10*(-1+down*2)
    if key == 119:
        player.vy-=10*(-1+down*2)
    if key == 115:
        player.vy+=10*(-1+down*2)


def handler():
    pass
