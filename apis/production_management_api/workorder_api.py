from typing import Dict, Any
from apis.base_api import BaseApi
from configs.settings import Config


class WorkOrderAPI(BaseApi):
    """工单管理API客户端"""

    def __init__(self, base_url: str = None):
        """
        初始化工单API客户端
        """
        if base_url is None:
            base_url = f"{Config.API_BASE_URL}/production"
        super().__init__(base_url)

    def create_workorder(self, workorder_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        创建工单

        Args:
            workorder_data: 工单数据
                - workorder_no: 工单编号
                - product_code: 产品编码
                - plan_quantity: 计划数量
                - priority: 优先级
                - planned_start_time: 计划开始时间
                - planned_end_time: 计划结束时间

        Returns:
            包含响应数据的字典
        """
        endpoint = "/workorders"
        return self.client.post(endpoint, json_data=workorder_data)