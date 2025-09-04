#test_cases/ui_tests/test_master_data/test_material_management.py
import time
import pytest
import allure
from pages.master_data.material_management_page import MaterialManagementPage

class TestMaterialManagement:
    """物料管理测试用例"""

    @pytest.mark.parametrize("material_code,expected", [
        ("MAT_1756906978", True),
        ("MAT_1756907105", True),
        ("99999999999", False),  # 不存在的编码
        ("", False),  # 空编码
    ])
    @allure.feature("物料管理")
    @allure.story("物料编码搜索功能")
    def test_search_material_by_code(self, material_management_driver, material_code, expected):
        """测试物料编码搜索功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        # 搜索物料
        material_page.search_material(material_code=material_code)
        # 验证搜索结果
        actual_result = material_page.is_material_exists(material_code=material_code)
        assert actual_result == expected

    @pytest.mark.parametrize("material_name,expected", [
        ("测试物料A", True),
        ("测试物料B", True),
        ("不存在的物料", False),  # 不存在的名称
        ("", False),  # 空名称
    ])
    @allure.feature("物料管理")
    @allure.story("物料名称搜索功能")
    def test_search_material_by_name(self, material_management_driver, material_name, expected):
        """测试物料名称搜索功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        # 搜索物料
        material_page.search_material(material_name=material_name)
        # 验证搜索结果
        actual_result = material_page.is_material_exists(material_name=material_name)
        assert actual_result == expected

    @pytest.mark.parametrize("material_data,expected", [
        ({
             "material_code": f"MAT_{int(time.time())}",
             "material_name": "测试物料CccC",
             "unit": "件",
             "category": "原材料"
         }, True),
        ({
             "material_code": f"MAT_{int(time.time()) + 1}",
             "material_name": "测试物料DddD",
             "unit": "米",
             "category": "原材料"
         }, True),
    ])
    @allure.feature("物料管理")
    @allure.story("物料新增功能")
    def test_add_new_material(self, material_management_driver, material_data, expected):
        """测试物料新增功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        material_page.add_new_material(material_data)
        # 搜索并验证新增的物料存在
        material_page.search_material(material_code=material_data["material_code"])
        actual_result = material_page.is_material_exists(material_code=material_data["material_code"])
        assert actual_result == expected

    @pytest.mark.parametrize("new_data,expected", [
        ({
             "material_code": "MAT_1756966634",
             "material_name": "测试物料CccC",
             "unit": "件",
             "category": "原材料"
         }, True),
        # ({
        #      "material_code": f"MAT_{int(time.time()) + 1}",
        #      "material_name": "测试物料DddD",
        #      "unit": "米",
        #      "category": "原材料"
        #  }, True),
    ])
    @allure.feature("物料管理")
    @allure.story("物料修改功能")
    def test_edit_material(self, material_management_driver, new_data, expected):
        """测试物料修改功能 - 数据驱动"""
        material_page = MaterialManagementPage(material_management_driver)
        material_page.edit_material(new_data)
        # 搜索并验证新增的物料存在
        material_page.search_material(material_code=new_data["material_code"])
        actual_result = material_page.is_material_exists(material_code=new_data["material_code"])
        assert actual_result == expected


