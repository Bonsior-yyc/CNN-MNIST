import time
import matplotlib.pyplot as plt


class Progress_bar(object):
    def __init__(self):
        self.start = time.perf_counter()
        self.last_update = time.perf_counter()

    def bar(self, index, length, script, batch=1):
        index = index * batch
        if length - index < batch:
            index = length-1
        percentage = (index+1) / length
        progress = list('..........................')
        progress[(index+1) * 25//length] = '>'
        progress[:(index+1) * 25//length] = '=' * ((index+1) * 25//length + 1)
        progress = ''.join(progress)
        end_time = time.perf_counter()
        print("\r{}: {}  time left:{:.2f}s {}/{}  {:.2f} {} time cost:{:.2f}s "
              .format(script,
                      progress,
                      (end_time - self.start) / percentage * (1 - percentage),
                      (index+1), length, percentage * 100, "%", end_time - self.start), end='')
        self.last_update = time.perf_counter()


def show_image(array, rows=1, cols=1):
    # 判断是否有多张图
    if rows * cols == 1:
        plt.figure()
        plt.imshow(array, cmap='gray')
        plt.show()
    else:
        # 打印到一张图
        for row in range(rows):
            for col in range(cols):
                index = row * cols + col
                plt.subplot(rows, cols, index + 1)
                plt.imshow(array[index], cmap="gray", interpolation="nearest")
                plt.axis('off')
        plt.show()


