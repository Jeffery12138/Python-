# 保存数据最简单的方式之一是将其写入到文件中.
# 通过将输出写入文件,即便关闭包含程序输出的终端窗口,这些输出也依然存在:
# 1.可以在程序结束运行后查看这些输出
# 2.可与别人分享输出文件
# 3.还可编写程序来将这些输出读取到内存中并进行处理

# 10.2.1 写入空文件
# 要将文本写入文件，在调用open()时需要提供另一个实参'w'，代表以写入模式打开文本
# 打开文件时可以指定模式：
# 'r'读取模式；'w'写入模式；'a'附加模式；'r+'读取和写入的模式；'b'二进制模式
# 如果省略模式实参，默认只读模式打开文件
# file_name = 'programming.txt'
# with open(file_name, 'w') as file_object:
#     file_object.write("I love programming.")

# note：
# Python 只能将字符串写入文本，要将数值数据存储到文本文件中，
# 必须先使用函数str()将其转换为字符串格式

# 10.2.2 写入多行
# 函数write()不会再写入文本末尾添加换行符
# file_name = 'programming.txt'
# with open(file_name, 'w') as file_object:
#     # 如下两行内容挤在了一起
#     file_object.write('I love programing.')
#     file_object.write("I love creating new games.")

# 要让字符串都单独占一行，需要在write()语句中包含换行符：
# 像显示到终端的输出一样，还可以使用空格，制表符和空行来设置
# 这些输出格式
# file_name = 'programming.txt'
# with open(file_name, 'w') as file_object:
#     file_object.write('I love programming.\n')
#     file_object.write('I love creating new games.\n')

# 10.2.3 附加到文件
file_name = "programming.txt"
# 以附加模式打开文件，将内容附加到文件末尾，而不是覆盖文件原来的内容
# 如果文件不存在，则会新建
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
