# 前10个数[1, 10]的平方的列表

# 创建一个空列表
squares = []
# 使用range()函数遍历1~10的值
for value in range(1, 11):
    # 在循环中计算当前值得平方，并将结果存储到square中
    square = value ** 2
    # 将新计算得到的平方值附加到列表squares末尾
    squares.append(square)
# 循环结束后，打印列表squares
print(squares)

# 为了使代码更简洁，可不使用临时变量square，而直接将每个计算得到的值附加到列表末尾
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value**2 for value in range(1, 11)]
print(squares)