# 4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
# # 使用切片复制，生成两个列表
# friend_food = my_foods[:]
# 不使用切片复制，两个变量名my_foods和friend_foods对应一个列表
friend_food = my_foods
my_foods.append('cannoli')
friend_food.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_food)
