import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.master_data_locators.workstation_locators import WorkstationLocators

class WorkStation(BasePage):
    """车间设置页面对象封装车间设置页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_workstation(self, search_data:dict):
        """车间编码和车间名称"""
        self.click(WorkstationLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(WorkstationLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(WorkstationLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(WorkstationLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_workstation_exists(self, workstation_data: dict):
        """检查指定的车间是否存在（精确匹配）"""
        try:
            column_mapping = {
                'code': 1, 'edit_code': 1,
                'name': 2, 'edit_name': 2,
                'workshop': 4,
                'process': 5,
            }

            # 一次性获取所有行
            rows = self.find_elements(WorkstationLocators.TABLE_ROWS, allow_empty=True)
            if not rows:
                return False
            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in workstation_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))
            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                match = True

                for field, col_index in check_fields:
                    expected_value = workstation_data[field]
                    cell_text = self._get_cell_text(cells[col_index])
                    if cell_text != expected_value:
                        match = False
                        break
                if match:
                    return True
            return False
        except Exception as e:
            print(f"检查车间存在时出错: {e}")
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
        """编辑车间信息:param edit_data: 新的车间数据字典，必须包含workstation_code"""
        # 搜索要编辑的车间
        self.search_workstation(edit_data)
        self.click(WorkstationLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(WorkstationLocators.EDIT_BUTTON)
        # 编辑车间信息
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
        """删除车间"""
        self.search_workstation(delete_data)
        self.click(WorkstationLocators.CHECKBOX)
        self.click(WorkstationLocators.DELETE_BUTTON)
        self.click(WorkstationLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

