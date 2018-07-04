#! usr/bin/env python3
# coding=utf-8
__author__ = "RidingRoad 公众号 Python孙行者"

import re

"""
写一个函数，它接收一个字符串，做的事情和 strip()字符串方法一样。如果只
传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。否
则，函数第二个参数指定的字符将从该字符串中去除
"""
# 解题思路
# 1.如果只有一个参数,那么删除两端的空白
  # 通过分组的形式,分离两端空白部分和需要保留的部分
  # r'(\s*)(.+\w)(\s*)'
# 2.如果有两个参数,那么删除指定字符,使用re.sub进行替换即可
def strip_regex_version(string_data,delete=None):
    if delete == None:
        # 删除两侧空白
        string_data_regex = re.compile(r'(\s*)(.+\w)(\s*)') # 分组提取需要保留的部分
        result = string_data_regex.match(string_data).group(2)
    else:
        # 删除指定的字符
        result = re.sub(delete,'',string_data)
    return result


if __name__ == "__main__":
    while True:
        string_data = input("请输入原始字符串:")
        option = input("是否需要删除字符(y/n):")
        if option.lower() == 'y':
            while True:
                delete = input("请输入需要删除的字符:")
                if delete not in string_data:
                    print("您要删除的字符不存在,请重新输入")
                    delete = None
                    continue # 跳出本次循环,继续下一次的输入
                else:
                    break # 结束整个循环体
        else:
            delete = None

        print("正则版strip()效果:",strip_regex_version(string_data,delete))
        break  # 结束循环




