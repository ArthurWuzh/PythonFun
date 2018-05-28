import pygame


def play():
    """播放背景音乐"""

    # 初始化
    pygame.mixer.init()

    # 加载音乐
    pygame.mixer.music.load("./music/with_you_all_the_time.mp3")

    # 循环播放，检查音乐流是否一在用，有返回Ture，没返回False.False
    while True:
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()


if __name__ == "__main__":
    play()
