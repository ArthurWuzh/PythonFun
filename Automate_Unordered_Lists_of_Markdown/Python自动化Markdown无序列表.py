#！/usr/bin/env python3
# coding=utf-8
__author__ = "RidingRoad"

import pyperclip

def main():
    """运行前把需要形成无序列表的数据选中右击复制
       运行后右击粘贴即可生成Mark down格式无序列表
    """
    # 获取剪贴板的数据
    text = pyperclip.paste()
    # 对长字符串根据"\n"进行分割到一个列表
    text_split = text.split('\n')
    # 在每一行前添加"* "(*号和一个空格)
    for i in range(len(text_split)):
        text_split[i] = "* " + text_split[i]
    # 合并
    text = "\n".join(text_split)
    # 把处理后的数据放回剪贴板
    pyperclip.copy(text)


if __name__ == "__main__":
    main()