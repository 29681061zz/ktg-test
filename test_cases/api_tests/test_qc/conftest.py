import pytest

@pytest.fixture(scope="function")
def authenticated_qcdefect_api(api_token):
    """已认证的常见缺陷API - 函数式fixture"""
    from apis.qc_api.qcdefect_api import QcdefectAPI
    api = QcdefectAPI()
    api.set_auth_token(api_token)
    yield api
