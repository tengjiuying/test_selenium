# 填写正确的注册信息，当填写错误时，返回错误信息
import time

from selenium.webdriver.common.by import By
from page.base_page import BasePage


class RegisterPage(BasePage):
    # 填写注册信息
    def register(self, compName, adminName, adminPhone, getVcode):
        self._driver.find_element(By.ID, "corp_name").send_keys(compName)
        self._driver.find_element(By.XPATH, "//span[text()='选择行业类型']").click()
        self._driver.find_element(By.XPATH, "//div[@data-name='IT服务']").click()
        self._driver.find_element(By.XPATH, "//a[text()=' 计算机软件/硬件/信息服务 ']").click()

        self._driver.find_element(By.XPATH, "//span[text()='选择员工规模']").click()
        self._driver.find_element(By.XPATH, "//span[text()='1-50人']").click()
        self._driver.find_element(By.ID, "manager_name").send_keys(adminName)
        self._driver.find_element(By.ID, "register_tel").send_keys(adminPhone)
        # 点击发送验证码按钮
        self._driver.find_element(By.ID, "get_vcode").click()
        time.sleep(10)
        self._driver.find_element(By.ID, getVcode).send_keys(getVcode)
        self._driver.find_element(By.ID, "iagree").click()
        # 等待注册按钮出现
        self._driver.implicitly_wait(5)
        self._driver.find_element(By.ID, "submit_btn").click()
        # 填写完毕可停留在注册页，继续调用该方法
        return self

    # 填写错误时返回错误信息
    def get_error_message(self):
        # return self.driver.find_element(By.CLASS_NAME,"error").text
        # 收集所有错误信息
        result = []
        for element in self._driver.find_elements(By.CSS_SELECTOR, "div.error"):
            result.append(element.text)
        return result
