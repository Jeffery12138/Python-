cars = ['bmw', 'audi', 'toyota', 'subaru']
# 方法sort()永久性地修改了列表元素的排列顺序
# cars.sort()

# sort()方法传递参数reverse=True按字母顺序相反的顺序排列列表元素，永久性地改变列表
# cars.sort(reverse=True)

# 使用sorted()函数对列表进行临时排序（将可迭代对象作为参数传入sorted()函数）
# print("Here is original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")

# reverse()反转列表的元素的排列顺序，可随时恢复到原来的排列顺序（再次调用reverse()即可）
# print(cars)
# cars.reverse()

# 使用len()函数确认列表的长度
print(len(cars))
print(cars)