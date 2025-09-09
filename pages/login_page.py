from .base_page import BasePage
from configs.settings import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.BASE_URL}/login"
    # 定位器
    LOGIN_BUTTON = (By.XPATH, "//button[.//span[text()='登 录']]")
    USER_AVATAR = (By.CLASS_NAME, "user-avatar")  # 登录后的用户头像
    AVATAR_WRAPPER = (By.CLASS_NAME, "avatar-wrapper")  # 头像包装器

    def login(self):
        """一键登录操作"""
        # 先导航到登录页面确保状态
        self.driver.get(self.url)
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON),message="等待登录按钮可点击超时")
        login_btn.click()
        # 等待URL变化（离开登录页面）
        self.wait.until(lambda driver: "login" not in driver.current_url, message="等待页面跳转超时")
        # 等待用户头像出现（最可靠的登录成功标志）
        self.wait.until(EC.presence_of_element_located(self.USER_AVATAR), message="等待用户头像出现超时")
        return True

    def ensure_logged_in(self):
        """确保处于登录状态"""
        # 先检查当前状态
        if self.is_logged_in():
            return True
        # 执行登录
        return self.login()

    def is_logged_in(self):
        """检查是否已经登录 - 通过用户头像元素判断"""
        try:
            current_url = self.driver.current_url

            # 如果在登录页面，肯定未登录
            if "login" in current_url:
                # print("在登录页面，未登录")
                return False
            # 检查用户头像元素（最可靠的判断方式）
            try:
                # 检查头像包装器
                avatar_wrapper = self.find(self.AVATAR_WRAPPER)
                if avatar_wrapper and avatar_wrapper.is_displayed():
                    # print("找到用户头像包装器，已登录")
                    return True
            except:
                pass

            try:
                # 检查用户头像图片
                user_avatar = self.find(self.USER_AVATAR)
                if user_avatar and user_avatar.is_displayed():
                    # print("找到用户头像，已登录")
                    return True
            except:
                pass
            # print("未找到登录证据")
            return False
        except Exception as e:
            # print(f"检查登录状态时出错: {e}")
            return False


