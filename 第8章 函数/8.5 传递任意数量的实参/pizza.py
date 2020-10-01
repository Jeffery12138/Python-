# 预先不知道函数需要接受多少个实参
# 形参名*toppings中的星号让python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中。
# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     """概述要制作的比萨"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- "+topping)
#
#
# # 不管收到的是一个值还是三个值，这个函数都能妥善处理
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 8.5.1 结合使用位置实参和任意数量实参
# 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
# python先匹配位置实参和关键字实参，在讲余下的实参都收集到最后一个形参中。

# 前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings的前面
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print("\nMaking a "+ str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
