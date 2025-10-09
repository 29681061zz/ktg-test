from typing import Dict, Any
from apis.base_api import BaseApi

class ProcessAPI(BaseApi):
    """工序设置API客户端"""
    def __init__(self, base_url: str = None):
        """初始化工序API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_process(self,search_data:Dict[str, Any],page_num: int = 1,page_size: int = 10) -> Dict[str, Any]:
        """搜索工序"""
        endpoint = "/mes/pro/process/list"
        params = {"pageNum": page_num, "pageSize": page_size, "processCode": search_data["processCode"]}
        return self.client.get(endpoint, params=params)

    def add_process(self, process_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加工序"""
        endpoint = "/mes/pro/process"
        return self.client.post(endpoint, json_data=process_data)

    def edit_process(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改工序信息"""
        endpoint = "/mes/pro/process"
        search_response = self.search_process(edit_data)
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

