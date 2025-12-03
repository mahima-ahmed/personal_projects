import math
from turtle import *

def heart_a(k):
    return 15*math.sin(k)**3
def heart_b(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)
speed(0) # speed can be customized, if you want it fast, just increase the number
bgcolor('black') # background colour can be customized
for i in range(360):
    goto(heart_a(i)*20, heart_b(i)*20)
    for j in range(5):
        color('maroon') # colour of the heart can be also customized to your preference
    goto(0,0)
done()
