# 实现从首页跳转至注册页
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.login import LoginPage
from page.register import RegisterPage

class IndexPage(BasePage):
    # 进入注册页面
    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        return RegisterPage(self.driver)

    # 进入登录页面
    def goto_login(self):
        self.driver.find_element(By.LINK_TEXT, 'Login').click()
        return LoginPage(self.driver)