"""
已对此源代码进行更新：
1. 进行分模块
2. 使用多线程提供背景音乐播放
【源代码最新地址】: https://github.com/RidingRoad/PythonFun/tree/master/Draw_520_with_Turtle
"""

from turtle import *
import math,sys

#绘制5
bgcolor("#fbbc05")
penup()
back(200)
pendown()
color("red","#4285f4")
begin_fill()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(80)
right(90)
forward(20)
right(90)
forward(60)
left(90)
forward(20)
left(90)
forward(60)
right(90)
forward(100)
right(90)
forward(80)
right(90)
forward(20)
end_fill()

#从5移动到2的起点
penup()
backward(20)
right(90)
forward(100)

# 绘制2
pendown()
color("red","#34a853")
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
# right(90)
# forward(60)
end_fill()

#2移动到0的起点
penup()
backward(110)
right(90)
forward(10)
pendown()
right(90)

#绘制0
pencolor("#ea4335")
pensize(20)
begin_fill()
forward(60)
left(90)
forward(120)
left(90)
forward(60)
left(90)
forward(120)

#移动到5的下面
penup()
pensize(1)
right(90)
forward(210)
left(90)
forward(15)

#在5的下面绘制RR

#第一个R
color("red","black")
begin_fill()
pendown()
forward(40)
left(90)
forward(10)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(5)
right(90)
forward(19)
left(90)
forward(10)
left(45)
forward(int(math.sqrt(pow(15,2)+pow(25,2))))
left(90)
forward(10)
left(90)
forward(int(math.sqrt(pow(10,2)+pow(25,2))))
right(135)
forward(15)
left(90)
forward(15)
left(90)
forward(40)
end_fill()

#移动到画第二个R的起点，相隔2px吧
penup()
backward(42)
left(90)

#画第二个R
color("red","black")
begin_fill()
pendown()
forward(40)
left(90)
forward(10)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(5)
right(90)
forward(19)
left(90)
forward(10)
left(45)
forward(int(math.sqrt(pow(15,2)+pow(25,2))))
left(90)
forward(10)
left(90)
forward(int(math.sqrt(pow(10,2)+pow(25,2))))
right(135)
forward(15)
left(90)
forward(17)
left(90)
forward(40)
end_fill()

#移动到0下面
penup()
backward(190)




#在0的下面绘制CY
# 先绘制C
color("red","black")
pendown()
begin_fill()
circle(27,200)
left(90)
fd(2)
right(90)
circle(18,-200)
right(90)
fd(10)
end_fill()


#绘制Y
#移动到Y的起点，相隔2px
penup()
right(90)
fd(2)
#开始绘制Y
color("red","black")


right(45)
fd(12)
pendown()
begin_fill()
forward(int(math.sqrt(pow(7,2)+pow(20,2))))
right(45)
fd(20)
left(90)
fd(10)
left(90)
fd(20)
right(45)
fd(int(math.sqrt(pow(7,2)+pow(20,2))))
left(90)
fd(10)
left(90)
fd(int(math.sqrt(pow(7,2)+pow(18,2))))
right(90)
fd(int(math.sqrt(pow(7,2)+pow(18,2))))
right(90)
fd(10)
end_fill()
backward(4)
done()


input("按任意键退出:") # 用来显示，以免程序退出
