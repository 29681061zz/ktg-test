import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.master_data_locators.customer_management_locators import CustomerLocators

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
        column_mapping = {
             'code': 1, 'edit_code': 1,
            'name': 2, 'edit_name': 2,
        }
        return self.is_record_exists(column_mapping, customer_data, CustomerLocators.TABLE_ROWS)

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

