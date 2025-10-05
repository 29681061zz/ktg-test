import pytest
import json
import os
from typing import Dict, List, Any

class DataManager:
    """统一测试数据管理器"""
    _data_cache = {}
    @staticmethod
    def _get_project_root():
        """获取项目根目录"""
        # 方法1：通过当前文件的父目录推算
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)  # utils的父目录就是项目根目录
        return project_root

    @staticmethod
    def load_module_data(category: str, module: str) -> Dict[str, Any]:
        """
        加载测试数据
        :param category: 分类，如 'master_data'
        :param module: 模块，如 'material_management'
        """
        cache_key = f"{category}/{module}"

        if cache_key in DataManager._data_cache:
            return DataManager._data_cache[cache_key]

        # 使用绝对路径
        project_root = DataManager._get_project_root()
        data_file = f"{module}.json"
        data_path = os.path.join(project_root, 'test_data', category, data_file)

        print(f"尝试加载数据文件: {data_path}")  # 调试信息

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"测试数据文件不存在: {data_path}")

        try:
            with open(data_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                DataManager._data_cache[cache_key] = data
                return data

        except json.JSONDecodeError as e:
            raise ValueError(f"JSON解析失败 {data_path}: {str(e)}")

    @staticmethod
    def get_test_cases(category: str, module: str, case_type: str) -> List[Dict[str, Any]]:
        """获取指定类型的测试用例"""
        module_data = DataManager.load_module_data(category, module)
        cases = module_data.get(case_type, [])

        if not cases:
            print(f"警告: {category}/{module} 中未找到 '{case_type}' 类型的测试用例")

        return cases

    @staticmethod
    def get_parametrize_args(category: str, module: str, case_type: str, args: List[str]) -> List[tuple]:
        """为pytest参数化准备数据格式"""
        test_cases = DataManager.get_test_cases(category, module, case_type)
        parametrize_data = []

        for case in test_cases:
            params = []
            for arg in args:
                param_value = case.get(arg)
                if param_value is None:
                    raise ValueError(f"测试用例中缺少参数 '{arg}': {case.get('test_id', '未知ID')}")
                params.append(param_value)

            parametrize_data.append(tuple(params))

        return parametrize_data

    # 主数据分类方法
    @staticmethod
    def parametrize_master_data(module: str, case_type: str, arg_names: List[str]):
        """主数据分类参数化快捷方法"""
        test_cases = DataManager.get_test_cases('master_data', module, case_type)
        # 使用测试用例中的 test_id 作为标识符
        ids_list = [case.get('test_id', f"{case_type}_{i}") for i, case in enumerate(test_cases)]
        return pytest.mark.parametrize(
            ",".join(arg_names),
            DataManager.get_parametrize_args('master_data', module, case_type, arg_names),
            ids=ids_list
        )
    # 仓库管理分类方法
    @staticmethod
    def parametrize_warehouse_management(module: str, case_type: str, arg_names: List[str]):
        """仓库管理分类参数化快捷方法"""
        test_cases = DataManager.get_test_cases('warehouse_management', module, case_type)
        # 使用测试用例中的 test_id 作为标识符
        ids_list = [case.get('test_id', f"{case_type}_{i}") for i, case in enumerate(test_cases)]
        return pytest.mark.parametrize(
            ",".join(arg_names),
            DataManager.get_parametrize_args('warehouse_management', module, case_type, arg_names),
            ids=ids_list
        )

    # 工具方法：清空缓存
    @staticmethod
    def clear_cache():
        """清空数据缓存"""
        DataManager._data_cache.clear()