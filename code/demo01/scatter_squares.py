# zc-cris

import matplotlib.pyplot as plt
'''渐变色散点图'''
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

x_values = list(range(1000))
y_values = [x ** 2 for x in x_values]
# 绘制散点图(可去掉点的轮廓以及指定点的颜色，大小)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=30)

# 设置x，y轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 自动保存图表(指定保存位置，bbox_inches 最好设置为tight)
plt.savefig('../../pictures/square_numbers.png', bbox_inches='tight')
# 显示图表
plt.show()
