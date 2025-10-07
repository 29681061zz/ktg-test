import pytest

@pytest.fixture(scope="function")
def authenticated_process_api(api_token):
    """已认证的工序API - 函数式fixture"""
    from apis.production_management_api.process_api import ProcessAPI
    api = ProcessAPI()
    api.set_auth_token(api_token)
    yield api