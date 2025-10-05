import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.master_data_locators.unitmeasure_locators import UnitmeasureLocators

class UnitMeasurePage(BasePage):
    """单位管理页面对象封装单位管理页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_unit(self, search_data:dict):
        """单位编码和单位名称"""
        self.click(UnitmeasureLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(UnitmeasureLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(UnitmeasureLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(UnitmeasureLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_unit_exists(self, unit_data: dict):
        """检查指定的单位是否存在（精确匹配）"""
        column_mapping = {
            'code': 1, 'edit_code': 1,
            'name': 2, 'edit_name': 2,
            'is_main_unit': 3,
            'conversion': 4,
        }
        return self.is_record_exists(column_mapping, unit_data, UnitmeasureLocators.TABLE_ROWS)


    def add_unit(self,add_data : dict):
        # 点击新增
        self.click(UnitmeasureLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(UnitmeasureLocators.UNIT_CODE_INPUT, add_data["code"])
        self.input_text(UnitmeasureLocators.UNIT_NAME_INPUT, add_data["name"])
        if add_data["is_main_unit"] == "是":
            self.click(UnitmeasureLocators.MAIN_UNIT_YES)
        else:
            self.click(UnitmeasureLocators.MAIN_UNIT_NO)
            self.select_option(UnitmeasureLocators.SELECT_MAIN_UNIT, add_data["main_unit"])
            self.input_text(UnitmeasureLocators.CONVERSION_INPUT, add_data["conversion"])
        #点击确定，然后点击关闭，回到初始的料管理页面
        self.click(UnitmeasureLocators.ADD_CONFIRM_BUTTON)
        time.sleep(0.5)

    def select_option(self, select_locator, option_text):
        # 点击下拉框展开选项
        self.click(select_locator)
        # 构建选项定位器 - Element UI的选项结构
        option_locator = (By.XPATH,f"//li[contains(@class, 'el-select-dropdown__item') and span[text()='{option_text}']]")
        # 点击选项
        self.click(option_locator)

    def edit_unit(self, edit_data: dict):
        """编辑单位信息:param edit_data: 新的单位数据字典，必须包含unit_code"""
        # 搜索要编辑的单位
        self.search_unit(edit_data)
        self.click(UnitmeasureLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(UnitmeasureLocators.EDIT_BUTTON)
        # 编辑单位信息
        if "edit_code" in edit_data:
            self.input_text(UnitmeasureLocators.UNIT_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(UnitmeasureLocators.UNIT_NAME_INPUT, edit_data["edit_name"])
        if "is_main_unit" in edit_data :
            if edit_data["is_main_unit"] == "是":
                self.click(UnitmeasureLocators.MAIN_UNIT_YES)
            else:
                self.click(UnitmeasureLocators.MAIN_UNIT_NO)
                if "main_unit" in edit_data:
                    self.select_option(UnitmeasureLocators.SELECT_MAIN_UNIT, edit_data["main_unit"])
                if "conversion" in edit_data:
                    self.input_text(UnitmeasureLocators.CONVERSION_INPUT, edit_data["conversion"])
        # 保存修改
        self.click(UnitmeasureLocators.EDIT_CONFIRM_BUTTON)
        time.sleep(0.5)


    def delete_unit(self, delete_data : dict):
        """删除单位"""
        self.search_unit(delete_data)
        self.click(UnitmeasureLocators.CHECKBOX)
        self.click(UnitmeasureLocators.DELETE_BUTTON)
        self.click(UnitmeasureLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

