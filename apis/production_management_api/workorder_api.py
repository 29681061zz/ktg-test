from typing import Dict, Any
from apis.base_api import BaseApi

class WorkOrderAPI(BaseApi):
    """生产工单API客户端"""

    def __init__(self, base_url: str = None):
        """初始化工序API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_workorder(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索工序"""
        endpoint = "/mes/pro/workorder/list"
        # 添加搜索条件
        return self.client.get(endpoint, params=search_data)
    
    def add_workorder(self, workorder_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加工序"""
        endpoint = "/mes/pro/workorder"
        return self.client.post(endpoint, json_data=workorder_data)