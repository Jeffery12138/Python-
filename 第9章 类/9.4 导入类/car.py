"""一个可用于表示汽车的类"""


class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始换描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """返回整洁的描述性名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条消息，指出汽车的里程"""
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        拒绝将里程表往回拨
        :param mileage:
        :return:
        """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        将里程表的读数增加指定的量
        拒绝将里程表往回拨
        :param miles:
        :return:
        """
        if miles >= 0:
            self.odometer += miles
        else:
            print("You can't roll back an odometer!")


