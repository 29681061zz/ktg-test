import allure
import pytest
from utils.assertion import ApiAssertion
from utils.data_manager import DataManager

@pytest.mark.api
@allure.feature("来料检验")
class TestIqc:
    """来料检验测试 - 数据驱动"""
    @allure.story("新增功能")
    @DataManager.qc('iqc', 'add_cases', ['add_data', 'expected_status'])
    def test_add_iqc(self, authenticated_iqc_api,add_data, expected_status):
        # 创建检测项
        response = authenticated_iqc_api.add_iqc(add_data)
        # 检查API调用成功
        (ApiAssertion.assert_status_code(response['status_code'],200)
         .assert_business_code(response['raw']['code'], expected_status))
        # 只有业务成功的情况下才进行搜索验证
        if response['raw']['code'] == 200:  # 业务成功
            # 重新搜索验证数据创建
            search_response = authenticated_iqc_api.search_iqc(add_data)
            # 检查搜索到数据且字段按测试数据全匹配
            (ApiAssertion.assert_all_fields_match(search_response['data'][0], add_data))

    @allure.story("搜索功能")
    @DataManager.qc('iqc', 'search_cases', ['search_data', 'expected_status'])
    def test_search_iqc(self, authenticated_iqc_api,search_data, expected_status):
        """测试检测项搜索"""
        response = authenticated_iqc_api.search_iqc(search_data)
        (ApiAssertion.assert_status_code(response['status_code'], 200)
         .assert_business_code(response['raw']['code'], expected_status)
         .assert_json_contains(response, 'data'))
        if response['data']:  # 只有存在数据时才进行字段匹配断言
            ApiAssertion.assert_all_fields_match(response['data'][0], search_data)

