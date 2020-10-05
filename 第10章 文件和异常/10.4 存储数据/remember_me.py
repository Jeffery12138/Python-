# 10.4.2 保存和读取用户生成的数据
# import json
# username = input("What is your name?")
#
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when you come back, " + username + "!")

# 将两个程序合并到一个程序中
import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
file_name = 'username.json'

try:
    with open(file_name) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name?")
    with open(file_name, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")