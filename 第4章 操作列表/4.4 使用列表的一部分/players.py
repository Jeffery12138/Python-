# 4-4-1切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
# 提取列表索引为0/1/2的元素
print(players[0:3])
# 提取列表索引为1/2/3个元素
print(players[1:4])
# 没有指定第一个索引，自动从列表开头开始，索引0
print(players[:4])
# 提取第3个元素（索引为2）到列表末尾的所有元素
print(players[2:])
# 输出列表的最后3个元素
print(players[-3:])

# 4-4-2 遍历切片
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
