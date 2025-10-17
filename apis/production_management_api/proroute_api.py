from typing import Dict, Any
from apis.base_api import BaseApi

class ProrouteAPI(BaseApi):
    """工艺流程API客户端"""
    def __init__(self, base_url: str = None):
        """初始化工艺流程API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_proroute(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索工艺流程"""
        endpoint = "/mes/pro/proroute/list"
        return self.client.get(endpoint, params=search_data)

    def add_proroute(self, proroute_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加工艺流程"""
        endpoint = "/mes/pro/proroute"
        return self.client.post(endpoint, json_data=proroute_data)

    def edit_proroute(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改工艺流程信息"""
        endpoint = "/mes/pro/proroute"
        search_response = self.search_proroute({"routeCode": edit_data["routeCode"]})
        edit_data["routeId"]= search_response['data'][0]['routeId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_proroute(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除工艺流程"""
        endpoint = "/mes/pro/proroute"
        # 通过编码搜索获取工艺流程ID
        search_response = self.search_proroute(delete_data)
        proroute_id = search_response['data'][0]['routeId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{proroute_id}")

