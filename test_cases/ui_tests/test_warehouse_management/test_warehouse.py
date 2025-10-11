import pytest
import allure
from pages.warehouse_management_page.warehouse_page import WareHousePage
from utils.data_manager import DataManager

@pytest.fixture(scope="function")
def warehouse_page(warehouse_driver):
    """创建仓库设置页面对象"""
    return WareHousePage(warehouse_driver)
@allure.feature("仓库设置")
@pytest.mark.ui
class TestWareHouse:
    """仓库测试用例"""
    @allure.story("新增功能")
    @DataManager.warehouse('warehouse', 'add_cases', ['add_data', 'expected_result'])
    def test_add_warehouse(self, warehouse_page, add_data, expected_result):
        """测试仓库新增功能 - 数据驱动"""
        warehouse_page.add_warehouse(add_data)
        # 搜索并验证新增的仓库存在
        warehouse_page.search_warehouse(add_data)
        actual_result = warehouse_page.is_warehouse_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.warehouse('warehouse', 'search_cases', ['search_data', 'expected_result'])
    def test_search_warehouse(self, warehouse_page, search_data, expected_result):
        """测试仓库搜索功能 - 数据驱动"""
        warehouse_page.search_warehouse(search_data)
        # 验证搜索结果
        actual_result = warehouse_page.is_warehouse_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.warehouse('warehouse', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_warehouse(self, warehouse_page, edit_data, expected_result):
        """测试仓库修改功能 - 数据驱动"""
        warehouse_page.edit_warehouse(edit_data)
        actual_result = warehouse_page.is_warehouse_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.warehouse('warehouse', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_warehouse(self, warehouse_page, delete_data, expected_result):
        """测试仓库删除功能 - 数据驱动"""
        warehouse_page.delete_warehouse(delete_data)
        actual_result = warehouse_page.is_warehouse_exists(delete_data)
        assert actual_result == expected_result
