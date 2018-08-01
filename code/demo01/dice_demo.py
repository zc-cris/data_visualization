# zc-cris
import pygal

from dice import Dice

dice = Dice()
numbers = []

while len(numbers) < 5000:
    play = dice.play()
    numbers.append(play)

# 将每个点数出现的次数统计起来
results = []
for i in range(1, dice.dice_num + 1):
    count = numbers.count(i)
    results.append(count)

# 绘制直方图（pygal）
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 5000 times'
# 横坐标的值必须和results里面的值的顺序一一对应
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frenquency of Result'

hist.add('D6', results)
hist.render_to_file('dice_visual.svg')
