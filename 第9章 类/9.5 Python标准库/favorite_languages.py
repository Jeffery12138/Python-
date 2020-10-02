# 要创建字典并记录其中的键—值对的添加顺序，
# 可使用模块collections中的OrderedDict类。

# 这是一个很不错的类，它兼具列表和字典的主要优点
# （在将信息关联起来的同时保留原来的顺序）。
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
