# zc-cris

import matplotlib.pyplot as plt

'''绘制最简单的折线图'''

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 设置输入和输出的数据，寻找他们之间的关系，顺手设置线条的宽度
plt.plot(input_value, squares, linewidth=5)

# 设置标题或者x，y项主题的内容以及文字大小
plt.title('caculate square', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('square of value', fontsize=14)

# 设置刻度标签的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
