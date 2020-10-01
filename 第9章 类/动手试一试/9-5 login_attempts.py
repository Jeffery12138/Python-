class User():
    """创建一个名为user的类"""
    def __init__(self, first_name, last_name):
        """初始化描述用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """打印用户的基本信息"""
        print("\nUser's first name: " + self.first_name)
        print("User's last name: " + self.last_name)

    def greet_user(self):
        """个性化问候用户"""
        full_name = self.first_name + self.last_name
        print(full_name.title() + ", nice to meet you.")

    def increment_login_attempts(self):
        """将login_attempts的值加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将login_attempts的值重置为0"""
        self.login_attempts = 0


user = User('Li', 'Junwei')
print("\nLogin attempts: " + str(user.login_attempts))
user.increment_login_attempts()
print("\nLogin attempts: " + str(user.login_attempts))
user.increment_login_attempts()
print("\nLogin attempts: " + str(user.login_attempts))
user.increment_login_attempts()
print("\nLogin attempts: " + str(user.login_attempts))
user.reset_login_attempts()
print("\nLogin attempts: " + str(user.login_attempts))
