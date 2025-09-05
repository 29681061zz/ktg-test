import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator_tuple):
        by, locator = locator_tuple
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, locator_tuple):
        """locator_tuple: (By.SOMETHING, 'selector')"""
        self.find(locator_tuple).click()

    def find_elements(self, locator_tuple, timeout=None):
        """查找多个元素"""
        try:
            by, locator = locator_tuple

            if timeout:
                return self.wait.until(EC.presence_of_all_elements_located((by, locator)))
            else:
                return self.driver.find_elements(by, locator)

        except Exception as e:
            print(f"查找多个元素失败: {e}")
            return []

    def input_text(self, locator_tuple, text):
        """locator_tuple: (By.SOMETHING, 'selector')"""
        element = self.find(locator_tuple)
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


    def type(self, locator_tuple, text):
        elem = self.find(locator_tuple)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator_tuple):
        elem = self.find(locator_tuple)
        return elem.text

    def screenshot(self, name):
        self.driver.save_screenshot(name)