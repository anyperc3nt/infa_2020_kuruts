import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((600, 800), pygame.SRCALPHA)
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
rect(screen, (220, 220, 220), (0, 0, 800, 400), 0)
def drawiglu(xcor, ycor, size):
    circle(screen, (220, 220, 220), (xcor, ycor + 35 * size), 175 * size)
    circle(screen, (0, 0, 0), (xcor, ycor + 35 * size), 175 * size, 1)
    rect(screen, (255, 255, 255), (xcor - 195 * size, ycor, 500 * size, 1000 * size))
    arc(screen, (0, 0, 0), (xcor - 55 * size, ycor - 140 * size, 110 * size, 20 * size), 3.14, 6.28, 1)
    arc(screen, (0, 0, 0), (xcor - 110 * size, ycor - 115 * size, 220 * size, 30 * size), 3.14, 6.28, 1)
    arc(screen, (0, 0, 0), (xcor - 150 * size, ycor - 65 * size, 300 * size, 25 * size), 3.14, 6.28, 1)
    line(screen, (0, 0, 0), (xcor - 170 * size, ycor), (xcor + 170 * size, ycor))

    line(screen, (0, 0, 0), (xcor - 115 * size, ycor - 45 * size), (xcor - 125 * size, ycor), 1)
    line(screen, (0, 0, 0), (xcor - 40 * size, ycor - 42 * size), (xcor - 45 * size, ycor), 1)
    line(screen, (0, 0, 0), (xcor + 25 * size, ycor - 42 * size), (xcor + 27 * size, ycor), 1)
    line(screen, (0, 0, 0), (xcor + 80 * size, ycor - 44 * size), (xcor + 87 * size, ycor), 1)
    line(screen, (0, 0, 0), (xcor + 130 * size, ycor - 47 * size), (xcor + 140 * size, ycor - 1 * size), 1)

    line(screen, (0, 0, 0), (xcor - 72 * size, ycor - 90 * size), (xcor - 85 * size, ycor - 45 * size), 1)
    line(screen, (0, 0, 0), (xcor - 5 * size, ycor - 85 * size), (xcor - 5 * size, ycor - 42 * size), 1)
    line(screen, (0, 0, 0), (xcor + 48 * size, ycor - 87 * size), (xcor + 53 * size, ycor - 44 * size), 1)
    line(screen, (0, 0, 0), (xcor + 99 * size, ycor - 93 * size), (xcor + 115 * size, ycor - 45 * size), 1)

    line(screen, (0, 0, 0), (xcor - 35 * size, ycor - 123 * size), (xcor - 45 * size, ycor - 87 * size))
    line(screen, (0, 0, 0), (xcor + 13 * size, ycor - 120 * size), (xcor + 17 * size, ycor - 87 * size))
    line(screen, (0, 0, 0), (xcor + 50 * size, ycor - 126 * size), (xcor + 67 * size, ycor - 89 * size))

