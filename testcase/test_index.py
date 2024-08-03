import unittest

from page import register
from page.index import IndexPage

class MyTestCase(unittest.TestCase):
    # 所有步骤初始化
    def setUp(self):
        self.index = IndexPage()
    def test_register(self):
        self.index.goto_register().register("2940681539@qq.com","12345")

    def test_login(self):
        self.index.goto_login().login("2940681539@qq.com","12345")
        # 断言填写结果，判断是否填写成功
        assert "请选择" in "|".join(register.RegisterPage.get_error_message())

    def tearDown(self):
        self.index.close()


