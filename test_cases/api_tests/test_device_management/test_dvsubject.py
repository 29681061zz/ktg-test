import allure
import pytest
from utils.assertion import ApiAssertion
from utils.data_manager import DataManager

@pytest.mark.api
@allure.feature("点检保养")
class TestDvsubject:
    """点检保养测试 - 数据驱动"""
    @allure.story("新增功能")
    @DataManager.device('dvsubject', 'add_cases', ['add_data', 'expected_status'])
    def test_add_dvsubject(self, authenticated_dvsubject_api,add_data, expected_status):
        # 创建点检保养
        response = authenticated_dvsubject_api.add_dvsubject(add_data)
        # 检查API调用成功
        (ApiAssertion.assert_status_code(response['status_code'],200)
         .assert_business_code(response['raw']['code'], expected_status))
        # 只有业务成功的情况下才进行搜索验证
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_dvsubject_api.search_dvsubject(add_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], add_data))

    @allure.story("搜索功能")
    @DataManager.device('dvsubject', 'search_cases', ['search_data', 'expected_status'])
    def test_search_dvsubject(self, authenticated_dvsubject_api,search_data, expected_status):
        """测试点检保养搜索"""
        response = authenticated_dvsubject_api.search_dvsubject(search_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status)
         .assert_json_contains(response, 'data')
         .assert_all_fields_match(response['data'][0], search_data))

    @allure.story("修改功能")
    @DataManager.device('dvsubject', 'edit_cases', ['edit_data', 'expected_status'])
    def test_edit_dvsubject(self, authenticated_dvsubject_api,edit_data, expected_status):
        # 修改点检保养
        response = authenticated_dvsubject_api.edit_dvsubject(edit_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status))
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_dvsubject_api.search_dvsubject(edit_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], edit_data))

    @allure.story("删除功能")
    @DataManager.device('dvsubject', 'delete_cases', ['delete_data', 'expected_status'])
    def test_delete_dvsubject(self, authenticated_dvsubject_api, delete_data, expected_status):
        """测试删除点检保养"""
        # 先确保点检保养存在
        search_response = authenticated_dvsubject_api.search_dvsubject(delete_data)
        assert len(search_response['data']) > 0, "删除前点检保养应该存在"
        # 删除点检保养
        response = authenticated_dvsubject_api.delete_dvsubject(delete_data)
        # 检查删除操作成功
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['data']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        # 验证点检保养确实被删除
        if response['raw']['code'] == 200:
            post_search = authenticated_dvsubject_api.search_dvsubject(delete_data)
            assert len(post_search['data']) == 0, "删除后点检保养应该不存在"
