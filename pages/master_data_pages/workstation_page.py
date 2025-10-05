import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.master_data_locators.workstation_locators import WorkstationLocators

class WorkStationPage(BasePage):
    """工作站页面对象封装工作站页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_workstation(self, search_data:dict):
        """工作站编码和工作站名称"""
        self.click(WorkstationLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(WorkstationLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(WorkstationLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(WorkstationLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_workstation_exists(self, workstation_data: dict):
        """检查指定的工作站是否存在（精确匹配）"""
        column_mapping = {
            'code': 1, 'edit_code': 1,
            'name': 2, 'edit_name': 2,
            'workshop': 4,
            'process': 5,
        }
        return self.is_record_exists(column_mapping, workstation_data, WorkstationLocators.TABLE_ROWS)

    def add_workstation(self,add_data : dict):
        # 点击新增
        self.click(WorkstationLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(WorkstationLocators.WORKSTATION_CODE_INPUT, add_data["code"])
        self.input_text(WorkstationLocators.WORKSTATION_NAME_INPUT, add_data["name"])
        if "location" in add_data:
            self.input_text(WorkstationLocators.WORKSTATION_LOCATION, add_data["location"])
        self.select_option(WorkstationLocators.WORKSHOP_SELECT, add_data["workshop"])
        self.select_option(WorkstationLocators.PROCESS_SELECT, add_data["process"])
        #点击保存回到初始的设置页面
        self.click(WorkstationLocators.ADD_SAVE_BUTTON)
        time.sleep(0.5)

    def select_option(self, select_locator, option_text):
        # 点击下拉框展开选项
        self.click(select_locator)
        # 构建选项定位器 - Element UI的选项结构
        option_locator = (By.XPATH,f"(//li[contains(@class, 'el-select-dropdown__item') and span[text()='{option_text}']])[2]")
        # 点击选项
        self.click(option_locator)

    def edit_workstation(self, edit_data: dict):
        """编辑工作站信息:param edit_data: 新的工作站数据字典，必须包含workstation_code"""
        # 搜索要编辑的工作站
        self.search_workstation(edit_data)
        self.click(WorkstationLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(WorkstationLocators.EDIT_BUTTON)
        # 编辑工作站信息
        if "edit_code" in edit_data:
            self.input_text(WorkstationLocators.WORKSTATION_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(WorkstationLocators.WORKSTATION_NAME_INPUT, edit_data["edit_name"])
        if "workshop" in edit_data:
            self.input_text(WorkstationLocators.WORKSHOP_SELECT, edit_data["area"])
        if "process" in edit_data:
            self.input_text(WorkstationLocators.PROCESS_SELECT, edit_data["area"])
        # 保存修改
        self.click(WorkstationLocators.EDIT_SAVE_BUTTON)
        time.sleep(0.5)


    def delete_workstation(self, delete_data : dict):
        """删除工作站"""
        self.search_workstation(delete_data)
        self.click(WorkstationLocators.CHECKBOX)
        self.click(WorkstationLocators.DELETE_BUTTON)
        self.click(WorkstationLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

