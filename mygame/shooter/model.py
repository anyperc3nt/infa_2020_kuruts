import pygame
import math
import numpy as np
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

from settings import *

class myplayer(object):
    def __init__(self):
        self.name="player"
        self.rot=0
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.ax = 0 
        self.ay = 0
        self.r = player_r
        self.atime=0
    
    def collide(self):
        if (abs(self.x)+self.r)>Xmodelsize/2:
            self.x=(Xmodelsize/2-self.r)*np.sign(self.x)
            self.vx*=-0.8
            self.vy*=0.8
        if (abs(self.y)+self.r)>Ymodelsize/2:
            self.y=(Ymodelsize/2-self.r)*np.sign(self.y)
            self.vy*=-0.8
            self.vx*=0.8

    def friction_old(self):
        "вязкое трение"
        self.vx-=k0*self.vx
        self.vy-=k0*self.vy
    
    def friction(self):
        self.vx-=k0*(abs(self.vx)**pow)*np.sign(self.vx)
        self.vy-=k0*(abs(self.vy)**pow)*np.sign(self.vy)
    
    def move(self):
        """ускоряется и перемещает себя значение скорости"""
        if(self.atime>0):
            self.vx+=playervelmax/atime*self.ax
            self.vy+=playervelmax/atime*self.ay
            self.atime-=1

        if abs(self.vx)>playervelmax:
            self.vx=np.sign(self.vx)*playervelmax

        if abs(self.vy)>playervelmax:
            self.vy=np.sign(self.vy)*playervelmax

        if(self.atime==0):
            self.ax=0
            self.ay=0

        self.x += self.vx
        self.y += self.vy

class myenemy(object):
    def __init__(self,x,y):
        self.name="enemy"
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.r = player_r
    
    def collide(self):
        if (abs(self.x)+self.r)>Xmodelsize/2:
            self.x=(Xmodelsize/2-self.r)*np.sign(self.x)
        if (abs(self.y)+self.r)>Ymodelsize/2:
            self.y=(Ymodelsize/2-self.r)*np.sign(self.y)
    
    def move(self):
        global dt
        dy=player.y-self.y
        dx=player.x-self.x

        self.vy=enemyvmax*dy/(dx**2+dy**2)**0.5
        self.vx=enemyvmax*dx/(dx**2+dy**2)**0.5

        self.x += self.vx*dt
        self.y += self.vy*dt       
        

def init():
    global dt
    dt=1
    global player
    player = myplayer()
    global enemy
    enemy = myenemy(100,100)


def tick():
    global dt
    dt=(player.vx**2+player.vy**2)**0.5 / playervelmax

    if(dt<0.05):
        dt=0.015

    player.move()
    player.collide()
    player.friction()

    enemy.move()
    enemy.collide()
    #print(player.x,player.y)
    

def keyhandler(key,isdown):
    "isdown принимает значения true и false"
    if (key == 97 or key == 100 or key == 119 or key == 115) and isdown:
    #if key == 119 and isdown:
        rot_rad=player.rot/180*np.pi

        if key==119:
            pass

        if key == 97:
            rot_rad-=np.pi/2

        if key == 100:
            rot_rad+=np.pi/2

        if key == 115:
            rot_rad+=np.pi

        player.ay=math.cos(rot_rad)-player.vy/playervelmax
        player.ax=math.sin(rot_rad)-player.vx/playervelmax
        player.atime=atime


def mousehandler(x):
    player.rot=int(x*mouse_sensivity)

