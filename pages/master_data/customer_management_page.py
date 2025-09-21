import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.customer_management_locators import CustomerLocators

class CustomerManagementPage(BasePage):
    """客户管理页面对象封装客户管理页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_customer(self, search_data:dict):
        """搜索客户:param customer_code: 客户码:param customer_name: 客户名称"""
        self.click(CustomerLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(CustomerLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(CustomerLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(CustomerLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_customer_exists(self, customer_data: dict):
        """检查指定的客户是否存在（精确匹配）"""
        try:
            column_mapping = {
                'code': 1, 'edit_code': 1,
                'name': 2, 'edit_name': 2,
            }

            # 一次性获取所有行
            rows = self.find_elements(CustomerLocators.TABLE_ROWS, allow_empty=True)
            if not rows:
                return False
            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in customer_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))
            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                match = True

                for field, col_index in check_fields:
                    expected_value = customer_data[field]
                    cell_text = self._get_cell_text(cells[col_index])
                    if cell_text != expected_value:
                        match = False
                        break
                if match:
                    return True
            return False
        except Exception as e:
            print(f"检查客户存在时出错: {e}")
            return False

    @staticmethod
    def _get_cell_text(cell_element):
        """极简版的单元格文本提取"""
        try:
            # 方法1: 直接获取文本（最快）
            text = cell_element.text.strip()
            if text:
                return text
            # 方法2: 快速检查常见结构（如果必须）
            # 使用更简单、更快速的选择器
            quick_elements = cell_element.find_elements(By.CSS_SELECTOR, "span, div, button")
            for element in quick_elements[:3]:  # 只检查前几个元素
                quick_text = element.text.strip()
                if quick_text:
                    return quick_text
            return cell_element.text.strip()

        except Exception:
            return ""

    def add_customer(self,add_data : dict):
        # 点击新增
        self.click(CustomerLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(CustomerLocators.CUSTOMER_CODE_INPUT, add_data["code"])
        self.input_text(CustomerLocators.CUSTOMER_NAME_INPUT, add_data["name"])
        #点击确定，回到初始的料管理页面
        self.click(CustomerLocators.ADD_CONFIRM_BUTTON)
        time.sleep(0.5)

    def edit_customer(self, edit_data: dict):
        """编辑客户信息:param edit_data: 新的客户数据字典，必须包含customer_code"""
        # 搜索要编辑的客户
        self.search_customer(edit_data)
        self.click(CustomerLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(CustomerLocators.EDIT_BUTTON)
        # 编辑客户信息
        if "edit_code" in edit_data:
            self.input_text(CustomerLocators.CUSTOMER_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(CustomerLocators.CUSTOMER_NAME_INPUT, edit_data["edit_name"])
        # 保存修改
        self.click(CustomerLocators.EDIT_CONFIRM_BUTTON)
        time.sleep(0.5)


    def delete_customer(self, delete_data : dict):
        """删除客户"""
        self.search_customer(delete_data)
        self.click(CustomerLocators.CHECKBOX)
        self.click(CustomerLocators.DELETE_BUTTON)
        self.click(CustomerLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

