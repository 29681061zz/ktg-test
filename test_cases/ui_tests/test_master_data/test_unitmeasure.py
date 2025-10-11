import pytest
import allure
from pages.master_data_pages.unitmeasure_page import UnitMeasurePage
from utils.data_manager import DataManager

@pytest.fixture(scope="function")
def unit_page(unitmeasure_driver):
    """创建计量单位页面对象"""
    return UnitMeasurePage(unitmeasure_driver)
@allure.feature("计量单位")
@pytest.mark.ui
class TestUnitMeasure:
    """单位管理测试用例"""
    @allure.story("新增功能")
    @DataManager.master('unitmeasure', 'add_cases', ['add_data', 'expected_result'])
    def test_add_unit(self, unit_page, add_data, expected_result):
        """测试单位新增功能 - 数据驱动"""
        unit_page.add_unit(add_data)
        # 搜索并验证新增的单位存在
        unit_page.search_unit(add_data)
        actual_result = unit_page.is_unit_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.master('unitmeasure', 'search_cases', ['search_data', 'expected_result'])
    def test_search_unit(self, unit_page, search_data, expected_result):
        """测试单位搜索功能 - 数据驱动"""
        unit_page.search_unit(search_data)
        # 验证搜索结果
        actual_result = unit_page.is_unit_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.master('unitmeasure', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_unit(self, unit_page, edit_data, expected_result):
        """测试单位修改功能 - 数据驱动"""
        unit_page.edit_unit(edit_data)
        actual_result = unit_page.is_unit_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.master('unitmeasure', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_unit(self, unit_page, delete_data, expected_result):
        """测试单位删除功能 - 数据驱动"""
        unit_page.delete_unit(delete_data)
        actual_result = unit_page.is_unit_exists(delete_data)
        assert actual_result == expected_result
