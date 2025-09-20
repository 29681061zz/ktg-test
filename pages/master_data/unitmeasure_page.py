import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.unitmeasure_locators import UnitmeasureLocators

class UnitmeasurePage(BasePage):
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
        try:
            column_mapping = {
                'code': 1, 'edit_code': 1,
                'name': 2, 'edit_name': 2,
                'is_main_unit': 3,
                'conversion': 4,
            }

            # 一次性获取所有行
            rows = self.find_elements(UnitmeasureLocators.TABLE_ROWS, allow_empty=True)
            if not rows:
                return False
            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in unit_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))
            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                match = True

                for field, col_index in check_fields:
                    expected_value = unit_data[field]
                    cell_text = self._get_cell_text(cells[col_index])
                    if cell_text != expected_value:
                        match = False
                        break
                if match:
                    return True
            return False
        except Exception as e:
            print(f"检查单位存在时出错: {e}")
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

