import pytest
import allure
from pages.master_data.customer_management_page import CustomerManagementPage


@pytest.fixture(scope="function")
def customer_page(customer_management_driver):
    """创建客户管理页面对象"""
    return CustomerManagementPage(customer_management_driver)
@allure.feature("客户管理")
@pytest.mark.ui
class TestCustomerManagement:
    """客户管理测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "CUS_001",
            "name": "新增客户_001",
         }, True),
    ])
    def test_add_customer(self, customer_page, add_data, expected):
        """测试客户新增功能 - 数据驱动"""
        customer_page.add_customer(add_data)
        # 搜索并验证新增的客户存在
        customer_page.search_customer(add_data)
        actual_result = customer_page.is_customer_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "CUS_001"}, True),
        ({"code": "CUS_0000000000"}, False),
        ({"name": "新增客户_001"}, True),
        # ({"name": "不存在的客户"}, False),
        # ({"code": "MAT_1756907106","name": "测试客户A"}, True),
        # ({"code": "MAT_1756906978", "name": "不存在的客户"}, False)
    ])
    def test_search_customer(self, customer_page, search_data, expected):
        """测试客户编码搜索功能 - 数据驱动"""
        # 搜索客户
        customer_page.search_customer(search_data)
        # 验证搜索结果
        actual_result = customer_page.is_customer_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "CUS_001",
            # "edit_code": "MAT_99999999",
            "edit_name": "修改客户",
         }, True),
    ])
    def test_edit_customer(self, customer_page, edit_data, expected):
        """测试客户修改功能 - 数据驱动"""
        customer_page.edit_customer(edit_data)
        actual_result = customer_page.is_customer_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "CUS_001",}, False), # 期望删除后客户不存在
    ])
    def test_delete_customer(self, customer_page, delete_data, expected):
        """测试客户删除功能 - 数据驱动"""
        customer_page.delete_customer(delete_data)
        actual_result = customer_page.is_customer_exists(delete_data)
        assert actual_result == expected
