# zc-cris

from matplotlib import pyplot as plt

from random_walk import RandomWalk

random_walk = RandomWalk()
random_walk.walk()

plt.title("Random Walk", fontsize=24)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
# 绘制散点图
plt.scatter(random_walk.x_values, random_walk.y_values, c=[i for i in range(random_walk.count)], cmap=plt.cm.Blues, edgecolors='none', s=5)
# 突出起点和终点
plt.scatter(0,0, c='red', s=50)
plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red', s=50)
# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
