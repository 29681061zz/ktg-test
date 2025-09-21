import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator_tuple):
        """locator_tuple: (By.SOMETHING, 'selector')"""
        self.find(locator_tuple).click()

    def find(self, locator_tuple, allow_empty=False):
        """查找单个元素"""
        by, locator = locator_tuple
        if allow_empty:
            # 快速模式：直接查找，不等待，立即返回结果或None
            try:
                return self.driver.find_element(by, locator)
            except NoSuchElementException:
                return None  # 没找到，返回None
        else:
            # 稳定模式：等待元素加载完成
            return self.wait.until(EC.presence_of_element_located((by, locator)))
    def find_elements(self, locator_tuple, allow_empty=False):
        """查找多个元素"""
        by, locator = locator_tuple
        if allow_empty:
            # 快速模式：直接查找，不等待，立即返回结果
            return self.driver.find_elements(by, locator)
        else:
            # 稳定模式：等待元素加载完成
            return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def input_text(self, locator_tuple, text):
        """locator_tuple: (By.SOMETHING, 'selector')"""
        element = self.find(locator_tuple)
        element.click()
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.clear()
        element.send_keys(text)

    def clear_input(self,locator_tuple):
        """清空输入框内容:param locator_tuple: 元素定位器元组，如 (By.ID, "username")"""
        element = self.find(locator_tuple)
        element.clear()  # 使用Selenium的clear()方法
        time.sleep(0.1)  # 短暂等待确保清空完成

    def select_option(self, select_locator, option_text):
        # 点击下拉框展开选项
        self.click(select_locator)
        # 构建选项定位器 - Element UI的选项结构
        option_locator = (By.XPATH,f"//div[@class='el-select-dropdown el-popper']//li[contains(@class, 'el-select-dropdown__item') and span[text()='{option_text}']]")
        # 点击选项
        self.click(option_locator)
