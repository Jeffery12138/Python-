# 4.5.1 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 不能给元组的元素赋值，修改元组的造作是被禁止的
# dimensions[0] = 250

# 4.5.2 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

# 4.5.3 修改元组变量
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
# 给元组变量赋值是合法的
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)