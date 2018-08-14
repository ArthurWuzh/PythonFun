豆瓣影评爬取及分析
### 影评爬取
影评爬取： 使用Scrapy框架进行爬取
#### 爬取一路好戏
终端路径切入到spiders文件夹<br>

```
爱情公寓及一出好戏影评\LoveApartmentMovieVersion\LoveApartmentMovieVersion\spiders
```

路径切换到data文件夹，运行以下命令，开始爬取：
```
scrapy crawl love_apartment_movie_version

```
结束后可以看到会生成一个json文件，打开json文件，在头加入“[”，在尾加入"]",形成列表，方便后面的处理

#### 爬取爱情公寓
1. 取消love_apartment_movie_version.py爱情公寓start_urls的注释,一路公寓的加上注释（要爬取那个就取消注释，不爬取的就注释掉，一次爬取一个）<br>
2. 切换到“爱情公寓及一出好戏影评\LoveApartmentMovieVersion\LoveApartmentMovieVersion\”，取消爱情公寓的注释，一路好戏加上注释
3. 路径切换到data文件夹，运行以下命令，开始爬取：
```
scrapy crawl love_apartment_movie_version

```
到这里两个电影的影评已爬取出来了。

### 影评分析
分析的py文件就在data文件夹的analysis.py文件，逐个运行就ok。