import pygame
import sys
from pygame.constants import WINDOWHITTEST
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
Xbound=800
Ybound=800
screen = pygame.display.set_mode((Xbound, Ybound))

transparent = (0,0,0,0)
backg = (50, 50, 70)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def make_transp(scr):
    """делает surface прозрачным"""
    scr1 = scr.convert_alpha()
    scr1.fill(transparent)
    return scr1

class myobject(object):
    """класс объекта, который имеет свой surface для отрисовки и может передвигаться по экране

    surface: принимает surface для использования в качестве текстурки
    x, y , vx, vy: положение объекта на экране и его скорость
    r: радиус коллизии
    type: значение типа, позволяет отличать объекты друг от друга    

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
    """класс таблицы, хранит количество очков и координаты отрисовки, позволяет отобразить кол-во очков на экране
    
    points: число для вывода на экран
    x,y - координаты надписи на экране
    
    """
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
    """получает объект класса myobject и событие event, при нажатии на объект определенного типа делает действие"""
    if((obj.x-event.pos[0])**2 + (obj.y-event.pos[1])**2<=obj.r**2):
        if obj.type==2:
            pygame.quit()
        elif obj.type==0:
            table1.points+=1
        elif obj.type==1:
            table1.points+=10

def collision(obj):
    """функция коллизии, получает объект класса myobject и при столкновении отражает его от стен
    
    Xbound, Ybound - границы экрана, заданы вне функции

    при типе объекта:
    0 - дает +1 очко
    1 - дает +10 очков
    2 - проиграл
    
    """
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

#создаем таблицу учета очков
table1=table(YELLOW,0,10,10)

#создаем surface шара и surface квадратикa
ball1 = make_transp(pygame.Surface((70,70)))
circle(ball1, BLUE, (35, 35), 35)

square1 = make_transp(pygame.Surface((70,70)))
rect(square1, GREEN, (0, 0,70,70))
circle(square1, BLACK, (20, 25), 5)
circle(square1, BLACK, (50, 25), 5)
rect(square1, BLACK, (15, 50,40,7))

square2 = make_transp(pygame.Surface((100,100)))
rect(square2, RED, (0, 0,100,100))
circle(square2, WHITE, (30, 30), 7)
circle(square2, WHITE, (70, 30), 7)
rect(square2, WHITE, (25, 60,50,10))

#и наконец массив объектов трех типов: шариков, квадратиков и третьего который я еще не придумал
all_objects = [
    [myobject(ball1,randint(1,Xbound-35),randint(1,Ybound-35),randint(1,5),randint(1,5),35,0) for i in range(1,20)],
    [myobject(square1,randint(1,Xbound-35),randint(1,Ybound-35),randint(1,5),randint(1,5),35,1) for i in range(1,4)],
    [myobject(square2,randint(1,Xbound-35),randint(1,Ybound-35),randint(1,5),randint(1,5),35,2) for i in range(1,15)]
]

"""типы объектов

0 - кружочек
1 - квадратик

"""

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for objects in all_objects:
                for obj in objects:
                    click_object(event,obj)
    
    for objects in all_objects:
        for obj in objects:
            obj.move()
            collision(obj)
            obj.draw()

    table1.draw()

    pygame.display.update()
    screen.fill(backg)

pygame.quit()