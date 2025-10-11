import pytest
import allure
from pages.warehouse_management_page.arrivalnotice_page import ArrivalNoticePage
from utils.data_manager import DataManager


@pytest.fixture(scope="function")
def arrivalnotice_page(arrivalnotice_driver):
    """创建到货通知页面对象"""
    return ArrivalNoticePage(arrivalnotice_driver)
@allure.feature("到货通知")
@pytest.mark.ui
class TestArrivalNotice:
    """到货通知测试用例"""
    @allure.story("新增功能")
    @DataManager.warehouse('arrivalnotice', 'add_cases', ['add_data', 'expected_result'])
    def test_add_arrivalnotice(self, arrivalnotice_page, add_data, expected_result):
        """测试到货通知新增功能 - 数据驱动"""
        arrivalnotice_page.add_arrivalnotice(add_data)
        # 搜索并验证新增的到货通知存在
        arrivalnotice_page.search_arrivalnotice(add_data)
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.warehouse('arrivalnotice', 'search_cases', ['search_data', 'expected_result'])
    def test_search_arrivalnotice(self, arrivalnotice_page, search_data, expected_result):
        """测试到货通知搜索功能 - 数据驱动"""
        arrivalnotice_page.search_arrivalnotice(search_data)
        # 验证搜索结果
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.warehouse('arrivalnotice', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_arrivalnotice(self, arrivalnotice_page, edit_data, expected_result):
        """测试到货通知修改功能 - 数据驱动"""
        arrivalnotice_page.edit_arrivalnotice(edit_data)
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.warehouse('arrivalnotice', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_arrivalnotice(self, arrivalnotice_page, delete_data, expected_result):
        """测试到货通知删除功能 - 数据驱动"""
        arrivalnotice_page.delete_arrivalnotice(delete_data)
        actual_result = arrivalnotice_page.is_arrivalnotice_exists(delete_data)
        assert actual_result == expected_result
