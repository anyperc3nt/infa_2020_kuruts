import turtle as t
t.shape('turtle')
t.speed(10)

from random import *

#randint(a, b)

for i in range (1,30):
    t.forward(30)
    t.left(randint(-180, 180))