# 화면에서 마우스 왼쪽 버튼을 누르면 
# 클릭한 위치에 다양한 색상, 크기, 각도의 거북이 모양 도장이 찍히는 프로그램
import turtle
import random 

turtle.shape('turtle')
turtle.penup()

## 변수 선언부 ##
global r, g, b
tSize = 10
angle = 0

## 함수 선언부 ##
def clickLeft(x,y):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))
    
    tSize = random.randint(1, 10)
    turtle.shapesize(tSize)
    
    angle = random.randint(0, 360)
    turtle.right(angle)
    
    turtle.stamp()
    turtle.goto(x,y)

r, g, b = 0.0, 0.0, 0.0
## 메인 코드 ##

turtle.onscreenclick(clickLeft,1)

turtle.done()