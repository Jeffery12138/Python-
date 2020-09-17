motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# 修改列表中的元素
# motorcycles[0] = 'ducati'
# 1.在列表末尾添加元素
# motorcycles.append('ducati')
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# 2.在列表中插入元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# 这种操作将列表中既有的元素都右移一个位置

# 3.使用del语句删除元素
# del motorcycles[0]
# del可删除任何位置处的列表元素，条件是知道其索引。
# del motorcycles[1]

# 4.使用方法pop()删除元素--弹出
# popped_motorcycles = motorcycles.pop()
# print(popped_motorcycles)
# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a " + last_owned.title() + ".")

# 5.弹出列表中任何位置处的元素
# first_owned = motorcycles.pop(0)
# print("The first motorcycle I owned was a " + first_owned.title() + ".")
# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del语句；
# 如果你要在删除元素后还能继续使用它，就使用方法pop()

# 6.根据值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print(motorcycles)