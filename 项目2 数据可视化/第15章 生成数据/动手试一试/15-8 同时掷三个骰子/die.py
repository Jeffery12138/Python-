from random import randint


class Die():
    """一个模拟骰子的类"""
    def __init__(self, num_sides=6):
        """初始化"""
        self.num_sides = num_sides

    def roll(self):
        """模拟掷骰子，返回一个介于1和最大值的值"""
        return randint(1, self.num_sides)