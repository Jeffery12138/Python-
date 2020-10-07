# 首先导入测试模块
import unittest
# 导入要测试的函数
from name_function import get_formatted_name


# 我们创建了一个名为NamesTestCase的类，
# 用于包含一系列针对get_formatted_name()的单元测试。
# 你可随便给这个类命名，但最好让它看起来与要测试的函数相关，
# 并包含字样Test。
# 这个类必须继承unittest.TestCase类。
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # 我们使用了unittest类最有用的功能之一：
        # 一个断言方法。
        # 断言方法用来核实得到的结果是否与期望的结果一致。
        # 将formatted_name的值同字符串'Janis Joplin'
        # 进行比较，如果它们相等，就万事大吉，
        # 如果它们不相等，跟我说一声！
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# unittest.main()让Python运行这个文件中的测试。
# 我学这段的时候unittest.main()这样执行时，Test 0。
# 改成unittest.main,就可以了。具体是什么原因，
# 我猜测是（）里面需要把测试对象写进去。
unittest.main