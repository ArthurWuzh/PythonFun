#! usr/bin/env python3
# coding=utf-8
__author__ = "RidingRoad 公众号 Python孙行者"

import re

def strong_password_detection(password):
    """
    强口令:长度不少于8个字符,同时包含大小写字母,至少有一位数字
    :param password: 待检测强度的密码
    :return: 如果满足强度要求,返回True,否则返回False
    """
    # 解决思路:
    # 1.使用len() 检测密码的长度
    # 2.使用一个正则检测是否有至少一位数字
    # 3.使用一个正则检测是否有大写字母
    # 4.使用一个正则检测是否有小写字母
    # 5.上面四个条件都为真的话,就返回True,否则返回False

    length_flag = False # 长度标志
    digit_flag = False  # 数字标志
    upper_flag = False  # 大写标志
    lower_flag = False  # 小写标志

    # 匹配数字的正则
    digit_regex = re.compile(r'\d')
    # 匹配大写字母的正则
    upper_regex = re.compile(r'[A-Z]')
    # 匹配小写字母的正则
    lower_regex = re.compile(r'[a-z]')

    if len(password) >= 8: # 判断长度
        length_flag = True

    if len(digit_regex.findall(password)) >= 1: # 判断是否包含至少一位数字
        digit_flag = True

    if len(upper_regex.findall(password)) > 0: # 判断是否包含大写字母
        upper_flag = True

    if len(lower_regex.findall(password)) > 0: # 判断是否包含小写字母
        lower_flag = True

    if length_flag and digit_flag and upper_flag and lower_flag: # 判断是否同时满足4个条件
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        password = input("请输入待检测密码强度的字符串:")
        if strong_password_detection(password):
            print("密码符合强度要求")
            break
        else:
            print("密码强度不足,请重新输入")



