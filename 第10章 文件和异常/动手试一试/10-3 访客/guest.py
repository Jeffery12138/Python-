# 提示用户输入其名字
name = input("Enter your name please:")

file_name = 'guest.txt'
with open(file_name, 'a') as file_object:
    file_object.write(name+'\n')