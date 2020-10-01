# 8.6.1 导入整个模块
# import pizza
# # 通过module_name.function_name()来使用已导入模块的所有函数
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.2 导入特定的函数
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数
# from module_name import function_0, function_1, function_2
# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')
# 使用这种语法，调用函数时无需使用句点

# # 8.6.3 使用as给函数指定别名
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
# # 指定别名的通用语法如下：
# # from module_name import function_name as fn

# 8.6.4 使用as给模块指定别名
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# # 不在关注模块名，而是专注于描述性的函数名
# # 给模块指定别名的通用语法：
# # import module_name as mn

# 8.6.5 导入模块中的所有函数
# 使用星号(*)可以导入模块中的所有函数
from pizza import *
# 由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 最佳的做法是，要么只导入你需要使用的函数，
# 要么导入整个模块并使用句点表示法。
# 这能让代码更清晰，更容易阅读和理解
