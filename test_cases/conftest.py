import pytest
from configs.settings import Config

@pytest.fixture(scope="function")
def material_management_driver(logged_in_driver, request):
    """物料管理driver"""
    # 将driver存储到request中，供hook使用
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/mditem"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def customer_management_driver(logged_in_driver, driver):
    """客户管理driver"""
    driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/client"
    driver.get(target_url)
    yield driver

@pytest.fixture(scope="function")
def unitmeasure_driver(logged_in_driver, driver):
    """计量单位driver"""
    driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/unitmeasure"
    driver.get(target_url)
    yield driver

@pytest.fixture(scope="function")
def vendor_management_driver(logged_in_driver, driver):
    """供应商管理driver"""
    driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/vendor"
    driver.get(target_url)
    yield driver