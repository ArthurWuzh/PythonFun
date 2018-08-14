# -*- coding: utf-8 -*-

import json


class LoveapartmentmovieversionPipeline(object):
    def __init__(self):
        # self.file = open('love.json','w') # 爬取爱情公寓影评就取消注释
        self.file = open('a_good_show.json','w') # 爬取一路好戏影评就取消注释

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ',\n'

        try:
            self.file.write(content)
        except Exception as e :
            raise Exception("error")
        return item

    def close_spider(self,spider):
        self.file.close()
