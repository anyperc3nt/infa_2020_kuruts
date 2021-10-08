import pygame
import sys
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
Xbound=800
Ybound=800
screen = pygame.display.set_mode((Xbound, Ybound))

transparent = (0,0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class myobject(object):
    """класс объекта, который имеет свой surface для отрисовки и может передвигаться по экране"""
    def __init__(self, surface, x, y , vx, vy, r):
        """Constructor"""
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
    
    def draw(self):
        """
        отображает себя на экране
        """
        pygame.Surface.blit(screen, self.surface, (self.x-self.r,self.y-self.r))

    def move(self):
        """
        перемещает себя значение скорости
        """
        self.x+=self.vx
        self.y+=self.vy

class table(object):
    """docstring"""
    def __init__(self, points):
        """Constructor"""
        self.points = points
    
    def draw(self):
        f1 = pygame.font.Font(None, 36)
        tbl = 'points: '
        tbl+=str(self.points)
        text1 = f1.render(tbl, True,GREEN)
        screen.blit(text1, (10, 10))

def click_object(event, obj):
    if((obj.x-event.pos[0])**2 + (obj.y-event.pos[1])**2<=obj.r**2):
        table1.points+=1
        obj.x=50

def collision(objects):
    for obj in objects:
        if(obj.x + obj.r > Xbound):
            obj.vx*=-1
            obj.x=Xbound-obj.r
        elif(obj.x - obj.r < 0):
            obj.vx*=-1
            obj.x=obj.r
        elif(obj.y - obj.r < 0):
            obj.vy*=-1
            obj.y=obj.r
        elif(obj.y + obj.r > Ybound):
            obj.vy*=-1
            obj.y=Ybound-obj.r

ball1 = pygame.Surface((50,50))
ball1 = ball1.convert_alpha()
ball1.fill(transparent)
circle(ball1, BLUE, (25, 25), 25)
balls = [myobject(ball1,randint(1,Xbound),randint(1,Ybound),randint(1,5),randint(1,5),25) for i in range(1,10)]

table1=table(0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                click_object(event,ball)
    
    for ball in balls:
        ball.move()
        ball.draw()
    collision(balls)
    table1.draw()

    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()