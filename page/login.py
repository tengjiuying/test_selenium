# 进入注册页面，扫描二维码
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.register import RegisterPage

class LoginPage(BasePage):
    # 扫描二维码
    def scan_qrcode(self):
        pass
    # 进入注册页
    def goto_register_page(self):
        self.driver.find_element(By.XPATH, '//a[@class="index_head_info_pCDownloadBtn"]').click()
        return RegisterPage(self.driver)