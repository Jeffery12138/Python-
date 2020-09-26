# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")

# 6.3.2 遍历字典中的所有键
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in favorite_languages.keys():
#     print(name.title())
# # 遍历字典时会默认遍历所有的键，输出不变
# for name in favorite_languages:
#     print(name.title())
# # 显示地使用keys()方法可让代码更容易理解，如果愿意，也可省略它

# 在这种循环（键循环）可使用当前键来访问与之相关联的值。
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("\tHi " + name.title() + ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")

# 还可以使用keys()确定某个人是否接受了调查
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# 6.3.3 按顺序遍历字典中的所有键sorted()
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# 6.3.4 遍历字典中的所有值
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# print("The following languages have been mentioned:")
# # 没有考虑重复的值
# for language in favorite_languages.values():
#     print(language.title())

# 使用set()方法将列表转为集合，保证元素的独一无二
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())