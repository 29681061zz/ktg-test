import pytest
import allure
from pages.master_data.unitmeasure_page import UnitmeasurePage


@pytest.fixture(scope="function")
def unit_page(unitmeasure_driver):
    """创建计量单位页面对象"""
    return UnitmeasurePage(unitmeasure_driver)
@allure.feature("计量单位")
@pytest.mark.ui
class TestUnitMeasure:
    """单位管理测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
             "code": "UNI_001",
             "name": "新增单位_001",
             "is_main_unit": "是",
         }, True),
        ({
            "code": "UNI_003",
            "name": "新增单位_003",
            "is_main_unit": "否",
            "main_unit": "新增单位_001",
            "conversion": "1000",
         }, True),
    ])
    def test_add_unit(self, unit_page, add_data, expected):
        """测试单位新增功能 - 数据驱动"""
        unit_page.add_unit(add_data)
        # 搜索并验证新增的单位存在
        unit_page.search_unit(add_data)
        actual_result = unit_page.is_unit_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "UNI_001"}, True),
        ({"code": "UNI_000"}, False),
        ({"name": "新增单位_001"}, True),
        # ({"name": "不存在的单位"}, False),
        # ({"code": "UNI_001","name": "新增单位_001"}, True),
        # ({"code": "UNI_001", "name": "不存在的单位"}, False)
    ])
    def test_search_unit(self, unit_page, search_data, expected):
        """测试单位搜索功能 - 数据驱动"""
        unit_page.search_unit(search_data)
        # 验证搜索结果
        actual_result = unit_page.is_unit_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "UNI_001",
            "edit_name": "修改单位",
            "is_main_unit": "是",
            # "main_unit": "公斤",
            "conversion": "",
         }, True),
    ])
    def test_edit_unit(self, unit_page, edit_data, expected):
        """测试单位修改功能 - 数据驱动"""
        unit_page.edit_unit(edit_data)
        actual_result = unit_page.is_unit_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "UNI_001",}, False), # 期望删除后单位不存在
    ])
    def test_delete_unit(self, unit_page, delete_data, expected):
        """测试单位删除功能 - 数据驱动"""
        unit_page.delete_unit(delete_data)
        actual_result = unit_page.is_unit_exists(delete_data)
        assert actual_result == expected
