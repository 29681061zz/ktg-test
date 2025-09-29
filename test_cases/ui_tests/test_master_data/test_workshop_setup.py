import pytest
import allure
from pages.master_data.workshop_setup_page import WorkshopPage

@pytest.fixture(scope="function")
def workshop_page(workshop_setup_driver):
    """创建车间设置页面对象"""
    return WorkshopPage(workshop_setup_driver)
@allure.feature("车间设置")
@pytest.mark.ui
class TestWorkShopSetup:
    """车间设置测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "WOR_001",
            "name": "新增车间_001",
            "area": "1000",
         }, True),
    ])
    def test_add_workshop(self, workshop_page, add_data, expected):
        """测试车间新增功能 - 数据驱动"""
        workshop_page.add_workshop(add_data)
        # 搜索并验证新增的车间存在
        workshop_page.search_workshop(add_data)
        actual_result = workshop_page.is_workshop_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "WOR_001"}, True),
        ({"code": "WOR_000"}, False),
        ({"name": "新增车间_001"}, True),
        # ({"name": "不存在的车间"}, False),
        # ({"code": "WOR_001","name": "新增车间_001"}, True),
        # ({"code": "WOR_001", "name": "不存在的车间"}, False)
    ])
    def test_search_workshop(self, workshop_page, search_data, expected):
        """测试车间搜索功能 - 数据驱动"""
        workshop_page.search_workshop(search_data)
        # 验证搜索结果
        actual_result = workshop_page.is_workshop_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "WOR_001",
            "edit_name": "修改车间",
            "area": "0",
         }, True),
    ])
    def test_edit_workshop(self, workshop_page, edit_data, expected):
        """测试车间修改功能 - 数据驱动"""
        workshop_page.edit_workshop(edit_data)
        actual_result = workshop_page.is_workshop_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "WOR_001",}, False), # 期望删除后车间不存在
    ])
    def test_delete_workshop(self, workshop_page, delete_data, expected):
        """测试车间删除功能 - 数据驱动"""
        workshop_page.delete_workshop(delete_data)
        actual_result = workshop_page.is_workshop_exists(delete_data)
        assert actual_result == expected
