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
backg = (50, 50, 70)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class myobject(object):
    """
    класс объекта, который имеет свой surface для отрисовки и может передвигаться по экране
    имеет значение type, позволяющую отличать объекты друг от друга    
    """
    def __init__(self, surface, x, y , vx, vy, r, type):
        """конструктор"""
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.type = type
    
    def draw(self):
        """отображает себя на экране"""
        pygame.Surface.blit(screen, self.surface, (self.x-self.r,self.y-self.r))

    def move(self):
        """перемещает себя значение скорости"""
        self.x+=self.vx
        self.y+=self.vy

class table(object):
    """класс таблицы, хранит количество очков и координаты отрисовки, позволяет отобразить кол-во очков на экране"""
    def __init__(self, color, points,x,y):
        """конструктор"""
        self.points = points
        self.color = color
        self.x = x
        self.y = y
    
    def draw(self):
        """вывод очков на экран"""
        f1 = pygame.font.Font(None, 36)
        tbl = 'points: '
        tbl+=str(self.points)
        text1 = f1.render(tbl, True,self.color)
        screen.blit(text1, (self.x, self.y))

def click_object(event, obj):
    if((obj.x-event.pos[0])**2 + (obj.y-event.pos[1])**2<=obj.r**2):
        if obj.type==1:
            table1.points+=1
        elif obj.type==2:
            table1.points+=10

def collision(objects):
    """функция коллизии, получает список объектов и при столкновении отражает их от стен"""
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



#создаем surface шара и массив объектов шаров
ball1 = pygame.Surface((50,50))
ball1 = ball1.convert_alpha()
ball1.fill(transparent)
circle(ball1, BLUE, (25, 25), 25)
balls = [myobject(ball1,randint(1,Xbound),randint(1,Ybound),randint(1,5),randint(1,5),25,1) for i in range(1,10)]
#создаем таблицу учета очков
table1=table(YELLOW,0,10,10)

#создаем surface шара и массив объектов шаров
square1 = pygame.Surface((70,70))
square1 = square1.convert_alpha()
square1.fill(transparent)
rect(square1, GREEN, (0, 0,70,70))
circle(square1, BLACK, (20, 25), 5)
circle(square1, BLACK, (50, 25), 5)
rect(square1, BLACK, (15, 50,40,7))
squares = [myobject(square1,randint(1,Xbound),randint(1,Ybound),randint(1,5),randint(1,5),35,2) for i in range(1,10)]

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
            for square in squares:
                click_object(event,square)
    

    """ тут не красиво конечно, так как из-за двух типов объектов код копипастится два раза
        надо будет создать список из всех объектов сразу
    """
    for ball in balls:
        ball.move()
        ball.draw()
    collision(balls)

    for square in squares:
        square.move()
        square.draw()
    collision(squares)

    table1.draw()

    pygame.display.update()
    screen.fill(backg)

pygame.quit()