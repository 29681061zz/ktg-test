import pytest
import allure
from pages.master_data.material_management_page import MaterialManagementPage

pytestmark = [pytest.mark.feature("物料管理")]
@pytest.fixture(scope="function")
def material_page(material_management_driver):
    """创建物料管理页面对象"""
    return MaterialManagementPage(material_management_driver)
class TestMaterialManagement:
    """物料管理测试用例"""
    @allure.story("搜索功能")
    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "MAT_001"}, True),
        ({"code": "MAT_0000000000"}, False),
        ({"name": "测试物料CccC"}, True),
        ({"name": "不存在的物料"}, False),
        ({"code": "MAT_1757231442","name": "测试物料CccC"}, True),
        ({"code": "MAT_1756906978", "name": "不存在的物料"}, False)
    ])
    def test_search_material(self, material_page, search_data, expected):
        """测试物料编码搜索功能 - 数据驱动"""
        # 搜索物料
        material_page.search_material(search_data)
        # 验证搜索结果
        actual_result = material_page.is_material_exists(search_data)
        assert actual_result == expected

    @allure.story("新增功能")
    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "MAT_002",
            "name": "新增物料_002",
            "specification": "10-50mm",
            "unit": "mm",
            "category": "原材料"
         }, True),
    ])
    def test_add_material(self, material_page, add_data, expected):
        """测试物料新增功能 - 数据驱动"""
        material_page.add_material(add_data)
        # 搜索并验证新增的物料存在
        material_page.search_material(add_data)
        actual_result = material_page.is_material_exists(add_data)
        assert actual_result == expected

    @allure.story("修改功能")
    @pytest.mark.parametrize("edit_data,expected", [
        ({"code": "MAT_002", "edit_code": "MAT_99999999"}, True),
        ({"code": "MAT_002", "edit_name": "修改物料_002"}, True),
        ({"code": "MAT_002", "specification": ""}, True),
        ({"code": "MAT_002", "unit": "米"}, True),
        ({"code": "MAT_002", "category": "产品成品"}, True),
        ({
            "code": "MAT_002",
            "edit_name": "新增物料_002",
            "specification": "10-50mm",
            "unit": "mm",
            "category": "原材料"
         }, True),
    ])
    def test_edit_material(self, material_page, edit_data, expected):
        """测试物料修改功能 - 数据驱动"""
        material_page.edit_material(edit_data)
        actual_result = material_page.is_material_exists(edit_data)
        assert actual_result == expected

    @allure.story("删除功能")
    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "MAT_002",}, False), # 期望删除后物料不存在
    ])
    def test_delete_material(self, material_page, delete_data, expected):
        """测试物料删除功能 - 数据驱动"""
        material_page.delete_material(delete_data)
        actual_result = material_page.is_material_exists(delete_data)
        assert actual_result == expected


