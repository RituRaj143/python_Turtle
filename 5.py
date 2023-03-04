import colorsys
import turtle
turtle.bgcolor("black")
t=turtle.Turtle()
t.speed(10)
n=36
h=0
for i in range(460):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(145)
    for j in range(5):
        t.fd(300)
        t.lt(150)
