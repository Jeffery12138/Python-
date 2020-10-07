import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    # TestCase类中包含了方法setUp()，
    # Python将先运行它，再运行各个以test_打头的方法。
    # 这样每个测试方法中都可使用在方法setUp()中创建的对象了。
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        :return:
        """
        question = "What language did you first learn to speak?"
        # 变量名包含前缀self(即存储在属性中)，可在这个类的任何地方使用
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main