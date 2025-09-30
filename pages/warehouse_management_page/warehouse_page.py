import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.warehouse_management_locators.warehouse_locators import WareHouseLocators

class WareHouse(BasePage):
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
        try:
            column_mapping = {
                'code': 1, 'edit_code': 1,
                'name': 2, 'edit_name': 2,
                'area': 4,
                'location': 3,
                'remark': 7,
            }

            # 一次性获取所有行
            time.sleep(0.5)
            rows = self.find_elements(WareHouseLocators.TABLE_ROWS, allow_empty=True)
            if not rows:
                return False
            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in warehouse_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))
            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                match = True

                for field, col_index in check_fields:
                    expected_value = warehouse_data[field]
                    cell_text = self._get_cell_text(cells[col_index])
                    if cell_text != expected_value:
                        match = False
                        break
                if match:
                    return True
            return False
        except Exception as e:
            print(f"检查仓库存在时出错: {e}")
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

    def add_warehouse(self,add_data : dict):
        # 点击新增
        self.click(WareHouseLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(WareHouseLocators.WAREHOUSE_CODE_INPUT, add_data["code"])
        self.input_text(WareHouseLocators.WAREHOUSE_NAME_INPUT, add_data["name"])
        if "location" in add_data:
            self.input_text(WareHouseLocators.WAREHOUSE_LOCATION, add_data["location"])
        if "area" in add_data:
            self.input_text(WareHouseLocators.WAREHOUSE_LOCATION, add_data["area"])
        if "remark" in add_data:
            self.input_text(WareHouseLocators.WAREHOUSE_LOCATION, add_data["remark"])
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
            self.input_text(WareHouseLocators.WAREHOUSE_LOCATION, edit_data["area"])
        if "remark" in edit_data:
            self.input_text(WareHouseLocators.WAREHOUSE_LOCATION, edit_data["remark"])
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

