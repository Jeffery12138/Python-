# 10.3.7 使用多个文件
# def count_words(filename):
#     """计算一个文本文件大致包含多少个单词"""
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#     else:
#         # 计算文件大致包含多少个单词
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) + " words.")
#

# filename = 'alice.txt'
# count_words(filename)

# 现在可以编写一个简单的循环，
# 计算要分析的任何文本包含多少个单词了。
# 为此，我们将要分析的文件的名称存储在一个列表中，
# 然后对列表中的每个文件都调用count_words()。
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
# for filename in filenames:
#     count_words(filename)

# 在这个示例中，使用try-except代码块提供了两个重要的优点：
# 避免让用户看到traceback；
# 让程序能够继续分析能够找到的其他文件。
# 如果不捕获因找不到siddhartha.txt而引发的FileNotFoundError异常，
# 用户将看到完整的traceback，
# 而程序将在尝试分析Siddhartha后停止运行
# ——根本不分析Moby Dick和LittleWomen。

# 10.3.8 失败时一声不吭
# 在前一个示例中，我们告诉用户有一个文件找不到。
# 但并非每次捕获到异常时都需要告诉用户，
# 有时候你希望程序在发生异常时一声不吭，
# 就像什么都没有发生一样继续运行。
# 要让程序在失败时一声不吭，可像通常那样编写try代码块，
# 但在except代码块中明确地告诉Python什么都不要做。
# Python有一个pass语句，
# 可在代码块中使用它来让Python什么都不要做：
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# note:
# pass语句还充当了占位符，
# 它提醒你在程序的某个地方什么都没有做，
# 并且以后也许要在这里做些什么。
# 例如，在这个程序中，
# 我们可能决定将找不到的文件的名称写入到文件missing_files.txt中。
# 用户看不到这个文件，但我们可以读取这个文件，
# 进而处理所有文件找不到的问题。

# 10.3.9 决定报告哪些错误
# 编写得很好且经过详尽测试的代码不容易出现内部错误，
# 如语法或逻辑错误，
# 但只要程序依赖于外部因素，如用户输入、存在指定的文件、
# 有网络链接，就有可能出现异常。
# 凭借经验可判断该在程序的什么地方包含异常处理块，
# 以及出现错误时该向用户提供多少相关的信息。
