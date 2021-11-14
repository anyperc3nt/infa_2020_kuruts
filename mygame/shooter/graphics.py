import pygame
import math
import numpy as np
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint

#import main
from settings import *
import textures
#main.screen

def blit_pivot_to_center_rot(source,x,y,rot):
    """x,y - координаты точки пивота отн центра"""
    rot_rad=rot/180*np.pi
    dx=int(Xscreensize/2)
    dy=int(Yscreensize/2)

    source_rot=pygame.transform.rotate(source,rot)

    dx1=abs(dx*math.cos(rot_rad))+abs(dy*math.sin(rot_rad))
    dy1=abs(dy*math.cos(rot_rad))+abs(dx*math.sin(rot_rad))
    dx=(dx-dx1)*scale
    dy=(dy-dy1)*scale

    Xpivot=-x*math.cos(rot_rad)+y*math.sin(rot_rad)
    Ypivot=+x*math.sin(rot_rad)+y*math.cos(rot_rad)
    pygame.Surface.blit(screen,source_rot,(int(Xpivot+dx),int(Ypivot+dy)))


def blit_pivot_to_center(source,x,y):
    pygame.Surface.blit(screen,source,(0,0))


def init():
    global screen
    screen = pygame.display.set_mode((Xscreensize, Yscreensize))
    pygame.display.update()
    textures.init()

    global layer_blank
    layer_blank = textures.make_transp(pygame.Surface((Xmodelsize,Ymodelsize)))
    #global screen_blank
    #screen_blank = textures.make_transp(pygame.Surface((Xscreensize,Yscreensize)))
    global layer_curr #текущий слой 
    global layer_motionblur #слой с накоплением предыдущих слоев (для моушенблюра)
    global layer_motionblur_blur #рызмытый слой layer_motionblur
    layer_curr = layer_blank
    layer_motionblur = layer_blank
    layer_motionblur_blur = layer_blank
    layer_motionblur.fill((0,0,0,255))

    global layerblack
    layerblack = textures.make_transp(pygame.Surface((Xmodelsize,Ymodelsize)))
    layerblack.fill(textures.BLACKforBM)


def draw(name,x,y,rot=0):
    """функция отрисовки объекта на слой короче на главный слой, который я потом перемещаю, поворачиваю и отображаю на экране"""
    if name == "player":
        tex=textures.ball1
    if name == "enemy":
        tex=textures.ball2
    pygame.Surface.blit(layer_curr,tex,(int(x-pygame.Surface.get_width(tex)/2),int(y-pygame.Surface.get_height(tex)/2)))


def motionblur_tick():
    global layer_curr 
    global layer_motionblur 
    global layer_motionblur_blur 
    global layerblack
    #тик обработки слоев
    pygame.Surface.blit(layer_motionblur,layerblack,(0,0))
    pygame.Surface.blit(layer_motionblur,layer_curr,(0,0))
    #моуушенблюр
    layer_motionblur_blur = pygame.Surface.copy(layer_motionblur)
    layer_motionblur_blur = pygame.transform.smoothscale(layer_motionblur_blur,(int(Xscreensize/motionblur_blurforce),int(Yscreensize/motionblur_blurforce)))
    layer_motionblur_blur = pygame.transform.smoothscale(layer_motionblur_blur,(Xscreensize,Yscreensize))
    pygame.Surface.set_alpha(layer_motionblur_blur, motionblur_brightness)
    

def update(x,y,rot,scale=1):
    global layer_curr
    global layer_motionblur_blur

    screen.fill(textures.BACKG)

    x*=Xscreensize/Xmodelsize*scale
    y*=Yscreensize/Ymodelsize*scale
    Xs=Xscreensize*scale
    Ys=Yscreensize*scale
    blit_pivot_to_center_rot(pygame.transform.smoothscale(layer_motionblur_blur,(Xs,Ys)),x,y,rot)
    blit_pivot_to_center_rot(pygame.transform.smoothscale(layer_curr,(Xs,Ys)),x,y,rot)
    #blit_pivot_to_center(pygame.transform.smoothscale(layer_motionblur_blur,(Xscreensize,Yscreensize)),x,y)
    pygame.display.update()

    #стирание слоя перед след кадром
    layer_curr = textures.make_transp(pygame.Surface((Xmodelsize,Ymodelsize)))


