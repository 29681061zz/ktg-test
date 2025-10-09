import allure
import pytest
from utils.assertion import ApiAssertion
from utils.data_manager import DataManager

@pytest.mark.api
@allure.feature("工序设置")
class TestProcess:
    """工序设置测试 - 数据驱动"""
    @allure.story("新增功能")
    @DataManager.production('process', 'add_cases', ['add_data', 'expected_status'])
    def test_add_process(self, authenticated_process_api,add_data, expected_status):
        # 创建工序
        response = authenticated_process_api.add_process(add_data)
        # 检查API调用成功
        (ApiAssertion.assert_status_code(response['status_code'],200)
         .assert_business_code(response['raw']['code'], expected_status))
        # 只有业务成功的情况下才进行搜索验证
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_process_api.search_process(add_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], add_data))

    @allure.story("搜索功能")
    @DataManager.production('process', 'search_cases', ['search_data', 'expected_status'])
    def test_search_process(self, authenticated_process_api,search_data, expected_status):
        """测试工序搜索"""
        response = authenticated_process_api.search_process(search_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status)
         .assert_json_contains(response, 'data')
         .assert_all_fields_match(response['data'][0], search_data))

    @allure.story("修改功能")
    @DataManager.production('process', 'edit_cases', ['edit_data', 'expected_status'])
    def test_edit_process(self, authenticated_process_api,edit_data, expected_status):
        # 修改工序
        response = authenticated_process_api.edit_process(edit_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status))
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_process_api.search_process(edit_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], edit_data))

    @allure.story("删除功能")
    @DataManager.production('process', 'delete_cases', ['delete_data', 'expected_status'])
    def test_delete_process(self, authenticated_process_api, delete_data, expected_status):
        """测试删除工序"""
        # 先确保工序存在
        search_response = authenticated_process_api.search_process(delete_data)
        assert len(search_response['data']) > 0, "删除前工序应该存在"
        # 删除工序
        response = authenticated_process_api.delete_process(delete_data)
        # 检查删除操作成功
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['data']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        # 验证工序确实被删除
        if response['raw']['code'] == 200:
            post_search = authenticated_process_api.search_process(delete_data)
            assert len(post_search['data']) == 0, "删除后工序应该不存在"
