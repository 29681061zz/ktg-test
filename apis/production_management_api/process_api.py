from typing import Dict, Any
from apis.base_api import BaseApi

class ProcessAPI(BaseApi):
    """工序设置API客户端"""
    def __init__(self, base_url: str = None):
        """初始化工序API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_process(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索工序"""
        endpoint = "/mes/pro/process/list"
        return self.client.get(endpoint, params=search_data)

    def add_process(self, process_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加工序"""
        endpoint = "/mes/pro/process"
        return self.client.post(endpoint, json_data=process_data)

    def edit_process(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改工序信息"""
        endpoint = "/mes/pro/process"
        search_response = self.search_process({"processCode": edit_data["processCode"]})
        edit_data["processId"]= search_response['data'][0]['processId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_process(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除工序"""
        endpoint = "/mes/pro/process"
        # 通过编码搜索获取工序ID
        search_response = self.search_process(delete_data)
        process_id = search_response['data'][0]['processId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{process_id}")

