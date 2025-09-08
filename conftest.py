# conftest.py
import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="session")  # 改为session，整个测试会话只启动一次浏览器
def driver():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")  # 保持function，每个测试函数登录一次
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login()
    yield driver

@pytest.fixture(scope="function")
def material_management_driver(logged_in_driver):
    """物料管理测试专用的driver"""
    driver = logged_in_driver
    target_url = "http://www.029tec.com/mes/md/mditem"
    if target_url not in driver.current_url:
        driver.get(target_url)
        time.sleep(1)
    yield driver