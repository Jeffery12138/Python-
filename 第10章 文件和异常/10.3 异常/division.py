# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。
# 每当发生让Python不知所措的错误时，它都会创建一个异常对象。
# 如果你编写了处理该异常的代码，程序将继续运行；
# 如果你未对异常进行处理，程序将停止，并显示一个traceback，
# 其中包含有关异常的报告。
# 异常是使用try-except代码块处理的。
# try-except代码块让Python执行指定的操作，
# 同时告诉Python发生异常时怎么办。
# 使用了try-except代码块时，即便出现异常，
# 程序也将继续运行：
# 显示你编写的友好的错误消息，
# 而不是令用户迷惑的traceback。

# 10.3.1 处理ZeroDivisionError异常
# print(5/0)
# ZeroDivisionError: division by zero
# ZeroDivisionError是一个异常对象

# 10.3.2 使用try-except代码块
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# 如果try-except代码块后面还有其他代码，
# 程序将接着运行，因为已经告诉了Python如何处理这种错误。

# 10.3.3 使用异常避免崩溃
# 发生错误时，如果程序还有工作没有完成，
# 妥善地处理错误就尤其重要。
# 这种情况经常会出现在要求用户提供输入的程序中；
# 如果程序能够妥善地处理无效输入，
# 就能再提示用户提供有效输入，而不至于崩溃。

# 创建一个只执行除法运算的简单计算器
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number:")
#     if first_number == 'q':
#         break
#     second_number = input("Second number:")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

# 10.3.4 else代码块
# 通过将可能引发错误的代码放在try-except代码块中，
# 可提高这个程序抵御错误的能力。
# 错误是执行除法运算的代码行导致的，
# 因此我们需要将它放到try-except代码块中。
# 这个示例还包含一个else代码块；
# 依赖于try代码块成功执行的代码都应放到else代码块中：

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# try-except-else代码块的工作原理大致如下：
# Python尝试执行try代码块中的代码；
# 只有可能引发异常的代码才需要放在try语句中。
# 有时候，有一些仅在try代码块成功执行时才需要运行的代码；
# 这些代码应放在else代码块中。
# except代码块告诉Python，
# 如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。
# 通过预测可能发生错误的代码，可编写健壮的程序，
# 它们即便面临无效数据或缺少资源，也能继续运行，
# 从而能够抵御无意的用户错误和恶意的攻击。