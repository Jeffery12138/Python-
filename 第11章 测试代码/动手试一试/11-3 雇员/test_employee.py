import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""
    def setUp(self):
        """创建雇员实例，供使用的测试方法使用"""
        self.my_employee = Employee('Li', 'Junwei', 300000)

    def test_give_default_raise(self):
        """测试默认涨薪5000"""
        self.my_employee.give_raise()
        self.assertEqual(305000, self.my_employee.annual_salary)

    def test_give_custom_raise(self):
        """测试任意涨薪数量"""
        self.my_employee.give_raise(-10000)
        self.assertEqual(290000, self.my_employee.annual_salary)


unittest.main