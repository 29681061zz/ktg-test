import pytest
import allure
from pages.warehouse_management_page.warehouse_page import WareHouse
@pytest.fixture(scope="function")
def warehouse_page(warehouse_driver):
    """创建仓库设置页面对象"""
    return WareHouse(warehouse_driver)
@allure.feature("仓库设置")
@pytest.mark.ui
class TestWareHouse:
    """仓库测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "WHS_001",
            "name": "新增仓库_001",
            "area": "100",
            "location": "新增仓库地点",
            "remark": "新增仓库",
         }, True),
    ])
    def test_add_warehouse(self, warehouse_page, add_data, expected):
        """测试仓库新增功能 - 数据驱动"""
        warehouse_page.add_warehouse(add_data)
        # 搜索并验证新增的仓库存在
        warehouse_page.search_warehouse(add_data)
        actual_result = warehouse_page.is_warehouse_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "WHS_001"}, True),
        ({"code": "WHS_000"}, False),
        ({"name": "新增仓库_001"}, True),
        # ({"name": "不存在的仓库"}, False),
        # ({"code": "WHS_001","name": "新增仓库_001"}, True),
        # ({"code": "WHS_001", "name": "不存在的仓库"}, False)
    ])
    def test_search_warehouse(self, warehouse_page, search_data, expected):
        """测试仓库搜索功能 - 数据驱动"""
        warehouse_page.search_warehouse(search_data)
        # 验证搜索结果
        actual_result = warehouse_page.is_warehouse_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "WHS_001",
            "edit_name": "修改仓库",
            "area": "0",
            "location": "",
            "remark": "",
         }, True),
    ])
    def test_edit_warehouse(self, warehouse_page, edit_data, expected):
        """测试仓库修改功能 - 数据驱动"""
        warehouse_page.edit_warehouse(edit_data)
        actual_result = warehouse_page.is_warehouse_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "WHS_001",}, False), # 期望删除后仓库不存在
    ])
    def test_delete_warehouse(self, warehouse_page, delete_data, expected):
        """测试仓库删除功能 - 数据驱动"""
        warehouse_page.delete_warehouse(delete_data)
        actual_result = warehouse_page.is_warehouse_exists(delete_data)
        assert actual_result == expected
