# zc-cris
import pygal

from dice import Dice

dice = Dice()
dice2 = Dice()

numbers = []
while len(numbers) < 5000:
    n1 = dice.play()
    n2 = dice2.play()
    numbers.append(n1 + n2)

frenquence = []
for i in range(2, dice2.dice_num * 2 + 1):
    num = numbers.count(i)
    frenquence.append(num)

hist = pygal.Bar()
hist.title = 'Results of rolling two D6 5000 times'

hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'value'
hist.y_title = 'frequency of value'

hist.add('2 D6', frenquence)
hist.render_to_file('dice2_visual.svg')
