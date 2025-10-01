import pytest
import allure
from pages.master_data_pages.workstation_page import WorkStationPage

@pytest.fixture(scope="function")
def workstation_page(workstation_driver):
    """创建工作站页面对象"""
    return WorkStationPage(workstation_driver)
@allure.feature("工作站")
@pytest.mark.ui
class TestWorkStation:
    """工作站测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "WST_001",
            "name": "新增工作站_001",
            "location": "新增工作站地点",
            "workshop": "测试车间",
            "process": "测试工序",
         }, True),
    ])
    def test_add_workstation(self, workstation_page, add_data, expected):
        """测试工作站新增功能 - 数据驱动"""
        workstation_page.add_workstation(add_data)
        # 搜索并验证新增的工作站存在
        workstation_page.search_workstation(add_data)
        actual_result = workstation_page.is_workstation_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "WST_001"}, True),
        ({"code": "WST_000"}, False),
        ({"name": "新增工作站_001"}, True),
        # ({"name": "不存在的工作站"}, False),
        # ({"code": "WST_001","name": "新增工作站_001"}, True),
        # ({"code": "WST_001", "name": "不存在的工作站"}, False)
    ])
    def test_search_workstation(self, workstation_page, search_data, expected):
        """测试工作站搜索功能 - 数据驱动"""
        workstation_page.search_workstation(search_data)
        # 验证搜索结果
        actual_result = workstation_page.is_workstation_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "WST_001",
            "edit_name": "修改工作站",
            "location": "",
         }, True),
    ])
    def test_edit_workstation(self, workstation_page, edit_data, expected):
        """测试工作站修改功能 - 数据驱动"""
        workstation_page.edit_workstation(edit_data)
        actual_result = workstation_page.is_workstation_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "WST_001",}, False), # 期望删除后工作站不存在
    ])
    def test_delete_workstation(self, workstation_page, delete_data, expected):
        """测试工作站删除功能 - 数据驱动"""
        workstation_page.delete_workstation(delete_data)
        actual_result = workstation_page.is_workstation_exists(delete_data)
        assert actual_result == expected
