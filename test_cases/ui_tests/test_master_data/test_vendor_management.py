import pytest
import allure
from pages.master_data_pages.vendor_management_page import VendorPage
from utils.data_manager import DataManager


@pytest.fixture(scope="function")
def vendor_page(vendor_management_driver):
    """创建供应商管理页面对象"""
    return VendorPage(vendor_management_driver)
@allure.feature("供应商管理")
@pytest.mark.ui
class TestVendorManagement:
    """供应商管理测试用例"""
    @allure.story("新增功能")
    @DataManager.master('vendor', 'add_cases', ['add_data', 'expected_result'])
    def test_add_vendor(self, vendor_page, add_data, expected_result):
        """测试供应商新增功能 - 数据驱动"""
        vendor_page.add_vendor(add_data)
        # 搜索并验证新增的供应商存在
        vendor_page.search_vendor(add_data)
        actual_result = vendor_page.is_vendor_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.master('vendor', 'search_cases', ['search_data', 'expected_result'])
    def test_search_vendor(self, vendor_page, search_data, expected_result):
        """测试供应商搜索功能 - 数据驱动"""
        vendor_page.search_vendor(search_data)
        # 验证搜索结果
        actual_result = vendor_page.is_vendor_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.master('vendor', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_vendor(self, vendor_page, edit_data, expected_result):
        """测试供应商修改功能 - 数据驱动"""
        vendor_page.edit_vendor(edit_data)
        actual_result = vendor_page.is_vendor_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.master('vendor', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_vendor(self, vendor_page, delete_data, expected_result):
        """测试供应商删除功能 - 数据驱动"""
        vendor_page.delete_vendor(delete_data)
        actual_result = vendor_page.is_vendor_exists(delete_data)
        assert actual_result == expected_result
