import matplotlib.pyplot as plt


def draw_cube_plot(n):
    """绘制图形，显示前n个整数的立方值"""
    x_values = list(range(1, n+1))
    y_values = [x**3 for x in x_values]
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
    # 设置图表标题并给坐标轴加上标签
    plt.title("Cubic Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Cube of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置每个坐标轴的取值范围
    plt.axis([0, int(1.2*n), 0, int(1.2*(n**3))])
    plt.show()


draw_cube_plot(5)
draw_cube_plot(5000)