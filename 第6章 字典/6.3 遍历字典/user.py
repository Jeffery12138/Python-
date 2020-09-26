# 6.3.1 遍历所有的键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
# 申明两个变量key/value（可使用任何名称k/v）存储键值对中的键和值
# 字典的items()方法返回一个键值对列表class:dict_items
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
