# 10.3.5 处理FileNotFoundError异常
# 使用文件时，一种常见的问题是找不到文件：
# 你要查找的文件可能在其他地方、
# 文件名可能不正确或者这个文件根本就不存在。
# 对于所有这些情形，都可使用try-except代码块以直观的方式进行处理。
# file_name = 'alice.txt'
# with open(file_name) as f_obj:
#     contents = f_obj.read()

# Python无法读取不存在的文件，因此它引发一个异常
# 在这个示例中，这个错误是函数open()导致的，
# 因此要处理这个错误，必须将try语句放在包含open()的代码行之前：
# file_name = 'alice.txt'
# try:
#     with open(file_name) as f_obj:
#         content = f_obj.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + file_name + " does not exist."
#     print(msg)

# 10.3.6 分析文本
file_name = 'alice.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " does not exist."
    print(msg)
# 仅当try代码块成功成功执行时才执行else代码块。
else:
    # 计算文件大致包含多少单词
    # 方法split()以空格为分隔符将字符串分拆成多个部分，
    # 并将这些部分都存储到一个列表中
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")
