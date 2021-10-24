import math
from random import choice
from random import randint as rnd
import pygame
from pygame.draw import *

FPS = 60

TRANSPARENT = (0, 0, 0, 0)

GREY = (150, 150, 150)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

g = 0.6


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.x += self.vx
        self.y -= self.vy
        self.vy -= g
        if(self.y > HEIGHT-self.r):
            self.y = HEIGHT-self.r
            self.vy *= -0.7

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r,
            width=1
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x-obj.x)**2+(self.y-obj.y)**2 <= (self.r+obj.r)**2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

        self.x = 40
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2(
            (event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)/2
        new_ball.vy = - self.f2_power * math.sin(self.an)/2
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if(event.pos[0]-20):
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """surf = pygame.Surface((self.f2_power+20, 10)).convert_alpha()
        surf.fill(TRANSPARENT)
        rect(surf, self.color, (0, 0,self.f2_power+20,10))
        pygame.Surface.blit(self.screen, pygame.transform.rotate(surf, -self.an), (self.x, self.y))"""

        #line(self.screen, self.color, (self.x,self.y), (self.x+(self.f2_power+20)*math.cos(self.an),self.y+(self.f2_power+20)*math.sin(self.an)), width=10)
        width = 10
        coords = [
            (self.x, self.y),
            (self.x+(self.f2_power+20)*math.cos(self.an),
             self.y+(self.f2_power+20)*math.sin(self.an)),
            (self.x+(self.f2_power+20)*math.cos(self.an)+width*math.sin(self.an),
             self.y+(self.f2_power+20)*math.sin(self.an)-width*math.cos(self.an)),
            (self.x+width*math.sin(self.an), self.y-width*math.cos(self.an))
        ]

        polygon(self.screen, self.color, (coords), width=0)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, live=1):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.color = RED
        self.live = live

    def hit(self, point=1):
        """Попадание шарика в цель."""
        self.live -= 1
        global points
        points += point

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            screen,
            BLACK,
            (self.x, self.y),
            self.r,
            width=1
        )


def drawscore():
    """вывод очков на экран"""
    f1 = pygame.font.Font(None, 36)
    tbl = 'points: '
    tbl += str(points)
    text1 = f1.render(tbl, True, BLACK)
    screen.blit(text1, (10, 10))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
points = 0

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False


def showtext():
    screen.fill(WHITE)
    f1 = pygame.font.Font(None, 36)
    tbl = 'вы уничтожили цель за '
    tbl += str(bullet)
    tbl += ' выстрелов'
    text1 = f1.render(tbl, True, BLACK)
    screen.blit(text1, (180, 250))
    pygame.display.update()
    for i in range(1, 100):
        clock.tick(FPS)


while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    drawscore()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target):
            target.hit()
            if(target.live == 0):
                target = Target()
                bullet = 0
                balls = []
                showtext()
    gun.power_up()

pygame.quit()
