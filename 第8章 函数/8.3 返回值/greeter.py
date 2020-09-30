# 8.3.4 结合使用函数和while循环
# 以更正规的方式问候用户
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name+" "+last_name
    return full_name.title()
# 这是一个无限循环


# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     l_name = input("Last name:")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, "+formatted_name+"!")

# 我们要让用户能够尽可能容易地退出，
# 因此每次提示用户输入时，都应提供退出途径。
# 每次提示用户输入时，都使用break语句提供了退出循环的简单途径


while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

