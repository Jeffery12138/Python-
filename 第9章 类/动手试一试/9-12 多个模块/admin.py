from user import User


class Privileges():
    """创建一个权限类"""
    def __init__(self):
        """属性初始换"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示管理员权限"""
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """创建管理员子类"""
    def __init__(self, first_name, last_name):
        """初始换管理员属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.privilege = Privileges()
