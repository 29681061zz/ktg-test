from .base_page import BasePage
from configs.settings import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import ddddocr
import time

class LoginPage(BasePage):
    # 定位器
    LOGIN_BUTTON = (By.XPATH, "//button[.//span[text()='登 录']]")
    CAPTCHA_INPUT = (By.XPATH, "//input[@placeholder='验证码']")
    CAPTCHA_IMAGE = (By.CLASS_NAME, "login-code-img")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), '验证码错误')]")
    USER_AVATAR = (By.CLASS_NAME, "user-avatar")

    def login(self, max_retries=10):
        """一键登录操作，验证码错误时自动重试"""
        self.driver.get(f"{Config.BASE_URL}/login")
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        ocr = ddddocr.DdddOcr(show_ad=False)
        retry_count = 0
        while retry_count < max_retries:
            try:
                # 识别验证码
                captcha_element = self.find(self.CAPTCHA_IMAGE)
                self.wait.until(lambda d: captcha_element.get_attribute("src") is not None)
                src_data = captcha_element.get_attribute("src")
                base64_data = src_data.split(",")[1]
                text = ocr.classification(base64_data)
                captcha_result = self.calculate_captcha(text)


                if captcha_result is None:
                    retry_count += 1
                    continue

                # 输入验证码
                self.input_text(self.CAPTCHA_INPUT, str(captcha_result))
                # 点击登录
                self.click(self.LOGIN_BUTTON)

                # 检查错误提示
                try:
                    error_element = self.find(self.ERROR_MESSAGE)
                    if error_element.is_displayed():
                        retry_count += 1
                        continue
                except TimeoutException:
                    pass

                # 检查登录成功
                try:
                    self.find(self.USER_AVATAR)
                    return True
                except TimeoutException:
                    retry_count += 1
                    continue

            except Exception:
                retry_count += 1
                if retry_count < max_retries:
                    time.sleep(0.5)
        return False

    def calculate_captcha(self, expression):
        try:
            if expression[1] == '+' or expression[1] == 't':
                return int(expression[0]) + int(expression[2])
            if expression[1] == '-' or expression[1] == 'r':
                return int(expression[0]) - int(expression[2])
            if expression[1] == '*' or expression[1] == 'x':
                return int(expression[0]) * int(expression[2])
            if expression[1] == '/' or expression[1] == 'l':
                return int(expression[0]) // int(expression[2])
            return int(expression[0]) - int(expression[1])
        except (ValueError, IndexError):
            return None