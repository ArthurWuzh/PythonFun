"""使用Python支持获取字符的Unicode名称(\N{name})方式来打印中国的十二生肖图像"""
# 在Pycharm中可以顺利打印图像
# 蛇马羊猴鸡狗猪鼠牛虎兔龙  twelve Chinese horoscope animals
# 对应的英文名字：Snake Horse Sheep Monkey Chicken Dog Pig Mouse Ox Tiger Rabbit Dragon

# 把\N{name}的十二生肖名称放入到一个列表
twelve_Chinese_horoscope_animals = ['\N{Snake}', '\N{Horse}', '\N{Sheep}', '\N{Monkey}', '\N{Chicken}', '\N{Dog}',
                                    '\N{Pig}', '\N{Mouse}', '\N{Ox}', '\N{Tiger}', '\N{Rabbit}', '\N{Dragon}']

# 遍历列表打印十二生肖
for animal in twelve_Chinese_horoscope_animals:
    print(animal, end="  ")
