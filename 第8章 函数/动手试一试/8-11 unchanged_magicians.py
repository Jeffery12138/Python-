def show_magicians(magicians):
    """打印每个魔术师的名字"""
    for magician in magicians:
        print(magician)


def make_great(magicians):
    """让每个魔术师变得great"""
    for i in range(len(magicians)):
        # 修改列表中的元素
        # motorcycles[0] = 'ducati'
        magicians[i] = "the Great " + magicians[i]

    return magicians


magicians = ['lili', 'tod', 'jack', 'bob']
show_magicians(magicians)
magicians_copy = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_copy)