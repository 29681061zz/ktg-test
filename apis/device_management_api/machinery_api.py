from typing import Dict, Any
from apis.base_api import BaseApi

class MachineryAPI(BaseApi):
    """检测项设置API客户端"""
    def __init__(self, base_url: str = None):
        """初始化检测项设置API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_machinery(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索检测项"""
        endpoint = "/mes/dv/machinery/list"
        params = {"machineryCode": search_data["machineryCode"]}
        return self.client.get(endpoint, params=params)

    def add_machinery(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        endpoint="/mes/dv/machinery"
        return self.client.post(endpoint, json_data=edit_data)

    def edit_machinery(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改检测项信息"""
        endpoint = "/mes/dv/machinery"
        search_response = self.search_machinery(edit_data)
        edit_data["machineryId"]= search_response['data'][0]['machineryId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_machinery(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除检测项"""
        endpoint = "/mes/dv/machinery"
        # 通过编码搜索获取检测项ID
        search_response = self.search_machinery(delete_data)
        machinery_id = search_response['data'][0]['machineryId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{machinery_id}")

