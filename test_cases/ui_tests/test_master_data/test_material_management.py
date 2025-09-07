#test_cases/ui_tests/test_master_data/test_material_management.py
import time
import pytest
import allure
from pages.master_data.material_management_page import MaterialManagementPage

class TestMaterialManagement:
    """物料管理测试用例"""

    @pytest.mark.parametrize("search_data,expected", [
        ({"code": "MAT_1757231442"}, True),
        ({"code": "MAT_0000000000"}, False),
        ({"name": "测试物料CccC"}, True),
        ({"name": "不存在的物料"}, False),
        ({"code": "MAT_1757231442","name": "测试物料CccC"}, True),
        ({"code": "MAT_1756906978", "name": "不存在的物料"}, False)
    ])
    @allure.feature("物料管理")
    @allure.story("物料搜索功能")
    def test_search_material(self, material_management_driver, search_data, expected):
        """测试物料编码搜索功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        # 搜索物料
        material_page.search_material(search_data)
        # 验证搜索结果
        actual_result = material_page.is_material_exists(search_data)
        assert actual_result == expected

    @pytest.mark.parametrize("add_data,expected", [
        ({
            "code": "MAT_1756907106",
            "name": "测试物料A",
            "specification": "10-50mm",
            "unit": "米",
            "category": "原材料"
         }, True),
        # ({
        #      "code": f"MAT_{int(time.time()) + 1}",
        #      "name": "测试物料DddD",
        #      "unit": "米",
        #      "category": "原材料"
        #  }, True),
    ])
    @allure.feature("物料管理")
    @allure.story("物料新增功能")
    def test_add_material(self, material_management_driver, add_data, expected):
        """测试物料新增功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        material_page.add_material(add_data)
        # 搜索并验证新增的物料存在
        material_page.search_material(add_data)
        actual_result = material_page.is_material_exists(add_data)
        assert actual_result == expected

    @pytest.mark.parametrize("edit_data,expected", [
        ({
            "code" : "MAT_1756907106",
            # "edit_code": "MAT_99999999",
            "edit_name": "qqq",
            "specification": "",
            "unit": "mm",
         }, True),

    ])
    @allure.feature("物料管理")
    @allure.story("物料修改功能")
    def test_edit_material(self, material_management_driver, edit_data, expected):
        """测试物料修改功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        material_page.edit_material(edit_data)
        actual_result = material_page.is_material_exists(edit_data)
        assert actual_result == expected


    @pytest.mark.parametrize("delete_data,expected", [
        ({"code" : "MAT_1756907106",}, False), # 期望删除后物料不存在
    ])
    @allure.feature("物料管理")
    @allure.story("物料删除功能")
    def test_delete_material(self, material_management_driver, delete_data, expected):
        """测试物料修改功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        material_page.delete_material(delete_data)
        actual_result = material_page.is_material_exists(delete_data)
        assert actual_result == expected


