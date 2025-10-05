import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.warehouse_management_locators.itemrecpt_locators import ItemRecptLocators

class ItemRecptPage(BasePage):
    """到货通知页面对象封装到货通知页面的所有操作和断言方法"""
    # -------------------- 搜索操作 --------------------
    def search_itemrecpt(self, search_data:dict):
        """仓库编码和仓库名称"""
        self.click(ItemRecptLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(ItemRecptLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(ItemRecptLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(ItemRecptLocators.SEARCH_BUTTON)
        time.sleep(0.5)

    def is_itemrecpt_exists(self, itemrecpt_data: dict):
        """检查指定的仓库是否存在（精确匹配）"""
        column_mapping = {
            'code': 1, 'edit_code': 1,
            'name': 2, 'edit_name': 2,
            'pocode': 5,
            'date': 4,
            'vendorname':3,
        }
        return self.is_record_exists(column_mapping, itemrecpt_data, ItemRecptLocators.TABLE_ROWS)

    def add_itemrecpt(self,add_data : dict):
        # 点击新增
        self.click(ItemRecptLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(ItemRecptLocators.ITEMRECPT_CODE_INPUT, add_data["code"])
        self.input_text(ItemRecptLocators.ITEMRECPT_NAME_INPUT, add_data["name"])
        #选择供应商
        self.click(ItemRecptLocators.VENDOR_SELECT)
        self.input_text(ItemRecptLocators.VENDOR_NAME,add_data["vendorname"])
        self.click(ItemRecptLocators.VENDOR_SEARCH)
        self.click(ItemRecptLocators.SELECT_VENDOR_BUTTON)
        self.click(ItemRecptLocators.SELECT_VENDOR_CONFIRM)
        if "date" in add_data:
            self.input_text(ItemRecptLocators.ITEMRECPT_DATE_INPUT, add_data["date"])
        if "noticecode" in add_data:
            # 选择供到货通知单
            self.click(ItemRecptLocators.NOTICECODE_SELECT)
            self.click(ItemRecptLocators.NOTICECODE_SELECT_STATUS)
            self.click(ItemRecptLocators.NOTICECODE_STATUS)
            self.input_text(ItemRecptLocators.NOTICECODE_CODE,add_data["noticecode"])
            self.click(ItemRecptLocators.NOTICECODE_SEARCH)
            self.click(ItemRecptLocators.SELECT_NOTICECODE_BUTTON)
            self.click(ItemRecptLocators.SELECT_NOTICECODE_CONFIRM)
        if "pocode" in add_data:
            self.input_text(ItemRecptLocators.ITEMRECPT_POCODE, add_data["pocode"])
        #点击保存回到初始的设置页面
        self.click(ItemRecptLocators.ADD_SAVE_BUTTON)
        time.sleep(0.5)

    def edit_itemrecpt(self, edit_data: dict):
        """编辑仓库信息:param edit_data: 新的仓库数据字典，必须包含itemrecpt_code"""
        # 搜索要编辑的仓库
        self.search_itemrecpt(edit_data)
        self.click(ItemRecptLocators.CHECKBOX)
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(ItemRecptLocators.EDIT_BUTTON)
        # 编辑仓库信息
        if "edit_code" in edit_data:
            self.input_text(ItemRecptLocators.ITEMRECPT_CODE_INPUT, edit_data["edit_code"])
        if "edit_name" in edit_data:
            self.input_text(ItemRecptLocators.ITEMRECPT_NAME_INPUT, edit_data["edit_name"])
        if "date" in edit_data:
            self.input_text(ItemRecptLocators.ITEMRECPT_DATE_INPUT, edit_data["date"])
        if "vendorname" in edit_data:
            self.click(ItemRecptLocators.VENDOR_SELECT)
            self.input_text(ItemRecptLocators.VENDOR_NAME, edit_data["vendorname"])
            self.click(ItemRecptLocators.VENDOR_SEARCH)
            self.click(ItemRecptLocators.SELECT_VENDOR_BUTTON)
            self.click(ItemRecptLocators.SELECT_VENDOR_CONFIRM)
        if "noticecode" in edit_data:
            # 选择供到货通知单
            self.click(ItemRecptLocators.NOTICECODE_SELECT)
            self.input_text(ItemRecptLocators.NOTICECODE_CODE,edit_data["noticecode"])
            self.click(ItemRecptLocators.NOTICECODE_SEARCH)
            self.click(ItemRecptLocators.SELECT_NOTICECODE_BUTTON)
            self.click(ItemRecptLocators.SELECT_NOTICECODE_CONFIRM)
        if "pocode" in edit_data:
            self.input_text(ItemRecptLocators.ITEMRECPT_POCODE, edit_data["pocode"])
        # 保存修改
        self.click(ItemRecptLocators.EDIT_SAVE_BUTTON)
        time.sleep(0.5)

    def delete_itemrecpt(self, delete_data : dict):
        """删除仓库"""
        self.search_itemrecpt(delete_data)
        self.click(ItemRecptLocators.CHECKBOX)
        self.click(ItemRecptLocators.DELETE_BUTTON)
        self.click(ItemRecptLocators.DELETE_CONFIRM_BUTTON)
        time.sleep(0.5)

