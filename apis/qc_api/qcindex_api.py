from typing import Dict, Any
from apis.base_api import BaseApi

class QcindexAPI(BaseApi):
    """工艺流程API客户端"""
    def __init__(self, base_url: str = None):
        """初始化工艺流程API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_qcindex(self,search_data:Dict[str, Any],page_num: int = 1,page_size: int = 10) -> Dict[str, Any]:
        """搜索工艺流程"""
        endpoint = "/mes/qc/qcindex/list"
        params = {"pageNum": page_num, "pageSize": page_size, "indexCode": search_data["indexCode"]}
        return self.client.get(endpoint, params=params)

    def add_qcindex(self, qcindex_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加工艺流程"""
        endpoint = "/mes/qc/qcindex"
        return self.client.post(endpoint, json_data=qcindex_data)

    def edit_qcindex(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改工艺流程信息"""
        endpoint = "/mes/qc/qcindex"
        search_response = self.search_qcindex(edit_data)
        edit_data["indexId"]= search_response['data'][0]['indexId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_qcindex(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除工艺流程"""
        endpoint = "/mes/qc/qcindex"
        # 通过编码搜索获取工艺流程ID
        search_response = self.search_qcindex(delete_data)
        qcindex_id = search_response['data'][0]['indexId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{qcindex_id}")

