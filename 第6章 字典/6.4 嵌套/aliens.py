# 6.4.1 字典列表
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# 自动生成30个外星人
# 创建一个用于存储外星人的空列表
# aliens = []
# 创建30个绿色的外星人
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# # 显示前5个外星人
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # 显示创建了多少个外星人
# print("Total number of aliens: " + str(len(aliens)))

# 将前三个外星人修改为黄色的、速度为中等其值10个点
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 将前三个外星人修改为黄色的、速度为中等其值10个点
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    # 将黄色外星人改为移动速度快且值15个点的红色外星人
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))