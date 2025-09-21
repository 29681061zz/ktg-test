import pytest
import allure
from pages.master_data.vendor_management_page import VendorPage

pytestmark = [pytest.mark.feature("供应商管理")]
@pytest.fixture(scope="function")
def vendor_page(vendor_management_driver):
    """创建供应商管理页面对象"""
    return VendorPage(vendor_management_driver)
class TestVendorPage:
    """供应商管理测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "VEN_001",
            "name": "新增供应商_001",
            "abbreviation": "测试",
            "rating": "4",
         }, True),
    ])
    def test_add_vendor(self, vendor_page, add_data, expected):
        """测试供应商新增功能 - 数据驱动"""
        vendor_page.add_vendor(add_data)
        # 搜索并验证新增的供应商存在
        vendor_page.search_vendor(add_data)
        actual_result = vendor_page.is_vendor_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "VEN_001"}, True),
        ({"code": "VEN_000"}, False),
        ({"name": "新增供应商_001"}, True),
        # ({"name": "不存在的供应商"}, False),
        # ({"code": "VEN_001","name": "新增供应商_001"}, True),
        # ({"code": "VEN_001", "name": "不存在的供应商"}, False)
    ])
    def test_search_vendor(self, vendor_page, search_data, expected):
        """测试供应商搜索功能 - 数据驱动"""
        vendor_page.search_vendor(search_data)
        # 验证搜索结果
        actual_result = vendor_page.is_vendor_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "VEN_001",
            "edit_name": "修改供应商",
            "abbreviation": "",
            "rating": "5",
         }, True),
    ])
    def test_edit_vendor(self, vendor_page, edit_data, expected):
        """测试供应商修改功能 - 数据驱动"""
        vendor_page.edit_vendor(edit_data)
        actual_result = vendor_page.is_vendor_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "VEN_001",}, False), # 期望删除后供应商不存在
    ])
    def test_delete_vendor(self, vendor_page, delete_data, expected):
        """测试供应商删除功能 - 数据驱动"""
        vendor_page.delete_vendor(delete_data)
        actual_result = vendor_page.is_vendor_exists(delete_data)
        assert actual_result == expected
