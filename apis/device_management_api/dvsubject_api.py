from typing import Dict, Any
from apis.base_api import BaseApi

class DvsubjectAPI(BaseApi):
    """点检保养项目API客户端"""
    def __init__(self, base_url: str = None):
        """初始化点检保养项目API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_dvsubject(self,search_data:Dict[str, Any]) -> Dict[str, Any]:
        """搜索项目"""
        endpoint = "/mes/dv/dvsubject/list"
        params = {"subjectCode": search_data["subjectCode"]}
        return self.client.get(endpoint, params=params)

    def add_dvsubject(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        endpoint="/mes/dv/dvsubject"
        return self.client.post(endpoint, json_data=edit_data)

    def edit_dvsubject(self,edit_data: Dict[str, Any]) -> Dict[str, Any]:
        """修改项目信息"""
        endpoint = "/mes/dv/dvsubject"
        search_response = self.search_dvsubject(edit_data)
        edit_data["subjectId"]= search_response['data'][0]['subjectId']
        return self.client.put(endpoint, json_data=edit_data)

    def delete_dvsubject(self, delete_data: Dict[str, Any]) -> Dict[str, Any]:
        """删除项目"""
        endpoint = "/mes/dv/dvsubject"
        # 通过编码搜索获取项目ID
        search_response = self.search_dvsubject(delete_data)
        dvsubject_id = search_response['data'][0]['subjectId']
        # 发送删除请求
        return self.client.delete(f"{endpoint}/{dvsubject_id}")

