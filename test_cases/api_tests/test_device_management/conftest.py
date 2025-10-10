import pytest

@pytest.fixture(scope="function")
def authenticated_machinerytype_api(api_token):
    """已认证的设备类型设置API - 函数式fixture"""
    from apis.device_management_api.machinerytype_api import MachineryTypeAPI
    api = MachineryTypeAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_machinery_api(api_token):
    """已认证的设备类型设置API - 函数式fixture"""
    from apis.device_management_api.machinery_api import MachineryAPI
    api = MachineryAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_dvsubject_api(api_token):
    """已认证的设备类型设置API - 函数式fixture"""
    from apis.device_management_api.dvsubject_api import DvsubjectAPI
    api = DvsubjectAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_checkplan_api(api_token):
    """已认证的设备类型设置API - 函数式fixture"""
    from apis.device_management_api.checkplan_api import CheckplanAPI
    api = CheckplanAPI()
    api.set_auth_token(api_token)
    yield api