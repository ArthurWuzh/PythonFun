"""绘制CY"""

from turtle import *
import math, time


def draw():
    # 移动到0下面
    penup()
    backward(190)

    # 在0的下面绘制CY
    # 先绘制C
    color("black", "black")
    pendown()
    begin_fill()
    circle(27, 200)
    left(90)
    fd(2)
    right(90)
    circle(18, -200)
    right(90)
    fd(10)
    end_fill()

    # 绘制Y
    # 移动到Y的起点，相隔2px
    penup()
    right(90)
    fd(2)
    # 开始绘制Y
    color("black", "black")

    right(45)
    fd(12)
    pendown()
    begin_fill()
    forward(int(math.sqrt(pow(7, 2) + pow(20, 2))))
    right(45)
    fd(20)
    left(90)
    fd(10)
    left(90)
    fd(20)
    right(45)
    fd(int(math.sqrt(pow(7, 2) + pow(20, 2))))
    left(90)
    fd(10)
    left(90)
    fd(int(math.sqrt(pow(7, 2) + pow(18, 2))))
    right(90)
    fd(int(math.sqrt(pow(7, 2) + pow(18, 2))))
    right(90)
    fd(10)
    end_fill()
    backward(4)
    done()

    time.sleep(120)  # 用来显示，以免程序退出
    input("按任意键退出:")
