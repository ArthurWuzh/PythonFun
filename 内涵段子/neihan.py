import re, requests, time, sys

MAX_PAGES = 10  # 设置爬取的页数


class Neihan(object):
    def __init__(self):
        # 动态url
        self.url = 'https://www.neihan8.com/article/list_5_{}.html'
        # 构造请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
        }
        # 标题和内容的正则匹配模式
        self.regex = re.compile(
            r'''<a href="/article/\d+\.html">(.*?)</a>.*?<div class="f18 mb20">(.*?)</div>''', re.S)
        # result_list 用于存放已解析清洗好的段子数据
        self.result_list = list()

    # 请求某一具体页面数据
    def request(self, url, index):
        print('url:', url)
        # 设置时间间隔， 以免对目标网站造成太大压力
        time.sleep(0.5)
        # 为了规避反爬，爬取的不是第一页需带上Referer请求头信息
        if index != 1:
            # 动态生成url
            self.headers['Referer'] = 'https: // www.neihan8.com / article / list_5_{}.html'.format(index - 1)
        # 获取响应数据
        response = requests.get(url, headers=self.headers)
        # 此网站使用GBK编码，对返回的数据进行相应解码
        return response.content.decode('gbk')

    # 获取一个页面的所有段子原始数据，存放在data_list
    def get_data(self, index):
        data_list = self.regex.findall(self.request(self.url.format(index), index))
        # 如果返回的数据为空，说明网站上的段子都爬完了，退出程序
        if data_list == []:
            sys.exit(0)
        return data_list

    # 对数据进行提取清洗
    def parse_data_list(self, index):
        # result_list存放已解析清洗好的段子数据
        self.result_list = []
        # 获取到的段子列表数据放到duanzi
        duanzi = self.get_data(index)
        # 对段子列表数据duanzi每一个段子去掉空格和其他字符，保留换行
        for item in duanzi:
            result = re.sub(r'[<b>|</b>|<br />|<br>|<p>|</p>|\\u3000|\\r|\s|t|div|sa]', "", str(item))
            result = result.replace('&ldqo;', '“').replace('&dqo;', '”').replace('&helli;', '...').replace('&lqo;',
                                                                                                           '“').replace(
                '&qo;', '”').replace('&hell;', '...').replace('n', '\\n').replace('&zwj;', '').replace('&qot;',
                                                                                                       '"').replace(
                '&mh;', '').strip(' ')
            result = re.sub(r'yle.*?(?:x;|\)|;|\n|x)"', '', result)
            result = re.sub(r'hef.*?ml"', '', result)
            result = re.sub(r"cl=.*?(?:we'|\d+\")", '', result)
            result = re.sub(r'c=.*?\.jg"', '', result)

            # 把清洗好的数据添加到result_list
            self.result_list.append(eval(result))
        return self.result_list

    # 每一页数据保存为一个单独的Markdowm文档
    def save_md(self, index):
        duanzi_list = self.parse_data_list(index)
        file = open('内涵段子{}.md'.format(index), 'w')
        for item in duanzi_list:
            # 拼接成Markdown格式
            file.write('### ' + item[0] + item[1])
        # 关闭文件
        file.close()


if __name__ == '__main__':
    # 创建内涵段子实例对象
    neihan = Neihan()
    # 默认从第一页开始爬取
    index = 1
    # 这里也可以设置爬取的页数
    # while index <= MAX_PAGES:
    # 这里是爬取所有的段子
    while True:
        neihan.save_md(index)
        index += 1
