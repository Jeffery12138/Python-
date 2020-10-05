def count_word(filename, word):
    """计算一个文件中某个单词出现了多少次"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # 计算某个单词出现了多少次
        num_word = contents.lower().count(word)
        print("The word '" + word + "' has appears " + str(num_word) + " times in the " + filename + ".")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_word(filename, word='the')