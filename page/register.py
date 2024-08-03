# 填写正确的注册信息，当填写错误时，返回错误信息
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class RegisterPage(BasePage):
    # 填写注册信息
    def register(self, email, password):
        self.driver.find_element(By.ID,"email").send_keys(email)
        self.driver.find_element(By.ID,"password").send_keys(password)
        self.driver.find_element(By.ID,"submit").click()
        # 填写完毕可停留在注册页，继续调用该方法
        return self

    # 填写错误时返回错误信息
    def get_error_message(self):
        # return self.driver.find_element(By.CLASS_NAME,"error").text
        # 收集所有错误信息
        result = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, "div.error"):
            result.append(element.text)
        return result