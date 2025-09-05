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
    def search_material(self, search_data:dict):
        """搜索物料:param material_code: 物料编码:param material_name: 物料名称"""
        self.click(MaterialLocators.CLEAR_SEARCH_BUTTON)
        time.sleep(0.5)
        if "code" in search_data:
            self.input_text(MaterialLocators.SEARCH_CODE_INPUT, search_data["code"])
        if "name" in search_data:
            self.input_text(MaterialLocators.SEARCH_NAME_INPUT, search_data["name"])
        self.click(MaterialLocators.SEARCH_BUTTON)
        time.sleep(0.5)


    def is_material_exists(self, material_data : dict):
        """检查搜索结果中是否存在指定的物料编码或名称（精确匹配）"""
        try:
            rows = self.find_elements(MaterialLocators.TABLE_ROWS)
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                # 物料编码验证（第2列，索引1）
                if "code" in material_data:
                    code_cell = cells[1]
                    try:
                        button = code_cell.find_element(By.TAG_NAME, "button")
                        span = button.find_element(By.TAG_NAME, "span")
                        actual_code = span.text.strip()
                    except:
                        actual_code = code_cell.text.strip()
                    if actual_code != material_data["code"]:

                        continue
                # 物料编码修改后验证（第2列，索引1）
                if "edit_code" in material_data:
                    code_cell = cells[1]
                    try:
                        button = code_cell.find_element(By.TAG_NAME, "button")
                        span = button.find_element(By.TAG_NAME, "span")
                        actual_code = span.text.strip()
                    except:
                        actual_code = code_cell.text.strip()
                    if actual_code != material_data["edit_code"]:
                        continue
                # 物料名称验证（第3列，索引2）
                if "name" in material_data and len(cells) > 2:
                    name_cell = cells[2]
                    try:
                        name_div = name_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
                        actual_name = name_div.text.strip()
                    except:
                        actual_name = name_cell.text.strip()
                    if actual_name != material_data["name"]:
                        continue
                # 物料修改后名称验证（第3列，索引2）
                if "edit_name" in material_data and len(cells) > 2:
                    print(1231231)
                    name_cell = cells[2]
                    try:
                        name_div = name_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
                        actual_name = name_div.text.strip()
                    except:
                        actual_name = name_cell.text.strip()
                    if actual_name != material_data["edit_name"]:
                        continue
                # 物料规格型号验证（第4列，索引3）
                if "specification" in material_data and len(cells) > 3:
                    specification_cell = cells[3]
                    try:
                        specification_div = specification_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
                        actual_specification= specification_div.text.strip()
                    except:
                        actual_specification = specification_cell.text.strip()
                    if actual_specification != material_data["specification"]:
                        continue
                # 物料单位型号验证（第5列，索引4）
                if "unit" in material_data and len(cells) > 4:
                    print(111)
                    unit_cell = cells[4]
                    try:
                        unit_div = unit_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
                        actual_unit = unit_div.text.strip()
                    except:
                        actual_unit = unit_cell.text.strip()
                    if actual_unit != material_data["unit"]:
                        continue
                # 物料分类验证（第7列，索引6）
                if "category" in material_data and len(cells) > 6:
                    category_cell = cells[6]
                    try:
                        category_div = category_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
                        actual_category = category_div.text.strip()
                    except:
                        actual_category = category_cell.text.strip()
                    if actual_category != material_data["category"]:
                        continue
                return True
            return False
        except Exception as e:
            print(f"检查物料存在时出错: {e}")
            return False

    def add_material(self,material_data : dict):
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
        self.click(MaterialLocators.ADD_CONFIRM_BUTTON)
        self.click(MaterialLocators.CLOSE_BUTTON)

    def edit_material(self, new_data: dict):
        """编辑物料信息:param new_data: 新的物料数据字典，必须包含material_code"""
        # 搜索要编辑的物料
        self.search_material(new_data)

        # 直接点击编辑按钮（假设搜索后编辑按钮可见）
        self.click(MaterialLocators.EDIT_BUTTON)
        # 编辑物料信息
        if "edit_code" in new_data:
            self.input_text(MaterialLocators.MATERIAL_CODE_INPUT, new_data["edit_code"])
        if "edit_name" in new_data:
            self.input_text(MaterialLocators.MATERIAL_NAME_INPUT, new_data["edit_name"])
        if "unit" in new_data:
            self.select_option(MaterialLocators.UNIT_SELECT, new_data["unit"])
        if "category" in new_data:
            self.input_text(MaterialLocators.CATEGORY_SELECT, new_data["category"])
            time.sleep(0.5)
            self.find(MaterialLocators.CATEGORY_SELECT).send_keys(Keys.ENTER)
        # 保存修改
        self.click(MaterialLocators.EDIT_CONFIRM_BUTTON)
        # 关闭编辑窗口
        self.click(MaterialLocators.CLOSE_BUTTON)
        time.sleep(0.5)
