import allure
import pytest
from utils.assertion import ApiAssertion
from utils.data_manager import DataManager

@pytest.mark.api
@allure.feature("点检保养方案")
class TestCheckplan:
    """点检保养方案测试 - 数据驱动"""
    @allure.story("新增功能")
    @DataManager.device('checkplan', 'add_cases', ['add_data', 'expected_status'])
    def test_add_checkplan(self, authenticated_checkplan_api,add_data, expected_status):
        # 创建方案
        response = authenticated_checkplan_api.add_checkplan(add_data)
        # 检查API调用成功
        (ApiAssertion.assert_status_code(response['status_code'],200)
         .assert_business_code(response['raw']['code'], expected_status))
        # 只有业务成功的情况下才进行搜索验证
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_checkplan_api.search_checkplan(add_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], add_data))

    @allure.story("搜索功能")
    @DataManager.device('checkplan', 'search_cases', ['search_data', 'expected_status'])
    def test_search_checkplan(self, authenticated_checkplan_api,search_data, expected_status):
        """测试方案搜索"""
        response = authenticated_checkplan_api.search_checkplan(search_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        if response['data']: # 只有存在数据时才进行字段匹配断言
            ApiAssertion.assert_all_fields_match(response['data'][0], search_data)

    @allure.story("修改功能")
    @DataManager.device('checkplan', 'edit_cases', ['edit_data', 'expected_status'])
    def test_edit_checkplan(self, authenticated_checkplan_api,edit_data, expected_status):
        # 修改方案
        response = authenticated_checkplan_api.edit_checkplan(edit_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status))
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_checkplan_api.search_checkplan(edit_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], edit_data))

    @allure.story("删除功能")
    @DataManager.device('checkplan', 'delete_cases', ['delete_data', 'expected_status'])
    def test_delete_checkplan(self, authenticated_checkplan_api, delete_data, expected_status):
        """测试删除方案"""
        # 先确保方案存在
        search_response = authenticated_checkplan_api.search_checkplan(delete_data)
        assert len(search_response['data']) > 0, "删除前方案应该存在"
        # 删除方案
        response = authenticated_checkplan_api.delete_checkplan(delete_data)
        # 检查删除操作成功
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['data']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        # 验证方案确实被删除
        if response['raw']['code'] == 200:
            post_search = authenticated_checkplan_api.search_checkplan(delete_data)
            assert len(post_search['data']) == 0, "删除后方案应该不存在"
