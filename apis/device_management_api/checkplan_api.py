from typing import Dict, Any
from apis.base_api import BaseApi

class CheckplanAPI(BaseApi):
    """点检保养方案API客户端"""
    def __init__(self, base_url: str = None):
        """初始化点检保养方案API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_checkplan(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索方案"""
        endpoint = "/mes/dv/checkplan/list"
        params = {"planCode": search_data["planCode"]}
        return self.client.get(endpoint, params=params)

    def add_checkplan(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        endpoint="/mes/dv/checkplan"
        return self.client.post(endpoint, json_data=edit_data)

    def edit_checkplan(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改方案信息"""
        endpoint = "/mes/dv/checkplan"
        search_response = self.search_checkplan(edit_data)
        edit_data["planId"]= search_response['data'][0]['planId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_checkplan(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除方案"""
        endpoint = "/mes/dv/checkplan"
        # 通过编码搜索获取方案ID
        search_response = self.search_checkplan(delete_data)
        checkplan_id = search_response['data'][0]['planId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{checkplan_id}")

