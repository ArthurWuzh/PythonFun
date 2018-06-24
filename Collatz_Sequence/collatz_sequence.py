#!/usr/bin/env python3
# coding=utf-8
__author__ = "RidingRoad"

START_NUMBER = 1
END_NUMBER = 1000000


def collatz_seq(number):
    """
    获取到的number是奇数,则number=  3 * number + 1;
    偶数则number=  number // 2;
    如果考拉咨猜想真的成立,可以number=1,那么程序将会停止,否则,考拉咨猜想不成立
    :return:1
    """
    while True:
        if number == 1:
            return number
        else:
            # number为偶数
            if not number % 2:
                number = number // 2
            else:
                # number为奇数
                number = 3 * number + 1

def verify(num):
    """判断结果里的不是1的数"""
    return 1 != num

def main():
    # 存放验证考拉咨猜想函数的结果
    result = []
    for i in range(START_NUMBER, END_NUMBER):
        # 验证START_NUMBER, END_NUMBER之间的数
        result.append(collatz_seq(i))
    # 使用filter对结果进行判断是否存在非1的数
    print(list(filter(verify, result)))
    """
        filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of iterable for which function(item)
        is true. If function is None, return the items that are true.
    """


if __name__ == "__main__":
    main()



