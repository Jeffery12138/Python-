# 10.1.5 使用文件的内容
# 创建一个字符串，它包含文件中存储的所有数字且没有任何空格：
# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
#     # 将文件的所有行都储存在一个列表中
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     # 在变量pi_string存储的字符串包含了原来位于左边的空格，rstrip()只删除了右边的空格
#     pi_string += line.rstrip()
# print(pi_string)
# print(len(pi_string))
#
# # 使用strip()去除所有空格
# file_name = 'pi_digits.txt'
# with open(file_name) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))

# note:
# 读取文本文件时，Python将其中的所有文本都解读为字符串。
# 如果你读取的是数字，并要将其作为数值使用，就必须使用函数int()将其转换为整数，
# 或使用函数float()将其转换为浮点数

# # 10.1.6 包含一百万位的大型文件
# file_name = 'pi_million_digits.txt'
# with open(file_name) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# # print(pi_string)
# print(pi_string[:52] + "...")
# print(len(pi_string))

# 10.1.7 圆周率值中包含你的生日吗
file_name = 'pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")