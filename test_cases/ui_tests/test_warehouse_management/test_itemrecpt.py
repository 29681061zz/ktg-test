import pytest
import allure
from pages.warehouse_management_page.itemrecpt_page import ItemRecptPage
@pytest.fixture(scope="function")
def itemrecpt_page(itemrecpt_driver):
    """创建采购入库页面对象"""
    return ItemRecptPage(itemrecpt_driver)
@allure.feature("采购入库")
@pytest.mark.ui
class TestItemRecpt:
    """采购入库测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "IRT_001",
            "name": "新增采购入库_001",
            "pocode": "POC_001",
            "date": "2025-10-10",
            "vendorname": "测试供应商_001",
            "noticecode": "ANT_001",
         }, True),
    ])
    def test_add_itemrecpt(self, itemrecpt_page, add_data, expected):
        """测试采购入库新增功能 - 数据驱动"""
        itemrecpt_page.add_itemrecpt(add_data)
        # 搜索并验证新增的采购入库存在
        itemrecpt_page.search_itemrecpt(add_data)
        actual_result = itemrecpt_page.is_itemrecpt_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "IRT_001"}, True),
        ({"code": "IRT_000"}, False),
        ({"name": "新增采购入库_001"}, True),
        # ({"name": "不存在的采购入库"}, False),
        # ({"code": "ANT_001","name": "新增采购入库_001"}, True),
        # ({"code": "ANT_001", "name": "不存在的采购入库"}, False)
    ])
    def test_search_itemrecpt(self, itemrecpt_page, search_data, expected):
        """测试采购入库搜索功能 - 数据驱动"""
        itemrecpt_page.search_itemrecpt(search_data)
        # 验证搜索结果
        actual_result = itemrecpt_page.is_itemrecpt_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "IRT_001",
            "edit_name": "修改采购入库",
            "pocode": "",
            "date": "9999-10-10",
            # "vendorname": "",
         }, True),
    ])
    def test_edit_itemrecpt(self, itemrecpt_page, edit_data, expected):
        """测试采购入库修改功能 - 数据驱动"""
        itemrecpt_page.edit_itemrecpt(edit_data)
        actual_result = itemrecpt_page.is_itemrecpt_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "IRT_001",}, False), # 期望删除后采购入库不存在
    ])
    def test_delete_itemrecpt(self, itemrecpt_page, delete_data, expected):
        """测试采购入库删除功能 - 数据驱动"""
        itemrecpt_page.delete_itemrecpt(delete_data)
        actual_result = itemrecpt_page.is_itemrecpt_exists(delete_data)
        assert actual_result == expected
