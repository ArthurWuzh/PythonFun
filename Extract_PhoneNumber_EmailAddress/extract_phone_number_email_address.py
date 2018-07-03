#! usr/bin/env python3
# coding=utf-8
__author__ = "RidingRoad 公众号 Python孙行者"
import re, pyperclip


def extract_phone_email():
    '''
    从电脑剪贴板提取电话和邮箱信息,并把匹配到的结果放回剪贴板,
    运行后,结果已保存到你电脑的剪贴板了,Ctrl + V 就可以了
    '''

    # 提取固话即分机号码的正则
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?          # 匹配区号,'?'表示区号可有可无
        (\s|-|\.)?                  # 分隔符 ,号码数字之间的分隔符 比如 020-333-3333,'?'表示分隔符可有可无
        (\d{3})                     # 号码中前面三个数字
        (\s|-|\.)                   # 分隔符
        (\d{4})                     # 最后的4个数字
        (\s*(ext|x|ext.)\s*(\d{2,5}))? # 获取分机号码
        )''', re.VERBOSE)  # re.VERBOSE 表示可以在正则表达式中写注释,正则中注释也是以'#'开头


    # 提取邮箱的正则
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9.%+-]+        # 邮箱的用户名
        @                       # @标志
        [a-zA-Z0-9.-]+          # 域名
        (\.[a-zA-Z]{2,4})       # 顶级域名
        )''', re.VERBOSE)

    text = str(pyperclip.paste())  # 获取剪贴板的信息存到变量text中
    matches = []  # 匹配成功的邮箱和电话存放到matches列表中

    for groups in phoneRegex.findall(text):  # 遍历匹配到的电话列表
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])  # 统一格式 020-333-3333
        if groups[8] != '':  # 如果有分机,则把分机号码也提取出来
            phoneNum += 'x' + groups[8]
        matches.append(phoneNum)

    for groups in emailRegex.findall(text):  # 遍历匹配到的邮箱
        matches.append(groups[0])

    if len(matches) > 0:  # 判断文本中是否存在电话邮箱地址
        pyperclip.copy("\n".join(matches))  # 把匹配结果存放到剪贴板中
        # print('Copied to clipboard:')
        # print('\n'.join(matches))
    else:
        print("文本中不存在邮箱或电话")


if __name__ == "__main__":
    """运行后,结果已保存到你电脑的剪贴板了,Ctrl + V 就可以了"""
    extract_phone_email()





