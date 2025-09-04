import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from .material_management_locators import  MaterialLocators
from common.modal import ConfirmModal

class MaterialManagementPage(BasePage):
    """
    物料管理页面对象
    封装物料管理页面的所有操作和断言方法
    """
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.modal = ConfirmModal(driver)

    # -------------------- 搜索操作 --------------------
    def search_material(self, material_code: str = None, material_name: str = None) -> None:
        """搜索物料:param material_code: 物料编码:param material_name: 物料名称"""
        self.click(MaterialLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if material_code:
            self.input_text(MaterialLocators.SEARCH_CODE_INPUT, material_code)
        if material_name:
            self.input_text(MaterialLocators.SEARCH_NAME_INPUT, material_name)
        self.click(MaterialLocators.SEARCH_BUTTON)
        time.sleep(0.5)


    def is_material_exists(self, material_code: str = None, material_name: str = None) -> bool:
        """检查搜索结果中是否存在指定的物料编码或名称（精确匹配）"""
        try:
            rows = self.find_elements(MaterialLocators.TABLE_ROWS)
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                # 物料编码验证（第2列，索引1）
                if material_code:
                    code_cell = cells[1]
                    try:
                        button = code_cell.find_element(By.TAG_NAME, "button")
                        span = button.find_element(By.TAG_NAME, "span")
                        actual_code = span.text.strip()
                    except:
                        actual_code = code_cell.text.strip()

                    if actual_code == material_code:
                        return True

                # 物料名称验证（第3列，索引2）
                if material_name and len(cells) > 2:
                    name_cell = cells[2]
                    try:
                        name_div = name_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
                        actual_name = name_div.text.strip()
                    except:
                        actual_name = name_cell.text.strip()

                    if actual_name == material_name:
                        return True
            return False

        except Exception as e:
            print(f"检查物料存在时出错: {e}")
            return False

    def add_new_material(self,material_data:dict):
        # 点击新增
        self.click(MaterialLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(MaterialLocators.MATERIAL_CODE_INPUT, material_data["material_code"])
        self.input_text(MaterialLocators.MATERIAL_NAME_INPUT, material_data["material_name"])
        self.select_option(MaterialLocators.UNIT_SELECT, material_data["unit"])
        self.input_text(MaterialLocators.CATEGORY_SELECT, material_data["category"]+ Keys.ENTER)
        #关闭批管理
        self.click(MaterialLocators.BATCH_MANAGEMENT_SWITCH)
        #点击确定，然后点击关闭，回到初始的料管理页面
        self.click(MaterialLocators.CONFIRM_BUTTON)
        self.click(MaterialLocators.CLOSE_BUTTON)

    def edit_material(self, new_data: dict):
        """编辑物料信息
        :param new_data: 新的物料数据字典，必须包含material_code
        """
        # 搜索要编辑的物料
        self.search_material(material_code=new_data["material_code"])
        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        print(1)
        self.click(MaterialLocators.EDIT_BUTTON)
        print(2)

        # 编辑物料信息
        if "material_name" in new_data:
            self.clear_input(MaterialLocators.MATERIAL_NAME_INPUT)
            self.input_text(MaterialLocators.MATERIAL_NAME_INPUT, new_data["material_name"])
        if "unit" in new_data:
            self.select_option(MaterialLocators.UNIT_SELECT, new_data["unit"])
        if "category" in new_data:
            self.clear_input(MaterialLocators.CATEGORY_SELECT)
            self.input_text(MaterialLocators.CATEGORY_SELECT, new_data["category"] + Keys.ENTER)

        # 保存修改
        self.click(MaterialLocators.CONFIRM_BUTTON)
        time.sleep(0.5)
        # 关闭编辑窗口
        self.click(MaterialLocators.CLOSE_BUTTON)

    def get_success_message(self):
        """获取成功消息"""
        return self.get_text(MaterialLocators.SUCCESS_MESSAGE)
