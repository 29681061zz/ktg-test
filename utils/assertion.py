from jsonschema import validate, ValidationError
from typing import Dict, Any, List


class ApiAssertion:
    """API断言工具类"""

    @staticmethod
    def assert_status_code(actual_code: int, expected_code: int, message: str = None):
        """断言状态码"""
        assert actual_code == expected_code, \
            message or f"状态码断言失败! 期望: {expected_code}, 实际: {actual_code}"
        return ApiAssertion

    @staticmethod
    def assert_response_time(response_data: Dict[str, Any], max_time: float):
        """断言响应时间"""
        elapsed = response_data.get('elapsed', 0)
        assert elapsed < max_time, \
            f"响应时间超时! 期望: <{max_time}ms, 实际: {elapsed:.2f}ms"
        return ApiAssertion

    @staticmethod
    def assert_json_schema(response_data: Dict[str, Any], schema: Dict[str, Any]):
        """断言JSON结构符合Schema"""
        data = response_data.get('data', {})
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            raise AssertionError(f"JSON Schema验证失败: {e.message}")
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
        """断言所有字段匹配:param actual_data: 实际数据:param expected_data: 期望数据:param exclude_fields: 要排除检查的字段列表"""
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
    def assert_success(response_data: Dict[str, Any]):
        """断言请求成功（状态码2xx）"""
        status_code = response_data.get('status_code', 0)
        assert 200 <= status_code < 300, \
            f"请求未成功! 状态码: {status_code}"
        return ApiAssertion

    @staticmethod
    def assert_error_code(response_data: Dict[str, Any], expected_error_code: str):
        """断言错误码"""
        data = response_data.get('data', {})
        actual_error_code = data.get('error_code') or data.get('code')
        assert actual_error_code == expected_error_code, \
            f"错误码断言失败! 期望: {expected_error_code}, 实际: {actual_error_code}"
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