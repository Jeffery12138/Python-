import unittest

from country_codes import get_country_code


class CountryCodesTestCase(unittest.TestCase):
    """测试country_codes.py"""

    def test_country_codes(self):
        """能够正确处理country_name吗"""
        code = get_country_code('Korea, Dem. People’s Rep.')
        self.assertEqual(code, 'kp')


unittest.main