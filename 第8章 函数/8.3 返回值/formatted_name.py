# 8.3.1 返回简单值
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#
#     # 调用返回值的函数时，需要提供一个变量，用于存储返回的值。
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# 8.3.2 让实参变成可选的
# def get_formatted_name(first_name, middle_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + " " + middle_name + " " + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# 可给实参middle_name指定一个默认值——空字符串，
# 并将其移到形参列表的末尾：
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# 可选值让函数能够处理各种不同情形的同时，确保函数调用尽可能简单。