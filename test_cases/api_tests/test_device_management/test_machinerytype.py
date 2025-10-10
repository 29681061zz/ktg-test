import allure
import pytest
from utils.assertion import ApiAssertion
from utils.data_manager import DataManager

@pytest.mark.api
@allure.feature("设备类型设置")
class TestMachineryType:
    """设备类型设置测试 - 数据驱动"""
    @allure.story("搜索功能")
    @DataManager.device('machinerytype', 'search_cases', ['search_data', 'expected_status'])
    def test_search_machinerytype(self, authenticated_machinerytype_api,search_data, expected_status):
        """测试设备类型搜索"""
        response = authenticated_machinerytype_api.search_machinerytype(search_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status)
         .assert_json_contains(response, 'data')
         .assert_all_fields_match(response['data'][0], search_data))

    @allure.story("修改功能")
    @DataManager.device('machinerytype', 'edit_cases', ['edit_data', 'expected_status'])
    def test_edit_machinerytype(self, authenticated_machinerytype_api,edit_data, expected_status):
        # 修改设备类型
        response = authenticated_machinerytype_api.edit_machinerytype(edit_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status))
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_machinerytype_api.search_machinerytype(edit_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], edit_data))

    @allure.story("删除功能")
    @DataManager.device('machinerytype', 'delete_cases', ['delete_data', 'expected_status'])
    def test_delete_machinerytype(self, authenticated_machinerytype_api, delete_data, expected_status):
        """测试删除设备类型"""
        # 先确保设备类型存在
        search_response = authenticated_machinerytype_api.search_machinerytype(delete_data)
        assert len(search_response['data']) > 0, "删除前设备类型应该存在"
        # 删除设备类型
        response = authenticated_machinerytype_api.delete_machinerytype(delete_data)
        # 检查删除操作成功
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['data']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        # 验证设备类型确实被删除
        if response['raw']['code'] == 200:
            post_search = authenticated_machinerytype_api.search_machinerytype(delete_data)
            assert len(post_search['data']) == 0, "删除后设备类型应该不存在"
