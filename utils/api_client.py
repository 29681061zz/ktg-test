import requests
import json
import logging
from typing import Optional, Dict, Any

class ApiClient:
    """API请求客户端基类"""

    def __init__(self, base_url: str = None, timeout: int = 10):
        self.session = requests.Session()
        self.base_url = base_url
        self.timeout = timeout
        self.logger = logging.getLogger('api_test')
        # 必要：设置基础请求头
        self.session.headers.update({
            'Content-Type': 'application/json; charset=utf-8'
        })

    def _full_url(self, endpoint: str) -> str:
        """构建完整URL"""
        return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"

    def _log_request(self, method: str, url: str, json_data: Dict = None):
        """基础请求日志"""
        log_message = f"🚀 发送请求: {method.upper()} {url}"
        if json_data:
            log_message += f"\n📦 请求体: {json.dumps(json_data, ensure_ascii=False)}"
        self.logger.info(log_message)

    def _log_response(self, response: requests.Response):
        """基础响应日志"""
        self.logger.info(f"📨 收到响应: 状态码={response.status_code}")

    def request(self, method: str, endpoint: str,
                json_data: Optional[Dict] = None,
                **kwargs) -> Dict[str, Any]:
        """统一请求方法 """
        url = self._full_url(endpoint)

        # 记录请求
        self._log_request(method, url, json_data)

        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                json=json_data,
                timeout=self.timeout,
                **kwargs
            )

            # 记录响应
            self._log_response(response)

            # 处理响应
            try:
                response_data = response.json() if response.content else {}
            except json.JSONDecodeError:
                response_data = {'raw_text': response.text}

            # 智能提取业务数据
            business_data = self._extract_business_data(response_data, endpoint)

            return {
                'success': 200 <= response.status_code < 300,
                'status_code': response.status_code,
                'data': business_data,  # 统一业务数据入口
                'message': response_data.get('msg', ''),
                'elapsed': response.elapsed.total_seconds() * 1000,
                'raw': response_data,  # 保留原始响应供特殊需求
            }

        except requests.exceptions.Timeout:
            self.logger.error(f"请求超时: {url}")
            raise
        except requests.exceptions.ConnectionError:
            self.logger.error(f"连接错误: {url}")
            raise
        except requests.exceptions.RequestException as e:
            self.logger.error(f"请求异常: {url}, 错误: {str(e)}")
            raise

    def _extract_business_data(self, response_data: Dict[str, Any], endpoint: str) -> Any:
        """智能提取业务数据"""
        # 1. 列表接口：直接返回 rows 数组
        if 'rows' in response_data:
            return response_data['rows']  # 直接返回数组，方便直接遍历
        # 2. 详情接口：直接返回 data 中的内容
        if 'data' in response_data and response_data['data'] is not None:
            return response_data['data']  # 直接返回对象
        # 3. 其他情况返回原始数据
        return response_data

    # 必要：HTTP方法快捷方式
    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        return self.request('GET', endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json_data: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        return self.request('POST', endpoint, json_data=json_data, **kwargs)

    def put(self, endpoint: str, json_data: Optional[Dict] = None, **kwargs) -> Dict[str, Any]:
        return self.request('PUT', endpoint, json_data=json_data, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        return self.request('DELETE', endpoint, **kwargs)

    def set_auth_token(self, token: str):
        """设置认证令牌 """
        self.session.headers.update({
            'Authorization': f'Bearer {token}'
        })
        self.logger.info("✅ 认证令牌已设置")