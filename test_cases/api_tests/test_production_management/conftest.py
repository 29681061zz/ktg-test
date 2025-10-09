import pytest

@pytest.fixture(scope="function")
def authenticated_workorder_api(api_token):
    """已认证的生产工单API - 函数式fixture"""
    from apis.production_management_api.workorder_api import WorkOrderAPI
    api = WorkOrderAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_process_api(api_token):
    """已认证的工序API - 函数式fixture"""
    from apis.production_management_api.process_api import ProcessAPI
    api = ProcessAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_proroute_api(api_token):
    """已认证的工艺路线API - 函数式fixture"""
    from apis.production_management_api.proroute_api import ProrouteAPI
    api = ProrouteAPI()
    api.set_auth_token(api_token)
    yield api