import ddddocr
from typing import Dict, Any, Optional
from apis.base_api import BaseApi

class AuthApi(BaseApi):
    """认证API"""
    def __init__(self, base_url: Optional[str] = None):
        if base_url is None:
            base_url = "/prod-api"
        super().__init__(base_url)

        self.ocr = ddddocr.DdddOcr(show_ad=False)

    def login(self, username: str, password: str, max_retries: int = 10) -> Dict[str, Any]:
        """
        自动处理验证码的登录流程
        """
        retry_count = 0
        while retry_count < max_retries:
            # 1. 获取验证码
            captcha_response = self.get_captcha()
            if captcha_response.get('status_code') != 200:
                return captcha_response

            captcha_data = captcha_response.get('data', {})
            captcha_img = captcha_data.get('img')
            captcha_key = captcha_data.get('uuid')

            if not captcha_img or not captcha_key:
                return {"error": "无法获取验证码"}

            # 2. 识别验证码
            captcha_text = self.recognize_captcha(captcha_img)
            if not captcha_text:
                retry_count += 1
                continue

            # 3. 计算验证码
            captcha_result = self.calculate_captcha(captcha_text)
            if captcha_result is None:
                retry_count += 1
                continue

            # 4. 登录
            login_data = {
                "username": username,
                "password": password,
                "code": str(captcha_result),
                "uuid": captcha_key
            }

            login_response = self.client.post("/login", json_data=login_data)

            # 5. 检查登录结果
            if login_response.get('status_code') == 200:
                response_data = login_response.get('data', {})
                if response_data.get('code') == 200:
                    token = self._extract_token(login_response)
                    if token:
                        self.set_auth_token(token)
                        return login_response
                else:
                    if "验证码" in response_data.get('msg', ''):
                        retry_count += 1
                        continue
                    else:
                        return login_response

        return {"error": f"登录失败，已达最大重试次数 {max_retries}"}

    def _extract_token(self, response: Dict[str, Any]) -> Optional[str]:
        """
        从响应中提取token
        """
        data = response.get('data', {})

        token_fields = ['access_token', 'token', 'auth_token', 'accessToken']
        for field in token_fields:
            if field in data:
                return data[field]

        if 'result' in data and isinstance(data['result'], dict):
            for field in token_fields:
                if field in data['result']:
                    return data['result'][field]

        return None

    def get_captcha(self) -> Dict[str, Any]:
        """
        获取验证码
        """
        return self.client.get("/captchaImage")

    def recognize_captcha(self, captcha_img_base64: str) -> str:
        """
        识别验证码图片
        """
        try:
            if ',' in captcha_img_base64:
                base64_data = captcha_img_base64.split(",")[1]
            else:
                base64_data = captcha_img_base64

            return self.ocr.classification(base64_data)
        except Exception:
            return ""

    def calculate_captcha(self, expression: str):
        """
        计算验证码表达式
        """
        try:
            char_to_num = {'q': 0, 't': 1, 'l': 1, 'z': 2}
            num1 = char_to_num.get(expression[0], expression[0])
            num2 = char_to_num.get(expression[2], expression[2])

            try:
                num1 = int(num1)
                num2 = int(num2)
            except ValueError:
                return None

            if len(expression) == 2:
                return num1 - num2

            op_map = {
                '+': '+', 't': '+',
                '-': '-', 'r': '-',
                '*': '*', 'x': '*', 'k': '*',
                '/': '//', 'l': '//'
            }
            operator = op_map.get(expression[1])
            if not operator:
                return num1 - num2

            return eval(f"{num1}{operator}{num2}")

        except (ValueError, IndexError, ZeroDivisionError, SyntaxError):
            return None