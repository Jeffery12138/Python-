# 10.4.1 使用json.dump()和json.load()
# 函数json.dump()接受两个实参：
# 要存储的数据
# 以及可用于存储数据的文件对象。

# 导入模块json
import json
# 创建一个数字列表
numbers = [2, 3, 5, 7, 11, 13]
# 指定要将该数字列表存储到其中的文件的名称
# 通常使用文件扩展名.json来指出文件存储的数据为JSON格式。
filename = 'numbers.json'
# 已写入模式'w'打开这个文件
with open(filename, 'w') as f_obj:
    # 使用函数json.dump()将数字列表存储到文件numbers.json中。
    json.dump(numbers, f_obj)