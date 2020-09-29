# 函数是带名字的代码块，用于完成具体的工作。
# 需要在程序中多次执行同一项任务时，你无需反复编写完成该任务的代码，
# 而只需调用执行该任务的函数，让Python运行其中的代码。

# 使用关键字def来告诉Python你要定义一个函数。
# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
#
#
# # 函数调用让Python执行函数的代码。
# greet_user()


# 8.1.1 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")


greet_user('jesse')


# 8.1.2 实参和形参
# 在函数greet_user()的定义中，变量username是一个形参
# ——函数完成其工作所需的一项信息。
# 在代码greet_user('jesse')中，值'jesse'是一个实参。
# 实参是调用函数时传递给函数的信息。

