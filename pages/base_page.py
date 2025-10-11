import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator_tuple):
        """locator_tuple: (By.SOMETHING, 'selector')"""
        by, locator = locator_tuple
        clickable_element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        clickable_element.click()
        return clickable_element

    def find(self, locator_tuple, allow_empty=False):
        """查找单个元素"""
        by, locator = locator_tuple
        if allow_empty:
            # 快速模式：直接查找，不等待，立即返回结果或None
            try:
                return self.driver.find_element(by, locator)
            except NoSuchElementException:
                return None  # 没找到，返回None
        else:
            # 稳定模式：等待元素加载完成
            return self.wait.until(EC.presence_of_element_located((by, locator)))
    def find_elements(self, locator_tuple, allow_empty=False):
        """查找多个元素"""
        by, locator = locator_tuple
        if allow_empty:
            # 快速模式：直接查找，不等待，立即返回结果
            return self.driver.find_elements(by, locator)
        else:
            # 稳定模式：等待元素加载完成
            return self.wait.until(EC.presence_of_all_elements_located((by, locator)))

    def input_text(self, locator_tuple, text):
        """locator_tuple: (By.SOMETHING, 'selector')"""
        element = self.click(locator_tuple)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(text)

    def is_record_exists(self, column_mapping: dict, record_data: dict, table_rows_locator):
        """
        通用方法：检查指定内容是否在表格中存在（精确匹配）
        :param column_mapping: 字段到列索引的映射，如 {'code': 1, 'name': 2}
        :param record_data: 要检查的记录数据字典
        :param table_rows_locator: 表格行元素的定位器
        :return: 存在返回True，否则返回False
        """
        try:
            # 一次性获取所有行
            rows = self.find_elements(table_rows_locator, allow_empty=True)
            if not rows:
                return False

            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in record_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))

            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) <= max(column_mapping.values()):
                    continue

                match = True
                for field, col_index in check_fields:
                    expected_value = record_data[field]
                    cell_text = self._get_cell_text(cells[col_index])
                    if cell_text != expected_value:
                        print(f"字段不匹配 - 字段: {field}, 期望: '{expected_value}', 实际: '{cell_text}'")
                        match = False
                        break
                if match:
                    return True
            return False
        except Exception as e:
            print(f"检查记录存在时出错: {e}")
            return False

    @staticmethod
    def _get_cell_text(cell_element):
        """通用方法：提取单元格文本（优化性能版）"""
        try:
            # 方法1: 直接获取文本（最快）
            text = cell_element.text.strip()
            if text:
                return text
            # 方法2: 快速检查常见结构
            quick_elements = cell_element.find_elements(By.CSS_SELECTOR, "span, div, button")
            for element in quick_elements[:3]:  # 只检查前几个元素
                quick_text = element.text.strip()
                if quick_text:
                    return quick_text
            return cell_element.text.strip()
        except Exception:
            return ""
