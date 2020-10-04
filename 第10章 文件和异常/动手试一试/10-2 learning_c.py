# 可使用replace()方法将字符串中的特定单词都替换为另一个单词
# 示例 message.replace(old_str, new_str)

file_name = '10-1 Python学习笔记\\learning_python.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    line = line.replace('Python', 'C').strip()
    print(line)