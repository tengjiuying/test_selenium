# 为子类提供公共方法：
# 提供初始化driver和退出driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver=None):
        # 对driver进行复用，若不存在driver则创建一个新的
        if driver is None:
            self.driver = webdriver.Chrome()
            # 设置隐式等待时间
            self._driver.implicitly_wait(3)
            # 访问网页
            self._driver.get('http://127.0.0.1:8000')
        else:
            # login与register需要使用该方法，避免重复构造driver
            self.driver = driver
    def close(self):
        sleep(20)
        self._driver.quit()