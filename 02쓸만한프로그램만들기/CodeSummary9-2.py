#마우스 왼쪽 버튼을 누른 좌표까지 거북이가 선을 그리기
import turtle

turtle.shape('turtle')

def screenLeft(x, y):
    turtle.pendown()
    turtle.goto(x, y)
    
turtle.onscreenclick(screenLeft, 1)

turtle.done()