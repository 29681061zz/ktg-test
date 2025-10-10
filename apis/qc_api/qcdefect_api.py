from typing import Dict, Any
from apis.base_api import BaseApi

class QcdefectAPI(BaseApi):
    """工艺流程API客户端"""
    def __init__(self, base_url: str = None):
        """初始化工艺流程API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_qcdefect(self,search_data:Dict[str, Any],page_num: int = 1,page_size: int = 10) -> Dict[str, Any]:
        """搜索工艺流程"""
        endpoint = "/mes/qc/qcdefect/list"
        params = {"pageNum": page_num, "pageSize": page_size, "defectName": search_data["defectName"]}
        return self.client.get(endpoint, params=params)

    def add_qcdefect(self, qcdefect_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加工艺流程"""
        endpoint = "/mes/qc/qcdefect"
        return self.client.post(endpoint, json_data=qcdefect_data)

    def edit_qcdefect(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改工艺流程信息"""
        endpoint = "/mes/qc/qcdefect"
        search_response = self.search_qcdefect(edit_data)
        edit_data["defectId"]= search_response['data'][0]['defectId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_qcdefect(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除工艺流程"""
        endpoint = "/mes/qc/qcdefect"
        # 通过编码搜索获取工艺流程ID
        search_response = self.search_qcdefect(delete_data)
        qcdefect_id = search_response['data'][0]['defectId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{qcdefect_id}")