def draweskimos(xcor, ycor, size, orientation):
    if orientation == 1:
        ellipse(screen, (220, 220, 220), (xcor - 50 * size, ycor - 50 * size, 200 * size, 140 * size), 0)
        arm = pygame.Surface((100 * size, 30 * size))
        arm.fill((255, 255, 255))
        ellipse(arm, (138, 102, 66), (0, 0, 100 * size, 30 * size))
        arm = pygame.transform.rotate(arm, -35)
        pygame.Surface.blit(screen, arm, (xcor + 60 * size, ycor + 80 * size))
        ellipse(screen, (138, 102, 66), (xcor - 60 * size, ycor + 100 * size, 100 * size, 30 * size))
        ellipse(screen, (138, 102, 66), (xcor - 25 * size, ycor + 40 * size, 150 * size, 300 * size))
        ellipse(screen, (138, 102, 66), (xcor - 30 * size, ycor - 30 * size, 160 * size, 120 * size))
        ellipse(screen, (244, 222, 204), (xcor, ycor, 100 * size, 60 * size), 0)
        rect(screen, (255, 255, 255), (xcor - 50 * size, ycor + 200 * size, 200 * size, 200 * size))
        ellipse(screen, (138, 102, 66), (xcor - 10 * size, ycor + 100 * size, 45 * size, 150 * size))
        ellipse(screen, (138, 102, 66), (xcor + 60 * size, ycor + 100 * size, 45 * size, 150 * size))
        ellipse(screen, (138, 102, 66), (xcor - 23 * size, ycor + 230 * size, 50 * size, 25 * size))
        ellipse(screen, (138, 102, 66), (xcor + 65 * size, ycor + 230 * size, 50 * size, 25 * size))
        rect(screen, (101, 67, 33), (xcor + 20 * size, ycor + 80 * size, 35 * size, 120 * size))
        rect(screen, (101, 67, 33), (xcor - 25 * size, ycor + 200 * size, 150 * size, 15 * size))
        line(screen, (0, 0, 0), (xcor - 50 * size, ycor), (xcor - 47 * size, ycor + 240 * size), 2)
        line(screen, (0, 0, 0), (xcor + 15 * size, ycor + 15 * size), (xcor + 35 * size, ycor + 25 * size), 2)
        line(screen, (0, 0, 0), (xcor + 80 * size, ycor + 15 * size), (xcor + 60 * size, ycor + 25 * size), 2)
        line(screen, (0, 0, 0), (xcor + 30 * size, ycor + 40 * size), (xcor + 70 * size, ycor + 40 * size), 2)

    if orientation == -1:
        ellipse(screen, (220, 220, 220), (xcor - 50 * size, ycor - 50 * size, 200 * size, 140 * size), 0)
        arm = pygame.Surface((100 * size, 30 * size))
        arm.fill((255, 255, 255))
        ellipse(arm, (138, 102, 66), (0, 0, 100 * size, 30 * size))
        arm = pygame.transform.rotate(arm, +35)
        pygame.Surface.blit(screen, arm, (xcor - 60 * size, ycor + 80 * size))
        ellipse(screen, (138, 102, 66), (xcor + 60 * size, ycor + 100 * size, 100 * size, 30 * size))
        ellipse(screen, (138, 102, 66), (xcor - 25 * size, ycor + 40 * size, 150 * size, 300 * size))
        ellipse(screen, (138, 102, 66), (xcor - 30 * size, ycor - 30 * size, 160 * size, 120 * size))
        ellipse(screen, (244, 222, 204), (xcor, ycor, 100 * size, 60 * size), 0)
        rect(screen, (255, 255, 255), (xcor - 50 * size, ycor + 200 * size, 200 * size, 200 * size))
        ellipse(screen, (138, 102, 66), (xcor - 10 * size, ycor + 100 * size, 45 * size, 150 * size))
        ellipse(screen, (138, 102, 66), (xcor + 60 * size, ycor + 100 * size, 45 * size, 150 * size))
        ellipse(screen, (138, 102, 66), (xcor - 23 * size, ycor + 230 * size, 50 * size, 25 * size))
        ellipse(screen, (138, 102, 66), (xcor + 65 * size, ycor + 230 * size, 50 * size, 25 * size))
        rect(screen, (101, 67, 33), (xcor + 20 * size, ycor + 80 * size, 35 * size, 120 * size))
        rect(screen, (101, 67, 33), (xcor - 25 * size, ycor + 200 * size, 150 * size, 15 * size))
        line(screen, (0, 0, 0), (xcor + 150 * size, ycor), (xcor + 147 * size, ycor + 240 * size), 2)
        line(screen, (0, 0, 0), (xcor + 15 * size, ycor + 15 * size), (xcor + 35 * size, ycor + 25 * size), 2)
        line(screen, (0, 0, 0), (xcor + 80 * size, ycor + 15 * size), (xcor + 60 * size, ycor + 25 * size), 2)
        line(screen, (0, 0, 0), (xcor + 30 * size, ycor + 40 * size), (xcor + 70 * size, ycor + 40 * size), 2)

