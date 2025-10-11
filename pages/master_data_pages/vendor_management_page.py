import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.master_data_locators.vendor_management_locators import VendorLocators

class VendorPage(BasePage):
    """供应商管理页面对象封装供应商管理页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_vendor(self, search_data:dict):
        """供应商编码和供应商名称"""
        self.click(VendorLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(VendorLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(VendorLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(VendorLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_vendor_exists(self, vendor_data: dict):
        """检查指定的供应商是否存在（精确匹配）"""
        column_mapping = {
            'code': 1,
            'name': 2, 'edit_name': 2,
            'abbreviation': 3,
            'rating': 5,
        }
        return self.is_record_exists(column_mapping, vendor_data, VendorLocators.TABLE_ROWS)


    def add_vendor(self,add_data : dict):
        # 点击新增
        self.click(VendorLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(VendorLocators.VENDOR_CODE_INPUT, add_data["code"])
        self.input_text(VendorLocators.VENDOR_NAME_INPUT, add_data["name"])
        if "abbreviation" in add_data:
            self.input_text(VendorLocators.ABBREVIATION_INPUT, add_data["abbreviation"])
        if "rating" in add_data:
            self.input_text(VendorLocators.RATING_INPUT, add_data["rating"])
        #点击确定，然后点击关闭，回到初始的管理页面
        self.click(VendorLocators.ADD_CONFIRM_BUTTON)
        time.sleep(0.5)

    def edit_vendor(self, edit_data: dict):
        """编辑供应商信息:param edit_data: 新的供应商数据字典，必须包含vendor_code"""
        # 搜索要编辑的供应商
        self.search_vendor(edit_data)
        self.click(VendorLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(VendorLocators.EDIT_BUTTON)
        # 编辑供应商信息
        if "edit_code" in edit_data:
            self.input_text(VendorLocators.VENDOR_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(VendorLocators.VENDOR_NAME_INPUT, edit_data["edit_name"])
        if "abbreviation" in edit_data:
            self.input_text(VendorLocators.ABBREVIATION_INPUT, edit_data["abbreviation"])
        if "rating" in edit_data:
            self.input_text(VendorLocators.RATING_INPUT, edit_data["rating"])
        # 保存修改
        self.click(VendorLocators.EDIT_CONFIRM_BUTTON)
        time.sleep(0.5)


    def delete_vendor(self, delete_data : dict):
        """删除供应商"""
        self.search_vendor(delete_data)
        self.click(VendorLocators.CHECKBOX)
        self.click(VendorLocators.DELETE_BUTTON)
        self.click(VendorLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

