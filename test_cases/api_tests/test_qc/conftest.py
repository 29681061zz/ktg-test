import pytest

@pytest.fixture(scope="function")
def authenticated_qcdefect_api(api_token):
    """已认证的常见缺陷API - 函数式fixture"""
    from apis.qc_api.qcdefect_api import QcdefectAPI
    api = QcdefectAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_qcindex_api(api_token):
    """已认证的常见缺陷API - 函数式fixture"""
    from apis.qc_api.qcindex_api import QcindexAPI
    api = QcindexAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_qctemplate_api(api_token):
    """已认证的常见缺陷API - 函数式fixture"""
    from apis.qc_api.qctemplate_api import QctemplateAPI
    api = QctemplateAPI()
    api.set_auth_token(api_token)
    yield api

@pytest.fixture(scope="function")
def authenticated_iqc_api(api_token):
    """已认证的常见缺陷API - 函数式fixture"""
    from apis.qc_api.iqc_api import IqcAPI
    api = IqcAPI()
    api.set_auth_token(api_token)
    yield api