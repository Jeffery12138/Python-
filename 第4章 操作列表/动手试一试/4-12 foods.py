my_foods = ['pizza', 'falafel', 'carrot cake']
# # 使用切片复制，生成两个列表
friend_foods = my_foods[:]
# 不使用切片复制，两个变量名my_foods和friend_foods对应一个列表
# friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)
print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)