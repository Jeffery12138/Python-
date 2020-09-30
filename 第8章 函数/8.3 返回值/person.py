# 8.3.3 返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构
# def build_person(first_name, last_name):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#
#     return person
#
#
# musician = build_person('jimi', 'hendrix')
# print(musician)

# 你可以轻松地扩展这个函数，使其接受可选值，
# 如中间名、年龄、职业或你要存储的其他任何信息。
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)