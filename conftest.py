# conftest.py
import time
import pytest
from selenium import webdriver
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
    target_url = "http://www.029tec.com/mes/md/mditem"
    if target_url not in driver.current_url:
        driver.get(target_url)
        time.sleep(1)
    yield driver