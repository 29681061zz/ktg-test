from typing import Dict, Any
from apis.base_api import BaseApi

class QctemplateAPI(BaseApi):
    """质检方案API客户端"""
    def __init__(self, base_url: str = None):
        """初始化质检方案API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_qctemplate(self,search_data:Dict[str, Any],page_num: int = 1,page_size: int = 10) -> Dict[str, Any]:
        """搜索质检方案"""
        endpoint = "/mes/qc/qctemplate/list"
        params = {"pageNum": page_num, "pageSize": page_size, "templateCode": search_data["templateCode"]}
        return self.client.get(endpoint, params=params)

    def add_qctemplate(self, qctemplate_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加质检方案"""
        endpoint = "/mes/qc/qctemplate"
        return self.client.post(endpoint, json_data=qctemplate_data)

    def edit_qctemplate(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改质检方案信息"""
        endpoint = "/mes/qc/qctemplate"
        search_response = self.search_qctemplate(edit_data)
        edit_data["templateId"]= search_response['data'][0]['templateId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_qctemplate(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除质检方案"""
        endpoint = "/mes/qc/qctemplate"
        # 通过编码搜索获取质检方案ID
        search_response = self.search_qctemplate(delete_data)
        qctemplate_id = search_response['data'][0]['templateId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{qctemplate_id}")

