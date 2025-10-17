import allure
import pytest
from utils.assertion import ApiAssertion
from utils.data_manager import DataManager

@pytest.mark.api
@allure.feature("常见缺陷")
class TestQcdefect:
    """常见缺陷测试 - 数据驱动"""
    @allure.story("新增功能")
    @DataManager.qc('qcdefect', 'add_cases', ['add_data', 'expected_status'])
    def test_add_qcdefect(self, authenticated_qcdefect_api,add_data, expected_status):
        # 创建常见缺陷
        response = authenticated_qcdefect_api.add_qcdefect(add_data)
        # 检查API调用成功
        (ApiAssertion.assert_status_code(response['status_code'],200)
         .assert_business_code(response['raw']['code'], expected_status))
        # 只有业务成功的情况下才进行搜索验证
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_qcdefect_api.search_qcdefect(add_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], add_data))

    @allure.story("搜索功能")
    @DataManager.qc('qcdefect', 'search_cases', ['search_data', 'expected_status'])
    def test_search_qcdefect(self, authenticated_qcdefect_api,search_data, expected_status):
        """测试常见缺陷搜索"""
        response = authenticated_qcdefect_api.search_qcdefect(search_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        if response['data']:  # 只有存在数据时才进行字段匹配断言
            ApiAssertion.assert_all_fields_match(response['data'][0], search_data)

    @allure.story("修改功能")
    @DataManager.qc('qcdefect', 'edit_cases', ['edit_data', 'expected_status'])
    def test_edit_qcdefect(self, authenticated_qcdefect_api,edit_data, expected_status):
        # 修改常见缺陷
        response = authenticated_qcdefect_api.edit_qcdefect(edit_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status))
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_qcdefect_api.search_qcdefect(edit_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], edit_data))

    @allure.story("删除功能")
    @DataManager.qc('qcdefect', 'delete_cases', ['delete_data', 'expected_status'])
    def test_delete_qcdefect(self, authenticated_qcdefect_api, delete_data, expected_status):
        """测试删除常见缺陷"""
        # 先确保常见缺陷存在
        search_response = authenticated_qcdefect_api.search_qcdefect(delete_data)
        assert len(search_response['data']) > 0, "删除前常见缺陷应该存在"
        # 删除常见缺陷
        response = authenticated_qcdefect_api.delete_qcdefect(delete_data)
        # 检查删除操作成功
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['data']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        # 验证常见缺陷确实被删除
        if response['raw']['code'] == 200:
            post_search = authenticated_qcdefect_api.search_qcdefect(delete_data)
            assert len(post_search['data']) == 0, "删除后常见缺陷应该不存在"
