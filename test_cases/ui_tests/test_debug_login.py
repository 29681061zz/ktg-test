# test_debug_login.py
import pytest
from pages.login_page import LoginPage


class TestDebugLogin:
    """专门用于调试登录问题的测试"""

    def test_direct_login(self, driver):
        """直接登录测试，模拟 TestLogin 的行为"""
        print("=== 直接登录测试开始 ===")
        login_page = LoginPage(driver)
        result = login_page.login()
        print(f"直接登录结果: {result}")
        print(f"最终URL: {driver.current_url}")
        assert result

    def test_via_fixture(self, logged_in_driver):
        """通过fixture登录测试，模拟物料管理测试的行为"""
        print("=== Fixture登录测试开始 ===")
        print(f"Fixture登录后URL: {logged_in_driver.current_url}")
        # 只是验证状态，不执行其他操作
        assert True