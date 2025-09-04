from selenium.webdriver.common.by import By


class ConfirmModal:
    """确认弹窗组件"""

    def __init__(self, driver):
        self.driver = driver

    def confirm(self):
        confirm_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'确认')]")
        confirm_btn.click()

    def cancel(self):
        cancel_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'取消')]")
        cancel_btn.click()