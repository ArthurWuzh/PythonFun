"""
本软件主要功能：
1. 实现对剪贴板的信息进行判断是否存在于某个文件中
2. 比如，有一份公司名单，判断招聘网站的公司是否在名单中
3. 通过运行本软件，点击“开始运行”，然后复制招聘网站的公司名，程序会自动判断是否存在于文件中
4. 使用pyinstaller进行打包成exe文件
"""
__author__ = "RidingRoad 公号：Python孙行者"

import time, re, threading

import pyperclip, tkinter, tkinter.messagebox

# 数据存放到列表里
company_list = []
with open('outsource_company.txt', 'rb') as f:
    while True:
        company = f.readline().decode().strip()
        if company is '':
            break
        else:
            company_list.append(company)


# 获取剪贴板信息
def get_data():
    # 公司名称
    company_name = pyperclip.paste()
    pyperclip.copy('')
    return company_name


# 判断是否在列表里
def is_exists(company_data, company_list):
    pattern = re.compile(company_data)
    # 遍历列表
    for company in company_list:
        try:
            result = pattern.search(company).group(0)
            if company_data in company:
                return True
        except:
            pass
    return False


# 弹窗显示信息
def show_result(result=False, in_message='：为外包公司，仅供参考', not_in_message='：没有收录在外包公司库，仅供参考'):
    global is_start
    global company_name
    while is_start:
        time.sleep(0.01)
        company_name = get_data()
        if not company_name == '':
            result = is_exists(company_name, company_list)
            # 在列表里
            if result:
                tkinter.messagebox.showwarning(title='查询结果', message='%s%s' % (company_name, in_message))
            else:
                tkinter.messagebox.showinfo(title='查询结果', message='%s%s' % (company_name, not_in_message))


def start():
    global is_start
    is_start = True
    thread = threading.Thread(target=show_result)
    thread.start()


def stop():
    global is_start
    is_start = False


if __name__ == '__main__':
    tk = tkinter.Tk()
    tk.geometry('280x30')
    global x, y, is_start
    tk.title('外包公司查询控制台')
    start = tkinter.Button(tk, text='开始运行', command=start, width=18, bg='#008B00')
    stop = tkinter.Button(tk, text='暂停运行', command=stop, width=20, bg='#FF6347')
    start.pack(side=tkinter.LEFT)
    stop.pack(side=tkinter.RIGHT)
    tkinter.messagebox.showinfo(title='软件使用温馨提示(公众号：Python孙行者)',
                                   message='点击“开始运行”即可\n每次复制，程序都会对复制的内容进行判断\n每次查询后会清空剪贴板内容\n若不需要查询请点击暂停运行，以免数据丢失!!!\n可以自定义丰富更新“outsource_company.txt”公司名单\n数据有限，仅供参考')
    tk.mainloop()

# pyinstaller -F -w --version-file=file_version_info.txt  check_outsource_company.py