import pytest
import json
import os
from typing import Dict, List, Any


class DataManager:
    """统一测试数据管理器"""
    _data_cache = {}

    @staticmethod
    def _get_project_root():
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.dirname(current_dir)

    @staticmethod
    def load_module_data(category: str, module: str) -> Dict[str, Any]:
        cache_key = f"{category}/{module}"
        if cache_key in DataManager._data_cache:
            return DataManager._data_cache[cache_key]

        data_path = os.path.join(
            DataManager._get_project_root(),
            'test_data', category, f"{module}.json"
        )

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"测试数据文件不存在: {data_path}")

        with open(data_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            DataManager._data_cache[cache_key] = data
            return data

    @staticmethod
    def parametrize(category: str, module: str, case_type: str, arg_names: List[str]):
        """通用参数化装饰器"""
        test_cases = DataManager.load_module_data(category, module).get(case_type, [])

        if not test_cases:
            print(f"警告: {category}/{module} 中未找到 '{case_type}' 类型的测试用例")
            return pytest.mark.parametrize(",".join(arg_names), [])

        # 准备参数化数据
        parametrize_data = []
        for case in test_cases:
            params = [case.get(arg) for arg in arg_names]
            if None in params:
                raise ValueError(f"测试用例中缺少参数: {case.get('test_id', '未知ID')}")
            parametrize_data.append(tuple(params))

        # 生成测试ID
        ids_list = [case.get('test_id', f"{case_type}_{i}") for i, case in enumerate(test_cases)]

        return pytest.mark.parametrize(
            ",".join(arg_names),
            parametrize_data,
            ids=ids_list
        )

    # 快捷方法
    @staticmethod
    def master_data(module: str, case_type: str, arg_names: List[str]):
        """主数据快捷方法"""
        return DataManager.parametrize('master_data', module, case_type, arg_names)

    @staticmethod
    def warehouse(module: str, case_type: str, arg_names: List[str]):
        """仓库管理快捷方法"""
        return DataManager.parametrize('warehouse_management', module, case_type, arg_names)

    @staticmethod
    def production(module: str, case_type: str, arg_names: List[str]):
        """生产管理快捷方法"""
        return DataManager.parametrize('production_management', module, case_type, arg_names)

    @staticmethod
    def qc(module: str, case_type: str, arg_names: List[str]):
        """生产管理快捷方法"""
        return DataManager.parametrize('qc', module, case_type, arg_names)

    @staticmethod
    def clear_cache():
        DataManager._data_cache.clear()