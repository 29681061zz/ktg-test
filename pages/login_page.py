from .base_page import BasePage
from configs.settings import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytesseract
from PIL import Image
import base64
import io
import re

class LoginPage(BasePage):
    # 定位器
    LOGIN_BUTTON = (By.XPATH, "//button[.//span[text()='登 录']]")
    CAPTCHA_INPUT = (By.XPATH, "//input[@placeholder='验证码']")  # 验证码输入框
    CAPTCHA_IMAGE = (By.CLASS_NAME, "login-code-img")  # 验证码图片

    USER_AVATAR = (By.CLASS_NAME, "user-avatar")  # 登录后的用户头像
    AVATAR_WRAPPER = (By.CLASS_NAME, "avatar-wrapper")  # 头像包装器

    def login(self):
        """一键登录操作"""
        # 先导航到登录页面确保状态
        self.driver.get(f"{Config.BASE_URL}/login")

        captcha_expression = self.get_captcha_text() # 识别验证码表达式
        captcha_result = self.calculate_captcha(captcha_expression)# 计算验证码

        self.input_text(self.CAPTCHA_INPUT,str(captcha_result))
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON),message="等待登录按钮可点击超时")
        login_btn.click()
        # 等待URL变化（离开登录页面）
        self.wait.until(lambda driver: "login" not in driver.current_url, message="等待页面跳转超时")
        # 等待用户头像出现（最可靠的登录成功标志）
        self.wait.until(EC.presence_of_element_located(self.USER_AVATAR), message="等待用户头像出现超时")
        return True

    def get_captcha_text(self):
        """获取并识别验证码"""
        try:
            # 等待验证码图片加载
            captcha_element = self.wait.until(
                EC.presence_of_element_located(self.CAPTCHA_IMAGE),
                message="等待验证码图片加载超时"
            )

            # 提取Base64数据
            src_data = captcha_element.get_attribute("src")
            if not src_data or "base64" not in src_data:
                raise ValueError("验证码图片数据格式不正确")

            base64_data = src_data.split(",")[1]

            # 解码为图片
            image_data = base64.b64decode(base64_data)
            image = Image.open(io.BytesIO(image_data))

            # 图片预处理
            image = image.convert('L')  # 转灰度
            # 可选：二值化处理（根据实际效果调整阈值）
            # image = image.point(lambda x: 0 if x < 180 else 255)

            # OCR识别
            captcha_text = pytesseract.image_to_string(image).strip()
            print(f"识别出的验证码文本: '{captcha_text}'")

            # 清理文本，提取数学表达式
            cleaned_text = re.sub(r'[^\d+\-*/=]', '', captcha_text)
            cleaned_text = cleaned_text.rstrip('=')
            print(f"清理后的表达式: '{cleaned_text}'")

            return cleaned_text

        except Exception as e:
            print(f"验证码识别失败: {e}")
            return None

    def calculate_captcha(self, expression):
        """安全计算验证码表达式"""
        try:
            if not expression:
                return None

            if '+' in expression:
                parts = expression.split('+')
                return int(parts[0]) + int(parts[1])
            elif '-' in expression:
                parts = expression.split('-')
                return int(parts[0]) - int(parts[1])
            elif '*' in expression:
                parts = expression.split('*')
                return int(parts[0]) * int(parts[1])
            elif '/' in expression:
                parts = expression.split('/')
                return int(parts[0]) // int(parts[1])  # 整除
            else:
                return None
        except (ValueError, IndexError, ZeroDivisionError):
            return None


