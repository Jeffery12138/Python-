class Employee():
    """一个Employee的类"""
    def __init__(self, first_name, last_name, annual_salary):
        """属性初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, annual_salary_raise=5000):
        self.annual_salary += annual_salary_raise
