#거북이가 서로 만나게 하기
#거북이 세 마리는 서로 만날 때까지 임의로 화면을 돌아다닌다. 세 마리 중 서로 만나는 거북이가 있다면 움직임을 멈추고, 모든 거북이의 크기를 세 배로 키운다.
import turtle
import math
import random 

t1, t2, t3 = [None] * 3
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6
swidth, sheight = 300, 300

turtle.title("거북이 만나기")
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)

t1 = turtle.Turtle('turtle'); t1.color('red'); t1.penup(); t1.speed(0)
t2 = turtle.Turtle('turtle'); t2.color('navyblue'); t2.penup(); t2.speed(0)
t3 = turtle.Turtle('turtle'); t3.color('pink'); t3.penup(); t3.speed(0)

t1.goto(-100, - 100); t2.goto(0, 0); t3.goto(100, 100)

while True :
    angle = random.randrange(0, 360)
    dist = random.randrange(1, 50)
    t1.left(angle); t1.forward(dist)
    angle = random.randrange(0, 360)
    dist = random.randrange(1, 50)
    t2.left(angle); t2.forward(dist)
    angle = random.randrange(0, 360)
    dist = random.randrange(1, 50)
    t3.left(angle); t3.forward(dist)
    
    t1X = t1.xcor(); t1Y = t1.ycor()
    t2X = t2.xcor(); t2Y = t2.ycor()
    t3X = t3.xcor(); t3Y = t3.ycor()
    
    if t1X >= 500 or t1Y >=500 or \
       t2X >= 500 or t2Y >= 500 or \
       t3X >= 500 or t3Y >= 500 : 
           t1.goto(-100, - 100); t2.goto(0, 0); t3.goto(100, 100)
    
    if math.sqrt(((t1X - t2X) * (t1X - t2X)) + ((t1Y - t2Y) * (t1Y - t2Y))) <=20 or \
        math.sqrt(((t1X - t3X) * (t1X - t3X)) + ((t1Y - t3Y) * (t1Y - t3Y))) <=20 or \
        math.sqrt(((t2X - t3X) * (t2X - t3X)) + ((t2Y - t3Y) * (t2Y - t3Y))) <=20 :
        t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
        break

turtle.done()
    