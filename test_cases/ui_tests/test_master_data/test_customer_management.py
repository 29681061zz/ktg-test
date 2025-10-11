import pytest
import allure
from pages.master_data_pages.customer_management_page import CustomerManagementPage
from utils.data_manager import DataManager


@pytest.fixture(scope="function")
def customer_page(customer_management_driver):
    """创建客户管理页面对象"""
    return CustomerManagementPage(customer_management_driver)
@allure.feature("客户管理")
@pytest.mark.ui
class TestCustomerManagement:
    """客户管理测试用例"""
    @allure.story("新增功能")
    @DataManager.master('customer', 'add_cases', ['add_data', 'expected_result'])
    def test_add_customer(self, customer_page, add_data, expected_result):
        """测试客户新增功能 - 数据驱动"""
        customer_page.add_customer(add_data)
        # 搜索并验证新增的客户存在
        customer_page.search_customer(add_data)
        actual_result = customer_page.is_customer_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.master('customer', 'search_cases', ['search_data', 'expected_result'])
    def test_search_customer(self, customer_page, search_data, expected_result):
        """测试客户编码搜索功能 - 数据驱动"""
        # 搜索客户
        customer_page.search_customer(search_data)
        # 验证搜索结果
        actual_result = customer_page.is_customer_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.master('customer', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_customer(self, customer_page, edit_data, expected_result):
        """测试客户修改功能 - 数据驱动"""
        customer_page.edit_customer(edit_data)
        actual_result = customer_page.is_customer_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.master('customer', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_customer(self, customer_page, delete_data, expected_result):
        """测试客户删除功能 - 数据驱动"""
        customer_page.delete_customer(delete_data)
        actual_result = customer_page.is_customer_exists(delete_data)
        assert actual_result == expected_result
