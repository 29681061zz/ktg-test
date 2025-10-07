import pytest
from configs.settings import Config

@pytest.fixture(scope="function")
def warehouse_driver(logged_in_driver, request):
    """仓库设置driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/wm/warehouse"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def arrivalnotice_driver(logged_in_driver, request):
    """到货通知driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/wm/arrivalnotice"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def itemrecpt_driver(logged_in_driver, request):
    """采购入库driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/wm/itemrecpt"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def productrecpt_driver(logged_in_driver, request):
    """产品入库driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/wm/productrecpt"
    logged_in_driver.get(target_url)
    yield logged_in_driver