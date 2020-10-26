import matplotlib.pyplot as plt

# 15.2.3 使用scatter()绘制散点图并设置其样式
# plt.scatter(2, 4)
# plt.show()

# 设置输出样式、标题、标签
# plt.scatter(2, 4, s=200)
# # 设置图表标题并给坐标加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

# 15.2.4 使用scatter()绘制一系列点
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)
# # 设置图表标题并给坐标加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()

# # 15.2.5 自动计算数据
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# # plt.scatter(x_values, y_values, s=40)
# # 15.2.6 删除数据点的轮廓
# # plt.scatter(x_values, y_values, edgecolor='none', s=40)
# # 15.2.7 自定义颜色
# # plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# # 要指定自定义颜色，可传递参数c，并将其设置为一个元组，
# # 其中包含三个0～1之间的小数值，它们分别表示红色、绿色和蓝色分量。
# # 值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
# # 设置图表标题并给坐标加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# # 设置刻度标记的大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# # 设置每个坐标轴的取值范围
# plt.axis([0, 1100, 0, 1100000])
# plt.show()

# 15.2.8 使用颜色映射
# 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。
# 在可视化中，颜色映射用于突出数据的规律
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
# plt.show()
# 15.2.9 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')
# 要让程序自动将图表保存到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用：
# 第一个实参指定要以什么样的文件名保存图表，
# 这个文件将存储到scatter_squares.py所在的目录中；
# 第二个实参指定将图表多余的空白区域裁剪掉。
# 如果要保留图表周围多余的空白区域，可省略这个实参。