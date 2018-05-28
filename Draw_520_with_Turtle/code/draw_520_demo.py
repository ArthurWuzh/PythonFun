import multiprocessing
import draw_5, draw_2, draw_0, draw_RR, draw_CY, play_music


def draw_main():
    """绘制图案"""
    draw_5.draw()
    draw_2.draw()
    draw_0.draw()
    draw_RR.draw()
    draw_CY.draw()


def main():
    """绘制520图案和播放背景音乐"""

    # 播放音乐
    play_process = multiprocessing.Process(target=play_music.play)
    # 绘制图案
    draw_process = multiprocessing.Process(target=draw_main)

    play_process.start()
    draw_process.start()


if __name__ == "__main__":
    main()
