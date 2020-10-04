# 10.1.1 读取整个文件

# 关键字with在不再需要访问文件后将其关闭。
# with open('pi_digits.txt') as file_object:
#     content = file_object.read()
#     # read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。
#     # print(content)
#     # 删除末尾的空行，可在print语句中使用rstrip()：
#     print(content.rstrip())

# 10.1.2文件路径
# 通过使用绝对路径，可读取系统任何地方的文件。
# 就目前而言，最简单的做法是，
# 要么将数据文件存储在程序文件所在的目录，
# 要么将其存储在程序文件所在目录下的一个文件夹中。

# 10.1.3 逐行读取
# 要以每次一行的方式检查文件，可对文件对象使用for循环：
# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         # print(line)
#         # 消除多余的空白行
#         print(line.rstrip())

# 10.1.4 创建一个包含文件各行内容的列表
# 使用关键字with时，open()返回的文件对象只在with代码块内可用。
# 如果要在with代码块外访问文件的内容，
# 可在with代码块内将文件的各行存储在一个列表中，
# 并在with代码块外使用该列表：你可以立即处理文件的各个部分，
# 也可推迟到程序后面再处理。
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    # readlines()从文件中读取每一行，并将其存储在一个列表中；
    lines = file_object.readlines()
    # print(lines)
for line in lines:
    print(line.rstrip())