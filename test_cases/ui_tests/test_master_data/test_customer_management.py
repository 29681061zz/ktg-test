#test_cases/ui_tests/test_master_data/test_customer_management.py
import time
import pytest
import allure
from pages.master_data.customer_management_page import CustomerManagementPage

@pytest.fixture(scope="function")
def customer_page(customer_management_driver):
    """创建物料管理页面对象"""
    return CustomerManagementPage(customer_management_driver)
class TestCustomerManagement:
    """物料管理测试用例"""
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "C00428"}, True),
        ({"code": "MAT_0000000000"}, False),
        ({"name": "xxx38"}, True),
        # ({"name": "不存在的物料"}, False),
        # ({"code": "MAT_1757231442","name": "测试物料CccC"}, True),
        # ({"code": "MAT_1756906978", "name": "不存在的物料"}, False)
    ])
    @allure.feature("客户管理")
    @allure.story("客户搜索功能")
    def test_search_material(self, customer_page, search_data, expected):
        """测试物料编码搜索功能 - 数据驱动"""
        # 搜索物料
        customer_page.search_material(search_data)
        # 验证搜索结果
        actual_result = customer_page.is_material_exists(search_data)
        assert actual_result == expected
