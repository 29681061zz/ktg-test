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
def customer_management_driver(logged_in_driver, request):
    """客户管理driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/client"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def unitmeasure_driver(logged_in_driver, request):
    """计量单位driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/unitmeasure"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def vendor_management_driver(logged_in_driver, request):
    """供应商管理driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/vendor"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def workshop_setup_driver(logged_in_driver, request):
    """车间设置driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/workshop"
    logged_in_driver.get(target_url)
    yield logged_in_driver

@pytest.fixture(scope="function")
def workstation_driver(logged_in_driver, request):
    """工作站driver"""
    request.node.driver = logged_in_driver
    target_url = f"{Config.BASE_URL}/mes/md/workstation"
    logged_in_driver.get(target_url)
    yield logged_in_driver