import allure
import pytest
from utils.assertion import ApiAssertion
from utils.data_manager import DataManager

@pytest.mark.api
@allure.feature("质检方案")
class TestQctemplate:
    """质检方案测试 - 数据驱动"""
    @allure.story("新增功能")
    @DataManager.qc('qctemplate', 'add_cases', ['add_data', 'expected_status'])
    def test_add_qctemplate(self, authenticated_qctemplate_api,add_data, expected_status):
        # 创建质检方案
        response = authenticated_qctemplate_api.add_qctemplate(add_data)
        # 检查API调用成功
        (ApiAssertion.assert_status_code(response['status_code'],200)
         .assert_business_code(response['raw']['code'], expected_status))
        # 只有业务成功的情况下才进行搜索验证
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_qctemplate_api.search_qctemplate(add_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], add_data))

    @allure.story("搜索功能")
    @DataManager.qc('qctemplate', 'search_cases', ['search_data', 'expected_status'])
    def test_search_qctemplate(self, authenticated_qctemplate_api,search_data, expected_status):
        """测试质检方案搜索"""
        response = authenticated_qctemplate_api.search_qctemplate(search_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status)
         .assert_json_contains(response, 'data')
         .assert_all_fields_match(response['data'][0], search_data))

    @allure.story("修改功能")
    @DataManager.qc('qctemplate', 'edit_cases', ['edit_data', 'expected_status'])
    def test_edit_qctemplate(self, authenticated_qctemplate_api,edit_data, expected_status):
        # 修改质检方案
        response = authenticated_qctemplate_api.edit_qctemplate(edit_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status))
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_qctemplate_api.search_qctemplate(edit_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], edit_data))

    @allure.story("删除功能")
    @DataManager.qc('qctemplate', 'delete_cases', ['delete_data', 'expected_status'])
    def test_delete_qctemplate(self, authenticated_qctemplate_api, delete_data, expected_status):
        """测试删除质检方案"""
        # 先确保质检方案存在
        search_response = authenticated_qctemplate_api.search_qctemplate(delete_data)
        assert len(search_response['data']) > 0, "删除前质检方案应该存在"
        # 删除质检方案
        response = authenticated_qctemplate_api.delete_qctemplate(delete_data)
        # 检查删除操作成功
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['data']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        # 验证质检方案确实被删除
        if response['raw']['code'] == 200:
            post_search = authenticated_qctemplate_api.search_qctemplate(delete_data)
            assert len(post_search['data']) == 0, "删除后质检方案应该不存在"
