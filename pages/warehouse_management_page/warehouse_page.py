import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.warehouse_management_locators.warehouse_locators import WareHouseLocators

class WareHousePage(BasePage):
    """仓库设置页面对象封装仓库设置页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_warehouse(self, search_data:dict):
        """仓库编码和仓库名称"""
        self.click(WareHouseLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(WareHouseLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(WareHouseLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(WareHouseLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_warehouse_exists(self, warehouse_data: dict):
        """检查指定的仓库是否存在（精确匹配）"""
        column_mapping = {
            'code': 1, 'edit_code': 1,
            'name': 2, 'edit_name': 2,
            'location': 3,
            'remark': 7,
        }
        return self.is_record_exists(column_mapping, warehouse_data, WareHouseLocators.TABLE_ROWS)

    def add_warehouse(self,add_data : dict):
        # 点击新增
        self.click(WareHouseLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(WareHouseLocators.WAREHOUSE_CODE_INPUT, add_data["code"])
        self.input_text(WareHouseLocators.WAREHOUSE_NAME_INPUT, add_data["name"])
        if "location" in add_data:
            self.input_text(WareHouseLocators.WAREHOUSE_LOCATION, add_data["location"])
        if "area" in add_data:
            self.input_text(WareHouseLocators.WAREHOUSE_AREA, add_data["area"])
        if "remark" in add_data:
            self.input_text(WareHouseLocators.WAREHOUSE_REMARK, add_data["remark"])
        #点击保存回到初始的设置页面
        self.click(WareHouseLocators.ADD_SAVE_BUTTON)
        time.sleep(0.5)

    def edit_warehouse(self, edit_data: dict):
        """编辑仓库信息:param edit_data: 新的仓库数据字典，必须包含warehouse_code"""
        # 搜索要编辑的仓库
        self.search_warehouse(edit_data)
        self.click(WareHouseLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(WareHouseLocators.EDIT_BUTTON)
        # 编辑仓库信息
        if "edit_code" in edit_data:
            self.input_text(WareHouseLocators.WAREHOUSE_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(WareHouseLocators.WAREHOUSE_NAME_INPUT, edit_data["edit_name"])
        if "location" in edit_data:
            self.input_text(WareHouseLocators.WAREHOUSE_LOCATION, edit_data["location"])
        if "area" in edit_data:
            self.input_text(WareHouseLocators.WAREHOUSE_AREA, edit_data["area"])
        if "remark" in edit_data:
            self.input_text(WareHouseLocators.WAREHOUSE_REMARK, edit_data["remark"])
        # 保存修改
        self.click(WareHouseLocators.EDIT_SAVE_BUTTON)
        time.sleep(0.5)

    def delete_warehouse(self, delete_data : dict):
        """删除仓库"""
        self.search_warehouse(delete_data)
        self.click(WareHouseLocators.CHECKBOX)
        self.click(WareHouseLocators.DELETE_BUTTON)
        self.click(WareHouseLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

