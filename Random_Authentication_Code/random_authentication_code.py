import random

"""背景知识"""
"""
1、ord(char) 返回字符char的ASCII码点
2、chr(int)  返回ASCII码点为int的字符
3、random.randint(1,3) 返回1到3之间的一个随机整数,包含1和3
4、range(a,b)  返回一个可迭代(遍历)<class 'range'>对象,内部有a 到 b-1之间的整数值
5、''.join(sequence) 返回一个由sequence序列元素和拼接符''(此处为空字符)拼接而成的字符串
6、print(ord('a'))#97
7、print(ord('z'))#122
8、print(ord('A'))#65
9、print(ord('Z'))#90
"""


random_code = []  # 使用random_code列表存放生成的验证码

"""生成6位随机数(含字母数字)"""
for i in range(1,7):
    # 控制为6位长度,每循环一次生成一位随机数

    if i == random.randint(1, 6):
        # 如果random.randint()生成的随机数与循环次数相等
        random_code.append(str(random.randint(0, 9)))
        # 那么这位验证码为数字0-9的之间一位随机数

    else:
        # 如果random.randint()生成的随机数与循环次数不相等
        random_code.append(chr(random.randint(65, 90)))
        # 那么这位验证码为字母A-Z的之间一位字符

print(''.join(random_code))
# 把random_code列表拼接成字符串
