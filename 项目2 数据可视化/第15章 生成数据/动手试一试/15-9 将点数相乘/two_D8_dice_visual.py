import pygal

from die import Die

# 创建两个骰子
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存储在一个列表中
results = [die_1.roll()*die_2.roll() for roll_num in range(1000)]

# 分析结果
values = []
for i in range(1, die_1.num_sides+1):
    for j in range(i, die_2.num_sides+1):
        value = i * j
        values.append(value)
values = sorted(list(set(values)))
frequencies = []
for value in values:
    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [str(value) for value in values]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 * D6", frequencies)
hist.render_to_file("two_D6_dice.svg")