ktg/                 # 项目根目录
├── common/                      # 【重命名】核心组件层
│   ├── __init__.py
│   ├── api_client.py          # 封装所有HTTP请求
├── configs/                     
│   ├── __init__.py
│   ├── settings.py          
├── pages/                     # 【重命名】页面对象层（POM核心！）
│   ├──master_data_pages/
│   │   ├──material_management_page.py
│   ├── __init__.py
│   ├── base_page.py           # 抽象基类，封装通用页面操作
│   ├── login_page.py          # 登录页面
│   └── ...                    # 其他页面
├── test_cases/                # 测试用例层
│   ├── api_tests/             # 接口测试
│   │   ├── __init__.py
│   │   ├── test_production_api.py
│   │   └── test_quality_api.py
│   └── ui_tests/              # UI测试test_master_data
│       ├── __init__.py
│       └── test_master_data
│           ├── test_production_ui.py
│           └── test_quality_ui.py
├── test_data/                 # 测试数据
│   ├── __init__.py
│   ├── api_data.json
│   └── ui_data.json
├── reports/                   # 测试报告输出目录
├── conftest.py                # 全局Pytest配置（如全局fixture）
└── pytest.ini                 # Pytest配置文件