def drawkoshecka(xcor, ycor, size):
    tail = pygame.Surface((120 * size, 20 * size))
    tail.fill((255, 255, 255))
    ellipse(tail, (220, 220, 220), (0, 0, 120 * size, 20 * size))
    tail = pygame.transform.rotate(tail, 30)
    pygame.Surface.blit(screen, tail, (xcor + 45 * size, ycor - 95 * size))
    leg1 = pygame.Surface((70 * size, 20 * size))
    leg1.fill((255, 255, 255))
    ellipse(leg1, (220, 220, 220), (0, 0, 70 * size, 20 * size))
    leg1 = pygame.transform.rotate(leg1, -135)
    pygame.Surface.blit(screen, leg1, (xcor - 145 * size, ycor - 45 * size))
    pygame.Surface.blit(screen, leg1, (xcor - 90 * size, ycor - 40 * size))
    leg1 = pygame.transform.rotate(leg1, 90)
    ear = pygame.Surface((16 * size, 9 * size))
    ear.fill((255, 255, 255))
    ellipse(ear, (220, 220, 220), (0, 0, 16 * size, 9 * size))
    ear = pygame.transform.rotate(ear, 115)
    teeth = pygame.Surface((10 * size, 4 * size))
    teeth.fill((163, 198, 192))
    ellipse(teeth, (255, 255, 255), (0, 0, 10 * size, 4 * size))
    teeth = pygame.transform.rotate(teeth, -90)
    pygame.Surface.blit(screen, leg1, (xcor + 30 * size, ycor - 45 * size))
    pygame.Surface.blit(screen, tail, (xcor + 55 * size, ycor - 105 * size))
    pygame.Surface.blit(screen, leg1, (xcor - 20 * size, ycor - 45 * size))
    ellipse(screen, (220, 220, 220), (xcor - 100 * size, ycor - 50 * size, 170 * size, 30 * size))
    ellipse(screen, (255, 0, 0), (xcor - 68 * size, ycor - 40 * size, 10 * size, 5 * size))
    ellipse(screen, (163, 198, 192), (xcor - 95 * size, ycor - 45 * size, 30 * size, 15 * size))
    circle(screen, (8, 37, 103), (xcor - 90 * size, ycor - 38 * size), 3 * size)
    pygame.Surface.blit(screen, ear, (xcor - 85 * size, ycor - 79 * size))
    ear = pygame.transform.rotate(ear, -55)
    pygame.Surface.blit(screen, ear, (xcor - 73 * size, ycor - 79 * size))
    pygame.Surface.blit(screen, teeth, (xcor - 86 * size, ycor - 47 * size))
    pygame.Surface.blit(screen, teeth, (xcor - 76 * size, ycor - 47 * size))
    ellipse(screen, (220, 220, 220), (xcor - 100 * size, ycor - 70 * size, 45 * size, 30 * size))
    ellipse(screen, (255, 255, 255), (xcor - 96 * size, ycor - 66 * size, 12 * size, 8 * size))
    ellipse(screen, (255, 255, 255), (xcor - 78 * size, ycor - 62 * size, 12 * size, 8 * size))
    circle(screen, (0, 0, 0), (xcor - 68 * size, ycor - 57 * size), 2 * size)
    circle(screen, (0, 0, 0), (xcor - 86 * size, ycor - 61 * size), 2 * size)
    circle(screen, (0, 0, 0), (xcor - 85 * size, ycor - 52 * size), 2 * size)


drawiglu(110, 425, 0.3)
drawiglu(320, 450, 0.3)
drawiglu(205, 480, 0.75)
drawiglu(130, 530, 0.5)
drawiglu(250, 570, 0.5)
draweskimos(540, 400, 0.25, 1)
draweskimos(450, 390, 0.25, 1)
draweskimos(480, 445, 0.25, 1)
draweskimos(390, 500, 0.25, -1)
draweskimos(460, 520, 0.25, -1)
draweskimos(550, 530, 0.25, 1)
draweskimos(480, 600, 0.75, 1)
drawkoshecka(200, 780, 0.5)
drawkoshecka(150, 700, 1)
drawkoshecka(70, 600, 0.5)
drawkoshecka(340, 715, 0.55)


pygame.display.update()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()