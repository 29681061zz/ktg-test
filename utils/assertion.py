from typing import Dict, Any, List

class ApiAssertion:
    """API断言工具类"""
    @staticmethod
    def assert_status_code(actual_code: int, expected_code: int, message: str = None):
        """断言HTTP状态码"""
        assert actual_code == expected_code, \
            message or f"HTTP状态码断言失败! 期望: {expected_code}, 实际: {actual_code}"
        return ApiAssertion

    @staticmethod
    def assert_business_code(actual_code: int, expected_code: int, message: str = None):
        """断言业务状态码"""
        assert actual_code == expected_code, \
            message or f"业务状态码断言失败! 期望: {expected_code}, 实际: {actual_code}"
        return ApiAssertion


    @staticmethod
    def assert_json_field(response_data: Dict[str, Any], field_path: str, expected_value: Any):
        """断言响应JSON中特定字段的值"""
        actual_value = ApiAssertion._extract_field(response_data, field_path)
        assert actual_value == expected_value, \
            f"字段 {field_path} 值断言失败! 期望: {expected_value}, 实际: {actual_value}"
        return ApiAssertion

    @staticmethod
    def assert_all_fields_match(actual_data: Dict[str, Any], expected_data: Dict[str, Any],
                                exclude_fields: List[str] = None):
        """断言所有字段匹配"""
        if exclude_fields is None:
            exclude_fields = []
        for field, expected_value in expected_data.items():
            if field in exclude_fields:
                continue

            if field in actual_data:
                actual_value = actual_data[field]
                assert actual_value == expected_value, \
                    f"字段 {field} 值断言失败! 期望: {expected_value}, 实际: {actual_value}"
            else:
                # 如果字段在实际数据中不存在，根据需求决定是否报错
                # 这里选择报错，因为期望的字段应该在响应中存在
                raise AssertionError(f"字段 {field} 在响应数据中不存在")
        return ApiAssertion

    @staticmethod
    def assert_json_contains(response_data: Dict[str, Any], field_path: str):
        """断言响应JSON中包含特定字段"""
        actual_value = ApiAssertion._extract_field(response_data, field_path)
        assert actual_value is not None, \
            f"响应中未找到字段: {field_path}"
        return ApiAssertion

    @staticmethod
    def _extract_field(data: Dict[str, Any], field_path: str) -> Any:
        """从嵌套字典中提取字段值"""
        keys = field_path.split('.')
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current