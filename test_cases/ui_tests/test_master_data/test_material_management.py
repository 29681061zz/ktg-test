import pytest
import allure
from pages.master_data_pages.material_management_page import MaterialManagementPage

@pytest.fixture(scope="function")
def material_page(material_management_driver):
    """创建物料管理页面对象"""
    return MaterialManagementPage(material_management_driver)

@allure.feature("物料管理")
@pytest.mark.ui
class TestMaterialManagement:
    """物料管理测试用例"""
    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "MAT_001",
            "name": "新增物料_001",
            "specification": "10-50mm",
            "unit": "测试单位001",
            "category": "测试物料分类"
         }, True),
    ])
    def test_add_material(self, material_page, add_data, expected):
        """测试物料新增功能 - 数据驱动"""
        material_page.add_material(add_data)
        # 搜索并验证新增的物料存在
        material_page.search_material(add_data)
        actual_result = material_page.is_material_exists(add_data)
        assert actual_result == expected

    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "MAT_001"}, True),
        ({"code": "MAT_000"}, False),
        ({"name": "新增物料_001"}, True),
        ({"name": "不存在的物料"}, False),
        ({"code": "MAT_001","name": "新增物料_001"}, True),
        ({"code": "MAT_001", "name": "不存在的物料"}, False)
    ])
    def test_search_material(self, material_page, search_data, expected):
        """测试物料编码搜索功能 - 数据驱动"""
        # 搜索物料
        material_page.search_material(search_data)
        # 验证搜索结果
        actual_result = material_page.is_material_exists(search_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({"code": "MAT_001", "edit_code": "MAT_99999999"}, False),
        ({"code": "MAT_001", "edit_name": "修改物料_001"}, True),
        ({"code": "MAT_001", "specification": ""}, True),
        ({"code": "MAT_001", "unit": "测试单位002"}, True),
        ({"code": "MAT_001", "category": "测试产品分类"}, True),
        ({
            "code": "MAT_001",
            "edit_name": "新增物料_001",
            "specification": "10-50mm",
            "unit": "测试单位001",
            "category": "测试物料分类"
         }, True),
    ])
    def test_edit_material(self, material_page, edit_data, expected):
        """测试物料修改功能 - 数据驱动"""
        material_page.edit_material(edit_data)
        actual_result = material_page.is_material_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "MAT_001",}, False), # 期望删除后物料不存在
    ])
    def test_delete_material(self, material_page, delete_data, expected):
        """测试物料删除功能 - 数据驱动"""
        material_page.delete_material(delete_data)
        actual_result = material_page.is_material_exists(delete_data)
        assert actual_result == expected


