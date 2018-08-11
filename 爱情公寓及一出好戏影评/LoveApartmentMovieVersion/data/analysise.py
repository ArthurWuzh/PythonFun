import json

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import io

myfont = matplotlib.font_manager.FontProperties(fname="DroidSansFallbackFull.ttf")
love_data = json.load(open('love.json'))
a_good_show_data = json.load(open('a_good_show.json'))

level_list = ['很差','较差','还行','推荐','力荐']
level_list_axios = ['OneStar','TwoStar','ThreeStar','FourStar','FiveStar']

# 统计各个星星等级的个数
def count_star(data,level_list):

    star_count = {}
    for i in data:
        if i['star'] in level_list:
            star_count[i['star']] = (star_count[i['star']] + 1) if star_count.get(i['star']) else 1
    return [star_count[level_list[0]], star_count[level_list[1]], star_count[level_list[2]],star_count[level_list[3]],star_count[level_list[4]]]

# 绘制饼图
def draw_pipe(name,star_count,level_list_axios):
    explode = (0.1, 0, 0, 0, 0)  # 0.1表示将Hogs那一块凸显出来
    plt.pie(star_count, explode=explode, labels=level_list_axios, autopct='%1.1f%%', shadow=False,startangle=90)  # startangle表示饼图的起始角度
    plt.axis('equal')
    plt.show()
    plt.savefig(name + '_pipe.png')


# 绘制柱状图
def draw_bar(name, star_count,level_list_axios):
    x = np.arange(5)
    width = 0.3
    ax = plt.subplot(1,1,1)
    ax.bar(x, star_count, width, color='b')
    ax.set_xticks(x+width)
    ax.set_xticklabels(level_list_axios)
    plt.show()
    plt.savefig(name + '_pipe.png')


# 绘制词云图片

# 准备词汇
def parse_signature(data):
    comment_list = []
    for i in data:
        comment = i['comment']
        print(comment)
        comment.replace('，',' ').replace('。',' ').replace('？',' ').replace('？',' ').replace('……',' ').replace('！',' ').replace('~',' ').replace('“',' ').replace('”',' ').replace('#',' ').replace('《',' ').replace('》',' ')
        comment_list.append(comment)

    text = " ".join(comment_list)
    with io.open('text.txt', 'w', encoding='utf-8') as f:
        wordlist = jieba.cut(text, cut_all=True)
        word_space_split = " ".join(wordlist)
        f.write(word_space_split)
        # f.write(text)
        f.close()



# 绘制词云
def draw_comment(name):
    text = open('text.txt', encoding='utf-8').read()
    coloring = np.array(Image.open('model2.png')) # 爱情公寓
    # coloring = np.array(Image.open('a_good_show.png')) # 一出好戏
    movie_wordcloud = WordCloud(background_color="gray", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,font_path="DroidSansFallbackFull.ttf").generate(text)
    image_colors = ImageColorGenerator(coloring)
    plt.imshow(movie_wordcloud.recolor(color_func=image_colors))
    plt.imshow(movie_wordcloud)
    plt.axis("off")
    plt.show()
    plt.savefig(name + '.png')



if __name__ == '__main__':
    # 首先绘制爱情公寓
    # love_count_star = count_star(love_data,level_list)
    # draw_pipe('love', love_count_star, level_list_axios)
    # draw_bar('love', love_count_star, level_list_axios)
    # parse_signature(love_data)
    # draw_comment('love_word_cloud')


    # 绘制一出好戏
    # a_good_show_count_star = count_star(a_good_show_data, level_list)
    # draw_pipe('a_good_show', a_good_show_count_star, level_list_axios)
    # draw_bar('a_good_show', a_good_show_count_star, level_list_axios)
    parse_signature(a_good_show_data)
    draw_comment('a_good_show_word_cloud')