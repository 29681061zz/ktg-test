import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.master_data_locators.workshop_setup_locators import WorkshopLocators

class WorkShopPage(BasePage):
    """车间设置页面对象封装车间设置页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_workshop(self, search_data:dict):
        """车间编码和车间名称"""
        self.click(WorkshopLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(WorkshopLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(WorkshopLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(WorkshopLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_workshop_exists(self, workshop_data: dict):
        """检查指定的车间设置是否存在（精确匹配）"""
        column_mapping = {
            'code': 1, 'edit_code': 1,
            'name': 2, 'edit_name': 2,
            'area': 3,
        }
        return self.is_record_exists(column_mapping, workshop_data, WorkshopLocators.TABLE_ROWS)


    def add_workshop(self,add_data : dict):
        # 点击新增
        self.click(WorkshopLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(WorkshopLocators.WORKSHOP_CODE_INPUT, add_data["code"])
        self.input_text(WorkshopLocators.WORKSHOP_NAME_INPUT, add_data["name"])
        if "area" in add_data:
            self.input_text(WorkshopLocators.WORKSHOP_AREA_INPUT, add_data["area"])
        #点击保存，回到初始的设置页面
        self.click(WorkshopLocators.ADD_CONFIRM_BUTTON)
        time.sleep(0.5)

    def edit_workshop(self, edit_data: dict):
        """编辑车间信息:param edit_data: 新的车间数据字典，必须包含workshop_code"""
        # 搜索要编辑的车间
        self.search_workshop(edit_data)
        self.click(WorkshopLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(WorkshopLocators.EDIT_BUTTON)
        # 编辑车间信息
        if "edit_code" in edit_data:
            self.input_text(WorkshopLocators.WORKSHOP_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(WorkshopLocators.WORKSHOP_NAME_INPUT, edit_data["edit_name"])
        if "area" in edit_data:
            self.input_text(WorkshopLocators.WORKSHOP_AREA_INPUT, edit_data["area"])
        # 保存修改
        self.click(WorkshopLocators.EDIT_CONFIRM_BUTTON)
        time.sleep(0.5)


    def delete_workshop(self, delete_data : dict):
        """删除车间"""
        self.search_workshop(delete_data)
        self.click(WorkshopLocators.CHECKBOX)
        self.click(WorkshopLocators.DELETE_BUTTON)
        self.click(WorkshopLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

