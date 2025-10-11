import pytest
import allure
from pages.master_data_pages.workshop_setup_page import WorkShopPage
from utils.data_manager import DataManager


@pytest.fixture(scope="function")
def workshop_page(workshop_setup_driver):
    """创建车间设置页面对象"""
    return WorkShopPage(workshop_setup_driver)
@allure.feature("车间设置")
@pytest.mark.ui
class TestWorkShopSetup:
    """车间设置测试用例"""
    @allure.story("新增功能")
    @DataManager.master('workshop', 'add_cases', ['add_data', 'expected_result'])
    def test_add_workshop(self, workshop_page, add_data, expected_result):
        """测试车间新增功能 - 数据驱动"""
        workshop_page.add_workshop(add_data)
        # 搜索并验证新增的车间存在
        workshop_page.search_workshop(add_data)
        actual_result = workshop_page.is_workshop_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.master('workshop', 'search_cases', ['search_data', 'expected_result'])
    def test_search_workshop(self, workshop_page, search_data, expected_result):
        """测试车间搜索功能 - 数据驱动"""
        workshop_page.search_workshop(search_data)
        # 验证搜索结果
        actual_result = workshop_page.is_workshop_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.master('workshop', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_workshop(self, workshop_page, edit_data, expected_result):
        """测试车间修改功能 - 数据驱动"""
        workshop_page.edit_workshop(edit_data)
        actual_result = workshop_page.is_workshop_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.master('workshop', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_workshop(self, workshop_page, delete_data, expected_result):
        """测试车间删除功能 - 数据驱动"""
        workshop_page.delete_workshop(delete_data)
        actual_result = workshop_page.is_workshop_exists(delete_data)
        assert actual_result == expected_result
