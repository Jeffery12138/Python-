class User():
    """创建一个名为user的类"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nUser's first name: " + self.first_name)
        print("User's last name: " + self.last_name)

    def greet_user(self):
        full_name = self.first_name + self.last_name
        print(full_name.title() + ", nice to meet you.")


user_0 = User('Li', 'Junwei')
user_0.describe_user()
user_0.greet_user()

user_1 = User('Liu', 'Yang')
user_1.describe_user()
user_1.greet_user()