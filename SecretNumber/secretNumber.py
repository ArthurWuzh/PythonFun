# 随机模块
import random


# 定义猜数字函数
def guessNumber():
    """这是一个猜数字游戏,6次机会"""
    # 使用随机函数生成一个随机整数并保存在变量secretNumber
    secretNumber = random.randint(1, 20)
    print('小可爱:我心里有个1到20的幸运数字')
    # 计数器
    guessesTaken = 0
    # guess用来保存玩家的数字
    guess = None
    # 使用range(1,7)控制循环6次,range(start,end,step)左闭右开
    for guessesTaken in range(1, 7):
        # Ask the player to guess 6 times.
        print('小可爱:猜猜(比心)')
        # 玩家输入数字
        guess = int(input("么么哒:"))
        # 计数器加一
        guessesTaken += 1
        if guess < secretNumber:
            print('小可爱:小了耶,傻瓜')
        elif guess > secretNumber:
            print('小可爱:大了哦,笨蛋')
        else:
            break  # 不大不小那就是对了,不用继续猜了,退出循环

    if guess == secretNumber:
        print('么么哒:心有灵犀哦,你只用' + str(guessesTaken) + '次就猜到我的心思')
    else:
        print('死鬼,哎,我的幸运数字是 ' + str(secretNumber))

if __name__ == "__main__":
    guessNumber()
