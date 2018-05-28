"""绘制图案5"""
from turtle import *


def draw():
    # 从5移动到2的起点
    penup()
    backward(20)
    right(90)
    forward(100)

    # 绘制2
    pendown()
    color("#34a853", "#34a853")
    begin_fill()
    left(90)
    forward(80)
    right(90)
    forward(60)
    left(90)
    forward(40)
    left(90)
    forward(40)
    left(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    forward(40)
    right(90)
    forward(80)
    right(90)
    forward(80)
    right(90)
    forward(60)
    left(90)
    forward(40)
    left(90)
    forward(60)
    right(90)
    forward(20)
    right(90)
    forward(80)
    end_fill()
