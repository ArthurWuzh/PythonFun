# -*- coding: utf-8 -*-
import re

import scrapy
from ..items import LoveapartmentmovieversionItem

class LoveApartmentMovieVersionSpider(scrapy.Spider):
    name = 'love_apartment_movie_version'
    allowed_domains = ['movie.douban.com']
    # start_urls = ['https://movie.douban.com/subject/24852545/comments?start=0&limit=20&sort=new_score&status=P'] # 爬取爱情公寓
    start_urls = ['https://movie.douban.com/subject/26985127/comments?start=0&limit=20&sort=new_score&status=P'] # 爬取一出好戏

    def parse(self, response):
        for each in response.xpath("//div[@class='comment']"):

            item = LoveapartmentmovieversionItem()
            item['name'] = each.xpath("./h3/span[@class='comment-info']/a/text()").extract_first()
            item['star'] = each.xpath("./h3/span[@class='comment-info']/span[2]/@title").extract_first()
            item['time'] = each.xpath("./h3/span[@class='comment-info']/span[3]/@title").extract_first()
            item['comment'] = each.xpath("./p/span/text()").extract_first()

            curpage = re.search('start=(\d+)', response.url).group(1)
            page = int(curpage) + 20
            url = re.sub('start=(\d+)', 'start='+str(page), response.url)

            yield scrapy.Request(url, callback=self.parse)
            yield item


