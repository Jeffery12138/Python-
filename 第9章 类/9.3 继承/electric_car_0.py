# 编写类时，并非总是要从空白开始。
# 如果你要编写的类是另一个现成类的特殊版本，可使用继承。
# 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；
# 原有的类称为父类，而新类称为子类。
# 子类继承了其父类的所有属性和方法，
# 同时还可以定义自己的属性和方法。

# 9.3.1 子类的方法__init__()
# 创建子类的实例时，
# Python首先需要完成的任务是给父类的所有属性赋值。
# 为此，子类的方法__init__()需要父类施以援手
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """Car类实例化的属性初始化"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回汽车的规范名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """读取汽车里程数"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程数设置为特定值"""
        """里程数不能倒转"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程数增加特定值"""
        """不能增加一个负值"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer")


# # 创建ElectricCar子类，继承父类Car
# # 创建子类时，父类必须包含在当前文件中，且位于子类前面。
# class ElectricCar(Car):
#     """电动汽车的独特之处"""
#     def __init__(self, make, model, year):
#         """初始化父类的属性"""
#         # super()是一个特殊函数，
#         # 帮助Python将父类和子类关联起来。
#         # 这行代码让Python调用ElectricCar的
#         # 父类的方法__init__()，
#         # 让ElectricCar实例包含父类的所有属性。
#         # 父类也称为超类（superclass），
#         # 名称super因此而得名。
#         super().__init__(make, model, year)
#
#         # 9.3.2 Python 2.7中的继承
#         # Python 2.7 语法如下，super()函数实参必不可少
#         # super(ElectricCar, self).__init__(make, model, year)
#         # 在Python 2.7中使用继承时，务必在定义父类时在括号内指定object
#
#
# my_tesla = ElectricCar('tesla', 'models', 2016)
# print(my_tesla.get_descriptive_name())

# 9.3.3 给子类定义属性和方法
# 让一个类继承另一个类后，
# 可添加区分子类和父类所需的新属性和方法。
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)

        # 对于ElectricCar类的特殊化程度没有任何限制。
        # 模拟电动汽车时，你可以根据所需的准确程度添加
        # 任意数量的属性和方法。
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'models', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
