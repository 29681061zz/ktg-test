import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.warehouse_management_locators.arrivalnotice_locators import ArrivalNoticeLocators

class ArrivalNotice(BasePage):
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
        try:
            column_mapping = {
                'code': 1, 'edit_code': 1,
                'name': 2, 'edit_name': 2,
                'pocode': 3,
                'date': 7,
                'vendorname':4,
            }

            # 一次性获取所有行
            time.sleep(0.5)
            rows = self.find_elements(ArrivalNoticeLocators.TABLE_ROWS, allow_empty=True)
            if not rows:
                return False
            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in arrivalnotice_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))
            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                match = True

                for field, col_index in check_fields:
                    expected_value = arrivalnotice_data[field]
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

    def add_arrivalnotice(self,add_data : dict):
        # 点击新增
        self.click(ArrivalNoticeLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_CODE_INPUT, add_data["code"])
        self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_NAME_INPUT, add_data["name"])
        if "pocode" in add_data:
            self.input_text(ArrivalNoticeLocators.ARRIVALNOTICE_POCODE, add_data["pocode"])
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

