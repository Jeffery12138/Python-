def print_content(filename):
    """
    读取文本文档，打印内容
    对FileNotFoundError进行捕获
    :param filename:
    :return:
    """
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + " does not exist.")
    else:
        pets = contents.split()
        print(pets)


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print_content(filename)