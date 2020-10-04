file_name = 'learning_python.txt'
with open(file_name) as file_object:
    # 第一次打印，读取整个文件
    content = file_object.read()
    print(content)

# 第一次with open()打印之后文件自动关闭，若要第二次打印，必须再开一次
with open(file_name) as file_object:
    # 第二次打印，遍历文件对象
    for line in file_object:
        print(line)

# 第三次打印将各行存储在一个列表中，再在with代码块外打印它们
with open(file_name) as file_object:
    lines = file_object.readlines()

# 第三次打印
print(lines)
for i in range(len(lines)):
    lines[i] = lines[i].strip()
print(lines)
for line in lines:
    print(line)