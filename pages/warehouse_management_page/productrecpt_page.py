import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.warehouse_management_locators.productrecpt_locators import ProductRecptLocators

class ProductRecptPage(BasePage):
    """产品入库页面对象封装产品入库页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_productrecpt(self, search_data:dict):
        """产品入库编码和产品入库名称"""
        self.click(ProductRecptLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(ProductRecptLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(ProductRecptLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(ProductRecptLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_productrecpt_exists(self, productrecpt_data: dict):
        """检查指定产品入库是否存在（精确匹配）"""
        try:
            column_mapping = {
                'code': 1, 'edit_code': 1,
                'name': 2, 'edit_name': 2,
                'pocode': 5,
                'date': 4,
                'vendorname':3,
            }

            # 一次性获取所有行
            time.sleep(0.5)
            rows = self.find_elements(ProductRecptLocators.TABLE_ROWS, allow_empty=True)
            if not rows:
                return False
            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in productrecpt_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))
            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                match = True

                for field, col_index in check_fields:
                    expected_value = productrecpt_data[field]
                    cell_text = self._get_cell_text(cells[col_index])
                    if cell_text != expected_value:
                        match = False
                        break
                if match:
                    return True
            return False
        except Exception as e:
            print(f"检查产品入库存在时出错: {e}")
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

    def add_productrecpt(self,add_data : dict):
        # 点击新增
        self.click(ProductRecptLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(ProductRecptLocators.PRODUCRECPT_CODE_INPUT, add_data["code"])
        if "name" in add_data:
            self.input_text(ProductRecptLocators.PRODUCRECPT_NAME_INPUT, add_data["name"])
        if "date" in add_data:
            self.input_text(ProductRecptLocators.PRODUCRECPT_DATE_INPUT, add_data["date"])
        if "workordercode" in add_data:
            # 选择生产工单
            self.click(ProductRecptLocators.WORKORDERCODE_SELECT)
            self.input_text(ProductRecptLocators.WORKORDERCODE_CODE,add_data["workordercode"])
            self.click(ProductRecptLocators.WORKORDERCODE_SEARCH)
            self.click(ProductRecptLocators.SELECT_WORKORDERCODE_BUTTON)
            self.click(ProductRecptLocators.SELECT_WORKORDERCODE_CONFIRM)
        #点击保存回到初始的设置页面
        self.click(ProductRecptLocators.ADD_SAVE_BUTTON)
        time.sleep(0.5)

    def edit_productrecpt(self, edit_data: dict):
        """编辑产品入库信息:param edit_data: 新产品入库数据字典，必须包含productrecpt_code"""
        # 搜索要编辑产品入库
        self.search_productrecpt(edit_data)
        self.click(ProductRecptLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(ProductRecptLocators.EDIT_BUTTON)
        # 编辑产品入库信息
        if "edit_code" in edit_data:
            self.input_text(ProductRecptLocators.PRODUCRECPT_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(ProductRecptLocators.PRODUCRECPT_NAME_INPUT, edit_data["edit_name"])
        if "date" in edit_data:
            self.input_text(ProductRecptLocators.PRODUCRECPT_DATE_INPUT, edit_data["date"])
        if "workordercode" in edit_data:
            # 选择生产工单
            self.click(ProductRecptLocators.WORKORDERCODE_SELECT)
            self.input_text(ProductRecptLocators.WORKORDERCODE_CODE,edit_data["workordercode"])
            self.click(ProductRecptLocators.WORKORDERCODE_SEARCH)
            self.click(ProductRecptLocators.SELECT_WORKORDERCODE_BUTTON)
            self.click(ProductRecptLocators.SELECT_WORKORDERCODE_CONFIRM)
        # 保存修改
        self.click(ProductRecptLocators.EDIT_SAVE_BUTTON)
        time.sleep(0.5)

    def delete_productrecpt(self, delete_data : dict):
        """删除产品入库"""
        self.search_productrecpt(delete_data)
        self.click(ProductRecptLocators.CHECKBOX)
        self.click(ProductRecptLocators.DELETE_BUTTON)
        self.click(ProductRecptLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

