class Restaurant():
    """创建一个restaurant的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化描述餐厅的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印餐厅的信息"""
        print("\nRestaurant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        """打印餐厅正在营业"""
        print("The " + self.restaurant_name + " restaurant is open.")

    def set_number_served(self, number_served):
        """设置就餐人数"""
        self.number_served = number_served

    def increment_number_served(self, number_served_increment):
        """将就餐人数递增"""
        self.number_served += number_served_increment


class IceCreamStand(Restaurant):
    """创建一个冰淇淋小店类，继承Restaurant类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化冰淇淋小店的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Green Tea']
        super().__init__(restaurant_name, cuisine_type)

    def get_flavors(self):
        """显示所有的冰淇淋口味"""
        print("There are the following ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)