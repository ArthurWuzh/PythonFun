import multiprocessing,threading,gevent,time
from gevent import monkey
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
    #进程版
    # 播放音乐
    play_process = multiprocessing.Process(target=play_music.play)
    # 绘制图案
    draw_process = multiprocessing.Process(target=draw_main)

    play_process.start()
    draw_process.start()

    #线程版,因为是音乐播放和绘图是交换进行的,会显得绘图很缓慢,体会一下龟速
    # play_music_thread = threading.Thread(target=play_music.play)
    # draw_thread = threading.Thread(target=draw_main)
    #
    # play_music_thread.start()
    # draw_thread.start()

    #协程版不行,需要时间阻塞才能有作用,由于本项目的两个任务都没有时间阻塞,所以用不了
    # monkey.patch_all()
    # play_music_gevent = gevent.spawn(play_music.play)
    # draw_gevent = gevent.spawn(draw_main)
    #
    # play_music_gevent.join()
    # time.sleep(0.00000000001)
    # draw_gevent.join()


if __name__ == "__main__":
    main()
