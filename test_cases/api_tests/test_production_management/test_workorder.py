import pytest
import requests
import json

class TestWorkOrder:

    def test_create_workorder(self, authenticated_workorder_api):
        response = authenticated_workorder_api.create_workorder()
        assert response['status_code'] == 201