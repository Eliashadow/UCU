from turtle import *
from math import sin

#Setup
setup(width=600, height=400)
bgcolor("white")
speed(0)

penup()
goto(-120,-120)
pendown()

#Body
color("black", "dark red")
width(8)
begin_fill()
right(90)
forward(50)
right(90)
forward(90)
right(90)
forward(100)
backward(50)
left(45)
forward(70)
for i in range(45):
    forward(1)
    right(2)
forward(70)
left(45)
for i in range(50):
    forward(2)
    left(0.15)
right(85)
forward(100)
right(12.5)
forward(200)
for i in range(45):
    forward(1)
    right(2)
forward(100)
left(90)
forward(30)
left(65)
backward(20)
forward(50)
left(25)
forward(5)
for i in range(100):
    forward(0.4)
    right(1.8)
forward(30)
left(90)
forward(30)
for i in range(100):
    forward(0.4)
    right(1.8)
forward(10)
left(180)
forward(20)
for i in range(100):
    forward(0.4)
    right(1.8)
forward(10)
left(180)
for i in range(100):
    forward(0.4)
    right(1.8)
left(10)
forward(100)
left(80)
forward(93)
right(90)
forward(83)
right(90)
forward(50)
left(90)
backward(20)
forward(190)
end_fill()


#Teeth
width(5)
penup()
goto(60, 0)
pendown()
color("black", "black")
begin_fill()
forward(220)
left(90)
for i in range(240):
  left(1)
  forward(1.5)
  right(0.25)
end_fill()

width(1)
penup()
goto(-120, 0)
pendown()
color("white", "white")
begin_fill()
left(180)
forward(20)
for i in range(90):
  left(1)
  forward(0.5)
left(180)
for i in range(90):
  left(1)
  forward(0.5)
forward(9)

for i in range(150):
  forward(1)
  goto(-119 + i, -90 + sin(i / 10) * 5)

left(180)
for i in range(90):
  left(1)
  forward(0.5)
left(180)
for i in range(90):
  left(1)
  forward(0.5)
forward(30)
end_fill()

penup()
goto(-70, 0)
color("black", "black")
begin_fill()
pendown()
left(180)
for i in range(4):
    forward(40)
    left(90)
end_fill()


#Eyes
penup()
goto(30, 80)
pendown()
dot(60, "black")

penup()
goto(15, 95)
pendown()
dot(20, "white")

penup()
goto(50, 65)
pendown()
dot(8, "white")

penup()
goto(-140, 80)
pendown()
dot(60, "black")

penup()
goto(-155, 95)
pendown()
dot(20, "white")

penup()
goto(-165, 50)
width(5)
left(180)
color("black", "dark red")
begin_fill()
pendown()
for i in range(180):
    forward(0.5)
    right(1)
end_fill()


width(3)
color("black", "white")
penup()
goto(-95, 100)
setheading(30)
pendown()
begin_fill()
for i in range(2):
    forward(60)
    right(90)
    forward(20)
    right(90)
end_fill()

penup()
goto(-75, 140)
setheading(-60)
pendown()
begin_fill()
for i in range(2):
    forward(60)
    right(90)
    forward(20)
    right(90)
end_fill()

hideturtle()
done()