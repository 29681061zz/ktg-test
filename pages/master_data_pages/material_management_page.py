import time
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.master_data_locators.material_management_locators import  MaterialLocators

class MaterialManagementPage(BasePage):
    """物料管理页面对象，封装所有物料相关的UI操作"""
    # -------------------- 搜索操作 --------------------
    def search_material(self, search_data:dict):
        """搜索物料"""
        self.click(MaterialLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(MaterialLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(MaterialLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(MaterialLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_material_exists(self, material_data: dict):
        """检查物料是否存在"""
        column_mapping = {
            'code': 1,
            'name': 2, 'edit_name': 2,
            'specification': 3,
            'unit': 4,
            'category': 6
        }
        return self.is_record_exists(column_mapping, material_data, MaterialLocators.TABLE_ROWS)

    def add_material(self,add_data : dict):
        # 点击新增
        self.click(MaterialLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(MaterialLocators.MATERIAL_CODE_INPUT, add_data["code"])
        self.input_text(MaterialLocators.MATERIAL_NAME_INPUT, add_data["name"])
        if "specification" in add_data:
            self.input_text(MaterialLocators.MATERIAL_SPECIFICATION_INPUT, add_data["specification"])
        self.select_option(MaterialLocators.UNIT_SELECT, add_data["unit"])
        self.input_text(MaterialLocators.CATEGORY_SELECT, add_data["category"] + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
        #关闭批管理
        self.click(MaterialLocators.BATCH_MANAGEMENT_SWITCH)
        #点击确定，然后点击关闭，回到初始的料管理页面
        self.click(MaterialLocators.ADD_CONFIRM_BUTTON)
        self.click(MaterialLocators.CLOSE_BUTTON)
        time.sleep(0.5)

    def select_option(self, select_locator, option_text):
        # 点击下拉框展开选项
        self.click(select_locator)
        # 构建选项定位器 - Element UI的选项结构
        option_locator = (By.XPATH,f"//li[contains(@class, 'el-select-dropdown__item') and span[text()='{option_text}']]")
        # 点击选项
        self.click(option_locator)

    def edit_material(self, edit_data: dict):
        """编辑物料信息:edit_data: 新的物料数据字典，必须包含code"""
        # 搜索要编辑的物料
        self.search_material(edit_data)
        self.click(MaterialLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(MaterialLocators.EDIT_BUTTON)
        # 编辑物料信息
        if "edit_code" in edit_data:
            self.input_text(MaterialLocators.MATERIAL_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(MaterialLocators.MATERIAL_NAME_INPUT, edit_data["edit_name"])
        if "specification" in edit_data:
            self.input_text(MaterialLocators.MATERIAL_SPECIFICATION_INPUT, edit_data["specification"])
        if "unit" in edit_data:
            self.select_option(MaterialLocators.UNIT_SELECT, edit_data["unit"])
        if "category" in edit_data:
            self.input_text(MaterialLocators.CATEGORY_SELECT,edit_data["category"] + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)
        # 保存修改
        self.click(MaterialLocators.EDIT_CONFIRM_BUTTON)
        # 关闭编辑窗口
        self.click(MaterialLocators.CLOSE_BUTTON)
        time.sleep(0.5)

    def delete_material(self, delete_data : dict):
        """删除物料"""
        self.search_material(delete_data)
        self.click(MaterialLocators.CHECKBOX)
        self.click(MaterialLocators.DELETE_BUTTON)
        self.click(MaterialLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)


