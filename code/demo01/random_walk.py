# zc-cris

from random import choice


class RandomWalk():
    def __init__(self, count=50000):
        # 初始化随机漫步的总次数
        self.count = count

        # 初始化随机漫步的点的x，y轴坐标
        self.x_values = [0]
        self.y_values = [0]

    def walk(self):
        '''生成对应的5000个随机坐标的点, 注意是< 不是《='''
        while len(self.x_values) < self.count:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])

            x_length = x_direction * x_distance
            y_length = y_direction * y_distance

            if x_length == 0 and y_length == 0:
                continue

            # 计算下一个点的位置
            next_x = self.x_values[-1] + x_length
            next_y = self.y_values[-1] + y_length
            self.x_values.append(next_x)
            self.y_values.append(next_y)
