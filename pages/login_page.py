from .base_page import BasePage
from configs.settings import Config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoSuchElementException
import ddddocr
import time

class LoginPage(BasePage):
    # 定位器
    LOGIN_BUTTON = (By.XPATH, "//button[.//span[text()='登 录']]")
    CAPTCHA_INPUT = (By.XPATH, "//input[@placeholder='验证码']")
    CAPTCHA_IMAGE = (By.CLASS_NAME, "login-code-img")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), '验证码错误')]")

    def login(self, max_retries=10):
        """一键登录操作，验证码错误时自动重试"""
        from utils.logger import setup_logger
        logger = setup_logger(__name__)
        # 关键修改：设置日志级别为CRITICAL，仅保留严重错误日志（可根据需要调整）
        # 级别说明：DEBUG < INFO < WARNING < ERROR < CRITICAL
        logger.setLevel("CRITICAL") # 这一行会禁用INFO/DEBUG/WARNING级别的日志

        logger.info(f"开始登录操作，最大重试次数: {max_retries}")
        self.driver.get(f"{Config.BASE_URL}/login")
        ocr = ddddocr.DdddOcr(show_ad=False)
        logger.debug("ddddocr实例已创建")

        retry_count = 0
        while retry_count < max_retries:
            logger.info(f"=== 第 {retry_count + 1} 次登录尝试 ===")
            try:
                # 1. 确保页面已加载（每次重试都重新访问/确认登录页）
                logger.debug("访问/确认登录页面")
                # 等待登录页面核心元素（如登录按钮）加载完成，确保页面就绪
                self.wait.until(lambda d: d.find_element(*self.LOGIN_BUTTON).is_displayed())
                logger.info(f"已确认登录页面加载完成: {Config.BASE_URL}/login")
                # 2. 查找验证码图片元素（带超时处理）
                logger.debug("开始查找验证码图片元素")
                captcha_element = self.wait.until(lambda d: d.find_element(*self.CAPTCHA_IMAGE),message="超时：未找到验证码图片元素")
                logger.debug("成功找到验证码图片元素")
                # 3. 等待验证码图片src有效（修复核心：判断src非空且包含base64）
                logger.debug("等待验证码图片src加载完成（非空+含base64）")
                src_data = self.wait.until(lambda d: captcha_element.get_attribute("src") or "",message="超时：验证码图片src未加载")
                # 二次校验：确保src包含base64（排除无效src）
                if not src_data or "base64" not in src_data:
                    logger.warning(f"验证码图片数据异常（src长度: {len(src_data) if src_data else 0}，无base64）")
                    retry_count += 1  # 关键：重试计数递增
                    self.driver.refresh()
                    time.sleep(1)  # 避免频繁刷新给服务器压力
                    continue
                # 4. 识别验证码（原有逻辑保留，补充日志）
                logger.debug(f"获取到有效验证码src，长度: {len(src_data)}")
                base64_data = src_data.split(",")[1]
                logger.debug(f"提取base64数据，长度: {len(base64_data)}")
                logger.debug("开始识别验证码")
                text = ocr.classification(base64_data)
                logger.info(f"验证码识别结果: '{text}'")
                # 5. 计算验证码（调用优化后的calculate_captcha）
                captcha_result = self.calculate_captcha(text)
                logger.info(f"验证码计算结果: {captcha_result}")
                if captcha_result is None:
                    logger.warning("验证码计算失败，无法解析表达式")
                    retry_count += 1  # 关键：重试计数递增
                    self.driver.refresh()  # 刷新页面获取新验证码
                    time.sleep(1)  # 等待刷新后页面加载完成
                    continue
                # 6. 输入验证码并登录
                logger.debug(f"输入验证码: {captcha_result}")
                self.input_text(self.CAPTCHA_INPUT,captcha_result)
                logger.debug("点击登录按钮")
                self.click(self.LOGIN_BUTTON)
                time.sleep(1)  # 等待登录请求响应（可替换为显式等待）
                # 7. 检查登录结果
                # 检查错误提示（验证码错误等）
                logger.debug("检查是否有验证码错误提示")
                try:
                    error_element = self.driver.find_element(*self.ERROR_MESSAGE)
                    if error_element.is_displayed():
                        logger.warning(f"有验证码错误提示登录失败：{error_element.text}")
                        retry_count += 1  # 关键：重试计数递增
                        self.driver.refresh()
                        time.sleep(1)
                        continue
                    else:
                        return True
                except NoSuchElementException:
                    logger.debug("未找到验证码错误提示元素")
                    return True
            # 8. 异常处理（所有异常都需递增重试计数）
            except:
                retry_count += 1
                self.driver.refresh()
                time.sleep(1)
            # 9. 重试间隔（避免高频请求被服务器拦截）
            if retry_count < max_retries:
                time.sleep(1)
        # 10. 达到最大重试次数
        logger.error(f"❌ 登录失败，已达最大重试次数 {max_retries}")
        return False

    def calculate_captcha(self, expression):
        try:
            # 映射字符到数字
            char_to_num = {'q': 0, 't': 1, 'l':1, 'z':2}
            num1 = char_to_num.get(expression[0], expression[0])
            num2 = char_to_num.get(expression[2], expression[2])
            # 转换为整数
            try:
                num1 = int(num1)
                num2 = int(num2)
            except ValueError:
                return None
            if len(expression) ==2:
                return num1 - num2
            # 映射运算符
            op_map = {
                '+': '+', 't': '+',
                '-': '-', 'r': '-',
                '*': '*', 'x': '*','k':'*',
                '/': '//', 'l': '//'
            }
            operator = op_map.get(expression[1])
            if not operator:
                return num1 - num2  # 处理未定义的运算符情况
            # 执行计算
            return eval(f"{num1}{operator}{num2}")
        except (ValueError, IndexError, ZeroDivisionError):
            return None