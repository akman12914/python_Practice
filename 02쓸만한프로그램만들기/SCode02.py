import turtle
import random 

##마우스 왼쪽 버튼을 누르면 거북이가 클릭한 지점까지 따라오는 프로그램##










global r,g,b;

def screenLeftClick(x, y):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    turtle.pendown()
    turtle.goto(x,y)


def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

##변수선언##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

##메인코드실행##
turtle.title("거북이로 그림그리기")
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
