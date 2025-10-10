from typing import Dict, Any
from apis.base_api import BaseApi

class MachineryTypeAPI(BaseApi):
    """检测项设置API客户端"""
    def __init__(self, base_url: str = None):
        """初始化检测项设置API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_machinerytype(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索检测项"""
        endpoint = "/mes/dv/machinerytype/list"
        params = {"machineryTypeName": search_data["machineryTypeName"]}
        return self.client.get(endpoint, params=params)

    def edit_machinerytype(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改检测项信息"""
        endpoint = "/mes/dv/machinerytype"
        search_response = self.search_machinerytype(edit_data)
        edit_data["machineryTypeId"]= search_response['data'][0]['machineryTypeId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_machinerytype(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除检测项"""
        endpoint = "/mes/dv/machinerytype"
        # 通过编码搜索获取检测项ID
        search_response = self.search_machinerytype(delete_data)
        machinerytype_id = search_response['data'][0]['machineryTypeId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{machinerytype_id}")

