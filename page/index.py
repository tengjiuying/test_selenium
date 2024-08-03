# 实现从首页跳转至注册页
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.login import LoginPage
from page.register import RegisterPage

class IndexPage(BasePage):
    _current_url = "https://work.weixin.qq.com/"
    # 进入注册页面
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '立即注册').click()
        return RegisterPage(self._driver)

    # 进入登录页面
    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, '企业登录').click()
        return LoginPage(self._driver)