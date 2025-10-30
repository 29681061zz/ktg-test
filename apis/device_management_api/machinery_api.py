from typing import Dict, Any
from apis.base_api import BaseApi

class MachineryAPI(BaseApi):
    """设备台账API客户端"""
    def __init__(self, base_url: str = None):
        """初始化设备台账API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_machinery(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索设备台账"""
        endpoint = "/mes/dv/machinery/list"
        return self.client.get(endpoint, params=search_data)

    def add_machinery(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        endpoint="/mes/dv/machinery"
        return self.client.post(endpoint, json_data=edit_data)

    def edit_machinery(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改设备台账信息"""
        endpoint = "/mes/dv/machinery"
        search_response = self.search_machinery({"machineryCode": edit_data["machineryCode"]})
        edit_data["machineryId"]= search_response['data'][0]['machineryId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_machinery(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除设备台账"""
        endpoint = "/mes/dv/machinery"
        # 通过编码搜索获取设备台账ID
        search_response = self.search_machinery(delete_data)
        machinery_id = search_response['data'][0]['machineryId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{machinery_id}")

