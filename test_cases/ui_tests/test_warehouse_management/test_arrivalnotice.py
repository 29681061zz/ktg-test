import pytest
import allure
from pages.warehouse_management_page.arrivalnotice_page import ArrivalNoticePage
@pytest.fixture(scope="function")
def arrivalnotice_page(arrivalnotice_driver):
    """创建到货通知页面对象"""
    return ArrivalNoticePage(arrivalnotice_driver)
@allure.feature("到货通知")
@pytest.mark.ui
class TestArrivalNotice:
    """到货通知测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "ANT_001",
            "name": "新增到货通知_001",
            "pocode": "POC_001",
            "date": "2025-10-10",
            "vendorname": "测试供应商_001",
         }, True),
    ])
    def test_add_arrivalnotice(self, arrivalnotice_page, add_data, expected):
        """测试到货通知新增功能 - 数据驱动"""
        arrivalnotice_page.add_arrivalnotice(add_data)
        # 搜索并验证新增的到货通知存在
        arrivalnotice_page.search_arrivalnotice(add_data)
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "ANT_001"}, True),
        ({"code": "ANT_000"}, False),
        ({"name": "新增到货通知_001"}, True),
        # ({"name": "不存在的到货通知"}, False),
        # ({"code": "ANT_001","name": "新增到货通知_001"}, True),
        # ({"code": "ANT_001", "name": "不存在的到货通知"}, False)
    ])
    def test_search_arrivalnotice(self, arrivalnotice_page, search_data, expected):
        """测试到货通知搜索功能 - 数据驱动"""
        arrivalnotice_page.search_arrivalnotice(search_data)
        # 验证搜索结果
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "ANT_001",
            "edit_name": "修改到货通知",
            "pocode": "",
            "date": "9999-10-10",
            # "vendorname": "",
         }, True),
    ])
    def test_edit_arrivalnotice(self, arrivalnotice_page, edit_data, expected):
        """测试到货通知修改功能 - 数据驱动"""
        arrivalnotice_page.edit_arrivalnotice(edit_data)
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "ANT_001",}, False), # 期望删除后到货通知不存在
    ])
    def test_delete_arrivalnotice(self, arrivalnotice_page, delete_data, expected):
        """测试到货通知删除功能 - 数据驱动"""
        arrivalnotice_page.delete_arrivalnotice(delete_data)
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(delete_data)
        assert actual_result == expected
