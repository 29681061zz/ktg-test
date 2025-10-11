import pytest
import allure
from pages.master_data_pages.workstation_page import WorkStationPage
from utils.data_manager import DataManager


@pytest.fixture(scope="function")
def workstation_page(workstation_driver):
    """创建工作站页面对象"""
    return WorkStationPage(workstation_driver)
@allure.feature("工作站")
@pytest.mark.ui
class TestWorkStation:
    """工作站测试用例"""
    @allure.story("新增功能")
    @DataManager.master('workstation', 'add_cases', ['add_data', 'expected_result'])
    def test_add_workstation(self, workstation_page, add_data, expected_result):
        """测试工作站新增功能 - 数据驱动"""
        workstation_page.add_workstation(add_data)
        # 搜索并验证新增的工作站存在
        workstation_page.search_workstation(add_data)
        actual_result = workstation_page.is_workstation_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.master('workstation', 'search_cases', ['search_data', 'expected_result'])
    def test_search_workstation(self, workstation_page, search_data, expected_result):
        """测试工作站搜索功能 - 数据驱动"""
        workstation_page.search_workstation(search_data)
        # 验证搜索结果
        actual_result = workstation_page.is_workstation_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.master('workstation', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_workstation(self, workstation_page, edit_data, expected_result):
        """测试工作站修改功能 - 数据驱动"""
        workstation_page.edit_workstation(edit_data)
        actual_result = workstation_page.is_workstation_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.master('workstation', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_workstation(self, workstation_page, delete_data, expected_result):
        """测试工作站删除功能 - 数据驱动"""
        workstation_page.delete_workstation(delete_data)
        actual_result = workstation_page.is_workstation_exists(delete_data)
        assert actual_result == expected_result
