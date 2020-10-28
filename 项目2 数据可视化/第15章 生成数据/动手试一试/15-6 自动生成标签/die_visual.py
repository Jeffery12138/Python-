import pygal


# 15.4.4 掷骰子
from die import Die

# 创建一个D6
die = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = [die.roll() for roll_num in range(1000)]
# 15.4.5 分析结果
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
# 15.4.6 绘制直方图
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(value) for value in range(1, die.num_sides+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')