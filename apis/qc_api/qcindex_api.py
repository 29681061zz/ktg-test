from typing import Dict, Any
from apis.base_api import BaseApi

class QcindexAPI(BaseApi):
    """检测项设置API客户端"""
    def __init__(self, base_url: str = None):
        """初始化检测项设置API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_qcindex(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索检测项"""
        endpoint = "/mes/qc/qcindex/list"
        return self.client.get(endpoint, params=search_data)

    def add_qcindex(self, qcindex_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加检测项"""
        endpoint = "/mes/qc/qcindex"
        return self.client.post(endpoint, json_data=qcindex_data)

    def edit_qcindex(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改检测项信息"""
        endpoint = "/mes/qc/qcindex"
        search_response = self.search_qcindex({"indexCode": edit_data["indexCode"]})
        edit_data["indexId"]= search_response['data'][0]['indexId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_qcindex(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除检测项"""
        endpoint = "/mes/qc/qcindex"
        # 通过编码搜索获取检测项ID
        search_response = self.search_qcindex(delete_data)
        qcindex_id = search_response['data'][0]['indexId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{qcindex_id}")

