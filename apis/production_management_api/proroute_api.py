from typing import Dict, Any
from apis.base_api import BaseApi

class ProrouteAPI(BaseApi):
    """工序设置API客户端"""
    def __init__(self, base_url: str = None):
        """初始化工序API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_proroute(self,search_data:Dict[str, Any],page_num: int = 1,page_size: int = 10) -> Dict[str, Any]:
        """搜索工序"""
        endpoint = "/mes/pro/proroute/list"
        params = {"pageNum": page_num, "pageSize": page_size, "routeCode": search_data["routeCode"]}
        return self.client.get(endpoint, params=params)

    def add_proroute(self, proroute_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加工序"""
        endpoint = "/mes/pro/proroute"
        return self.client.post(endpoint, json_data=proroute_data)

    def edit_proroute(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改工序信息"""
        endpoint = "/mes/pro/proroute"
        search_response = self.search_proroute(edit_data)
        edit_data["routeId"]= search_response['data'][0]['routeId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_proroute(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除工序"""
        endpoint = "/mes/pro/proroute"
        # 通过编码搜索获取工序ID
        search_response = self.search_proroute(delete_data)
        proroute_id = search_response['data'][0]['routeId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{proroute_id}")

