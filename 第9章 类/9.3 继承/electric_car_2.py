# 9.3.5 将实例用作属性

# 使用代码模拟实物时，给类添加的细节越来越多，属性和方法清单以及文件都越来越长。
# 需要将类的一部分作为一个独立的类提取出来。
# 可以将大型类拆分成多个协同工作的小类
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


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self, car_model):
        """打印一条描述电瓶车续航里程的信息"""
        """续航里程由电瓶容量和汽车型号共同决定"""
        if car_model == 'models':
            if self.battery_size == 70:
                range = 240
            elif self.battery_size == 85:
                range = 270
        else:
            range = 100
        message = car_model + " can go approximately " + str(range)
        message += " miles on a full charge with a " + str(self.battery_size) + "-kWh battery."
        print(message)


class ElectricCar(Car):
    """模拟电动车的尝试"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        :param make:
        :param model:
        :param year:
        """
        super().__init__(make, model, year)
        # self.battery = Battery()
        self.battery = Battery(battery_size=85)


my_tesla = ElectricCar('tesla', 'models', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range('models')
