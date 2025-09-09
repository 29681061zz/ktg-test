# conftest.py
import time
import pytest
from selenium import webdriver
from configs.settings import Config
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(1)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login()
    yield driver

@pytest.fixture(scope="function")
def material_management_driver(logged_in_driver):
    """物料管理测试专用的driver"""
    driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/mditem"
    driver.get(target_url)
    yield driver

@pytest.fixture(scope="function")
def customer_management_driver(logged_in_driver):
    """物料管理测试专用的driver"""
    driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/client"
    driver.get(target_url)
    yield driver