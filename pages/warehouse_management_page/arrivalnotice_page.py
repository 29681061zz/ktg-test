import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.warehouse_management_locators.arrivalnotice_locators import ArrivalNoticeLocators

class ArrivalNoticePage(BasePage):
    """到货通知页面对象封装到货通知页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_arrivalnotice(self, search_data:dict):
        """仓库编码和仓库名称"""
        self.click(ArrivalNoticeLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(ArrivalNoticeLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(ArrivalNoticeLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(ArrivalNoticeLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_arrivalnotice_exists(self, arrivalnotice_data: dict):
        """检查指定的仓库是否存在（精确匹配）"""
        column_mapping = {
            'code': 1,
            'name': 2, 'edit_name': 2,
            'pocode': 3,
            'date': 7,
            'vendorname':4,
        }
        return self.is_record_exists(column_mapping, arrivalnotice_data, ArrivalNoticeLocators.TABLE_ROWS)

    def add_arrivalnotice(self,add_data : dict):
        # 点击新增
        self.click(ArrivalNoticeLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_CODE_INPUT, add_data["code"])
        self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_NAME_INPUT, add_data["name"])
        if "pocode" in add_data:
            self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_POCODE, add_data["pocode"])
        if "date" in add_data:
            self.input_text(ArrivalNoticeLocators.ARRIVALDATE_INPUT, add_data["date"])
        #选择供应商
        self.click(ArrivalNoticeLocators.VENDOR_SELECT)
        self.input_text(ArrivalNoticeLocators.VENDOR_NAME,add_data["vendorname"])
        self.click(ArrivalNoticeLocators.VENDOR_SEARCH)
        self.click(ArrivalNoticeLocators.SELECT_VENDOR_BUTTON)
        self.click(ArrivalNoticeLocators.SELECT_VENDOR_CONFIRM)
        #点击保存回到初始的设置页面
        self.click(ArrivalNoticeLocators.ADD_SAVE_BUTTON)
        time.sleep(0.5)

    def edit_arrivalnotice(self, edit_data: dict):
        """编辑仓库信息:param edit_data: 新的仓库数据字典，必须包含arrivalnotice_code"""
        # 搜索要编辑的仓库
        self.search_arrivalnotice(edit_data)
        self.click(ArrivalNoticeLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(ArrivalNoticeLocators.EDIT_BUTTON)
        # 编辑仓库信息
        if "edit_code" in edit_data:
            self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_NAME_INPUT, edit_data["edit_name"])
        if "pocode" in edit_data:
            self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_POCODE, edit_data["pocode"])
        if "date" in edit_data:
            self.input_text(ArrivalNoticeLocators.ARRIVALDATE_INPUT, edit_data["date"])
        if "vendorname" in edit_data:
            self.click(ArrivalNoticeLocators.VENDOR_SELECT)
            self.input_text(ArrivalNoticeLocators.VENDOR_NAME, edit_data["vendorname"])
            self.click(ArrivalNoticeLocators.VENDOR_SEARCH)
            self.click(ArrivalNoticeLocators.SELECT_VENDOR_BUTTON)
            self.click(ArrivalNoticeLocators.SELECT_VENDOR_CONFIRM)
        # 保存修改
        self.click(ArrivalNoticeLocators.EDIT_SAVE_BUTTON)
        time.sleep(0.5)

    def delete_arrivalnotice(self, delete_data : dict):
        """删除仓库"""
        self.search_arrivalnotice(delete_data)
        self.click(ArrivalNoticeLocators.CHECKBOX)
        self.click(ArrivalNoticeLocators.DELETE_BUTTON)
        self.click(ArrivalNoticeLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

