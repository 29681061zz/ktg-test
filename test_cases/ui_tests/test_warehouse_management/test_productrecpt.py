import pytest
import allure
from pages.warehouse_management_page.productrecpt_page import ProductRecptPage
from utils.data_manager import DataManager

@pytest.fixture(scope="function")
def productrecpt_page(productrecpt_driver):
    """创建产品入库页面对象"""
    return ProductRecptPage(productrecpt_driver)
@allure.feature("产品入库")
@pytest.mark.ui
class TestProductRecpt:
    """产品入库测试用例"""
    @allure.story("新增功能")
    @DataManager.warehouse('productrecpt', 'add_cases', ['add_data', 'expected_result'])
    def test_add_productrecpt(self, productrecpt_page, add_data, expected_result):
        """测试产品入库新增功能 - 数据驱动"""
        productrecpt_page.add_productrecpt(add_data)
        # 搜索并验证新增的产品入库存在
        productrecpt_page.search_productrecpt(add_data)
        actual_result = productrecpt_page.is_productrecpt_exists(add_data)
        assert actual_result == expected_result

    @allure.story("搜索功能")
    @DataManager.warehouse('productrecpt', 'search_cases', ['search_data', 'expected_result'])
    def test_search_productrecpt(self, productrecpt_page, search_data, expected_result):
        """测试产品入库搜索功能 - 数据驱动"""
        productrecpt_page.search_productrecpt(search_data)
        # 验证搜索结果
        actual_result = productrecpt_page.is_productrecpt_exists(search_data)
        assert actual_result == expected_result

    @allure.story("修改功能")
    @DataManager.warehouse('productrecpt', 'edit_cases', ['edit_data', 'expected_result'])
    def test_edit_productrecpt(self, productrecpt_page, edit_data, expected_result):
        """测试产品入库修改功能 - 数据驱动"""
        productrecpt_page.edit_productrecpt(edit_data)
        actual_result = productrecpt_page.is_productrecpt_exists(edit_data)
        assert actual_result == expected_result

    @allure.story("删除功能")
    @DataManager.warehouse('productrecpt', 'delete_cases', ['delete_data', 'expected_result'])
    def test_delete_productrecpt(self, productrecpt_page, delete_data, expected_result):
        """测试产品入库删除功能 - 数据驱动"""
        productrecpt_page.delete_productrecpt(delete_data)
        actual_result = productrecpt_page.is_productrecpt_exists(delete_data)
        assert actual_result == expected_result
