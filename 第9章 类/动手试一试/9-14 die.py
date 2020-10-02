from random import randint


class Die():
    """创建一个骰子的类"""
    def __init__(self, sides=6):
        """初始化骰子的属性"""
        self.sides = sides

    def roll_die(self):
        """打印位于1和骰子面数之间的随机数"""
        x = randint(1, self.sides)
        print(x)


die_6 = Die()
print("\n掷10次6面的骰子，结果如下：")
for i in range(10):
    die_6.roll_die()
print("\n掷10次10面的骰子，结果如下：")
die_10 = Die(10)
for i in range(10):
    die_10.roll_die()
print("\n掷10次20面的骰子，结果如下：")
die_20 = Die(20)
for i in range(10):
    die_20.roll_die()