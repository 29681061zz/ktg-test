import os
import pytest
from datetime import datetime
from selenium import webdriver
from pages.login_page import LoginPage
from utils.logger import setup_logger

logger = setup_logger()


@pytest.fixture(scope="session")
def driver(request):
    is_in_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    if is_in_actions:   # 远程驱动配置
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from selenium.webdriver.edge.options import Options as EdgeOptions

        edge_options = EdgeOptions()
        edge_options.add_argument('--headless=new')
        edge_options.add_argument('--no-sandbox')
        edge_options.add_argument('--disable-dev-shm-usage')
        edge_options.add_argument('--disable-gpu')
        edge_options.add_argument('--window-size=1920,1080')
        driver_instance = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
    else:
        driver_instance=webdriver.Edge()        # 本地驱动配置
    driver_instance.implicitly_wait(1)
    yield driver_instance
    driver_instance.quit()

@pytest.fixture(scope="session")
def logged_in_driver(driver, request):
    """已登录的浏览器实例 """
    request.node.driver = driver    # 将driver存储到测试项中，供hook使用
    login_page = LoginPage(driver)
    login_page.login()
    yield driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """获取测试结果并在失败时自动截图"""
    outcome = yield
    report = outcome.get_result()

    # 只在测试执行阶段处理失败情况
    if report.when == "call" and report.failed:
        try:
            # 多种方式获取driver实例
            driver = None

            # 方式1：从fixture中直接获取
            driver = item.funcargs.get('driver', None)

            # 方式2：如果fixture名称不是driver，尝试其他常见名称
            if not driver:
                for fixture_name in ['browser', 'webdriver', 'selenium', 'chrome', 'firefox']:
                    driver = item.funcargs.get(fixture_name, None)
                    if driver:
                        break

            # 方式3：从测试类实例中获取
            if not driver and hasattr(item, 'cls'):
                driver = getattr(item.cls, 'driver', None)

            # 方式4：从item实例中获取
            if not driver:
                driver = getattr(item, 'driver', None)

            if driver and hasattr(driver, 'get_screenshot_as_png'):
                # 生成截图名称
                test_name = item.name.replace('[', '_').replace(']', '_')
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_name = f"FAILED_{test_name}_{timestamp}"

                # 直接附加到Allure报告
                import allure
                screenshot_data = driver.get_screenshot_as_png()

                allure.attach(
                    screenshot_data,
                    name=screenshot_name,
                    attachment_type=allure.attachment_type.PNG
                )
                # logger.info(f"测试失败截图已附加到Allure报告: {screenshot_name}") 日志
        except Exception as e:
            logger.error(f"截图处理失败: {str(e)}")

