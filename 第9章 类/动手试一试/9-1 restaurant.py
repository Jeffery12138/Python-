class Restaurant():
    """创建一个restaurant的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化描述餐厅的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印餐厅的信息"""
        print("\nRestaurant name: " + self.restaurant_name)
        print("Cuisine type: " + self.cuisine_type)

    def open_restaurant(self):
        """打印餐厅正在营业"""
        print("The " + self.restaurant_name + " restaurant is open.")


restaurant = Restaurant('shuizhuyu', 'all cooked')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_0 = Restaurant('ZERO', 'cool')
restaurant_1 = Restaurant('ONE', 'warm')
restaurant_2 = Restaurant('TWO', 'frozen')
restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()