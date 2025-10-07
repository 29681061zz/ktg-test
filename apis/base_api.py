from utils.api_client import ApiClient
from configs.settings import Config
from typing import Optional


class BaseApi:
    """业务API基类 - 改进版本"""
    def __init__(self, base_url: Optional[str] = None):
        """
        初始化业务API
        """
        # URL处理逻辑
        if base_url:
            if base_url.startswith('/'):
                # 相对路径，拼接基础URL
                final_url = f"{Config.API_BASE_URL.rstrip('/')}{base_url}"
            else:
                # 绝对URL，直接使用
                final_url = base_url
        else:
            final_url = Config.API_BASE_URL

        self.client = ApiClient(final_url)

    def set_auth_token(self, token: str):
        """设置认证令牌"""
        self.client.set_auth_token(token)
