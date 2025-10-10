from typing import Dict, Any
from apis.base_api import BaseApi

class IqcAPI(BaseApi):
    """来料检验API客户端"""
    def __init__(self, base_url: str = None):
        """初始化来料检验API客户端"""
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

    def search_iqc(self,search_data:Dict[str, Any],page_num: int = 1,page_size: int = 10) -> Dict[str, Any]:
        """搜索来料检验"""
        endpoint = "/mes/qc/iqc/list"
        params = {"pageNum": page_num, "pageSize": page_size, "iqcCode": search_data["iqcCode"]}
        return self.client.get(endpoint, params=params)

    def add_iqc(self, iqc_data: Dict[str, Any]) -> Dict[str, Any]:
        """添加来料检验"""
        endpoint = "/mes/qc/iqc"
        return self.client.post(endpoint, json_data=iqc_data)


