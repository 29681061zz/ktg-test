import pytest
from typing import Generator
from apis.auth_api import AuthApi
from configs.settings import Config
from utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="session")
def auth_api():
    """提供认证API实例"""
    return AuthApi()

@pytest.fixture(scope="session")
def api_token(auth_api) -> Generator[str, None, None]:
    """提供API token"""
    # setup: 登录获取token
    login_response = auth_api.login(
        username=Config.TEST_USERNAME,
        password=Config.TEST_PASSWORD,
    )

    if 'error' in login_response:
        pytest.skip(f"登录失败: {login_response['error']}")
    assert login_response.get('status_code') == 200, f"登录失败: {login_response}"
    token = auth_api._extract_token(login_response)
    assert token, "未获取到认证token"
    yield token  # 注入token
