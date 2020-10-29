from matplotlib import pyplot as plt
from temperature import Temperature

# 从文件中获取日期、最高气温和最低气温
filename_s = 'sitka_weather_2014.csv'
filename_d = 'death_valley_2014.csv'

# 实例化气温数据类
temper_s = Temperature(filename_s)
temper_d = Temperature(filename_d)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(temper_s.dates, temper_s.highs, c='red', alpha=0.5)
plt.plot(temper_s.dates, temper_s.lows, c='blue', alpha=0.5)
plt.fill_between(temper_s.dates, temper_s.highs, temper_s.lows, facecolor='blue', alpha=0.1)

plt.plot(temper_d.dates, temper_d.highs, c='red', alpha=0.5)
plt.plot(temper_d.dates, temper_d.lows, c='green', alpha=0.5)
plt.fill_between(temper_d.dates, temper_d.highs, temper_d.lows, facecolor='green', alpha=0.1)

# 设置图形的格式
title = "Daily high and low temperatures - 2014\nSitka and Death Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(0, 120)


plt.show()
