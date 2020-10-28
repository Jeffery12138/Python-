# 16.1.1 分析CSV文件头
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期和最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # 16.1.2 打印文件头及其位置
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 16.1.3 提取并读取数据
    dates, highs = [], []
    for row in reader:
        # 16.1.6 在图表中添加日期
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    # print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()