# 9.3.4 重写父类方法

# 对于父类的方法,只要它不符合子类模拟的实物的行为,都可以对其进行重写.
# 可在子类定义一个这样的方法,即它与要重写的父类方法同名.
# 这样Python将不会考虑这个父类方法，而只关注在子类定义的相应方法
class Car():
    """再一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """类的实例化的属性初始化"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回实例汽车的正式名称"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """读取汽车里程表"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """设置里程数为特定值"""
        """不能让里程表倒转"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程增加特定值"""
        """不能增加一个负值"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self, gas_number):
        """给汽车加特定体积大汽油"""
        print("Add " + str(gas_number) + "liters of fuel to the car.")


class ElectricCar(Car):
    """模拟电动车的尝试"""
    def __init__(self, make, model, year):
        """
        参数初始化
        将子类与父类关联
        :param make:
        :param model:
        :param year:
        """
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        """电动汽车没有邮箱"""
        print("This car doesn't need a gas tank!")


my_car = ElectricCar('tesla', 'models', 2016)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()
