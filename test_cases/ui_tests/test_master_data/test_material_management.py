import pytest
import allure
from utils.data_manager import DataManager
from pages.master_data_pages.material_management_page import MaterialManagementPage

@pytest.fixture(scope="function")
def material_page(material_management_driver):
    """创建物料管理页面对象"""
    return MaterialManagementPage(material_management_driver)

@allure.feature("物料管理")
@pytest.mark.ui
class TestMaterialManagement:
    """物料管理测试 - 数据驱动"""
    @allure.story("新增功能")
    @DataManager.parametrize_master_data('material_management', 'add_cases', ['add_data', 'expected_result'])
    def test_add_material(self, material_page, add_data, expected_result):
        material_page.add_material(add_data)
        # 搜索并验证新增的物料存在
        material_page.search_material(add_data)
        actual_result = material_page.is_material_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.parametrize_master_data('material_management', 'search_cases', ['search_data', 'expected_result'])
    def test_search_material(self, material_page, search_data, expected_result):
        # 搜索物料
        material_page.search_material(search_data)
        # 验证搜索结果
        actual_result = material_page.is_material_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.parametrize_master_data('material_management', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_material(self, material_page, edit_data, expected_result):
        material_page.edit_material(edit_data)
        actual_result = material_page.is_material_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.parametrize_master_data('material_management', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_material(self, material_page, delete_data, expected_result):
        material_page.delete_material(delete_data)
        actual_result = material_page.is_material_exists(delete_data)
        assert actual_result == expected_result


