import pytest
import allure
from pages.warehouse_management_page.itemrecpt_page import ItemRecptPage
from utils.data_manager import DataManager

@pytest.fixture(scope="function")
def itemrecpt_page(itemrecpt_driver):
    """创建采购入库页面对象"""
    return ItemRecptPage(itemrecpt_driver)
@allure.feature("采购入库")
@pytest.mark.ui
class TestItemRecpt:
    """采购入库测试用例"""
    @allure.story("新增功能")
    @DataManager.warehouse('itemrecpt', 'add_cases', ['add_data', 'expected_result'])
    def test_add_itemrecpt(self, itemrecpt_page, add_data, expected_result):
        """测试采购入库新增功能 - 数据驱动"""
        itemrecpt_page.add_itemrecpt(add_data)
        # 搜索并验证新增的采购入库存在
        itemrecpt_page.search_itemrecpt(add_data)
        actual_result = itemrecpt_page.is_itemrecpt_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.warehouse('itemrecpt', 'search_cases', ['search_data', 'expected_result'])
    def test_search_itemrecpt(self, itemrecpt_page, search_data, expected_result):
        """测试采购入库搜索功能 - 数据驱动"""
        itemrecpt_page.search_itemrecpt(search_data)
        # 验证搜索结果
        actual_result = itemrecpt_page.is_itemrecpt_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.warehouse('itemrecpt', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_itemrecpt(self, itemrecpt_page, edit_data, expected_result):
        """测试采购入库修改功能 - 数据驱动"""
        itemrecpt_page.edit_itemrecpt(edit_data)
        actual_result = itemrecpt_page.is_itemrecpt_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.warehouse('itemrecpt', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_itemrecpt(self, itemrecpt_page, delete_data, expected_result):
        """测试采购入库删除功能 - 数据驱动"""
        itemrecpt_page.delete_itemrecpt(delete_data)
        actual_result = itemrecpt_page.is_itemrecpt_exists(delete_data)
        assert actual_result == expected_result
