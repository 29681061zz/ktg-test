import time
from selenium.webdriver import Keys
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .material_management_locators import  MaterialLocators

class MaterialManagementPage(BasePage):
    """物料管理页面对象封装物料管理页面的所有操作和断言方法"""
    def __init__(self, driver):
        super().__init__(driver)

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

    def is_material_exists(self, material_data: dict):
        """检查指定的物料是否存在（精确匹配）"""
        try:
            column_mapping = {
                'code': 1, 'edit_code': 1,
                'name': 2, 'edit_name': 2,
                'specification': 3,
                'unit': 4,
                'category': 6
            }

            # 一次性获取所有行
            rows = self.find_elements(MaterialLocators.TABLE_ROWS, allow_empty=True)
            if not rows:
                return False

            # 预先处理需要检查的字段和列索引
            check_fields = []
            for field in material_data:
                if field in column_mapping:
                    check_fields.append((field, column_mapping[field]))
            for row in rows:
                # 一次性获取所有单元格
                cells = row.find_elements(By.TAG_NAME, "td")
                match = True

                for field, col_index in check_fields:
                    expected_value = material_data[field]
                    cell_text = self._get_cell_text(cells[col_index])
                    if cell_text != expected_value:
                        match = False
                        break
                if match:
                    return True
            return False
        except Exception as e:
            print(f"检查物料存在时出错: {e}")
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

    # def is_material_exists(self, material_data : dict):
    #     """检查指定的物料是否存在（精确匹配）"""
    #     try:
    #         rows = self.find_elements(MaterialLocators.TABLE_ROWS)
    #         for row in rows:
    #             cells = row.find_elements(By.TAG_NAME, "td")
    #             # 物料编码验证（第2列，索引1）
    #             if "code" in material_data:
    #                 code_cell = cells[1]
    #                 try:
    #                     button = code_cell.find_element(By.TAG_NAME, "button")
    #                     span = button.find_element(By.TAG_NAME, "span")
    #                     actual_code = span.text.strip()
    #                 except:
    #                     actual_code = code_cell.text.strip()
    #                 if actual_code != material_data["code"]:
    #                     continue
    #             # 物料编码修改后验证（第2列，索引1）
    #             if "edit_code" in material_data:
    #                 code_cell = cells[1]
    #                 try:
    #                     button = code_cell.find_element(By.TAG_NAME, "button")
    #                     span = button.find_element(By.TAG_NAME, "span")
    #                     actual_code = span.text.strip()
    #                 except:
    #                     actual_code = code_cell.text.strip()
    #                 if actual_code != material_data["edit_code"]:
    #                     continue
    #             # 物料名称验证（第3列，索引2）
    #             if "name" in material_data and len(cells) > 2:
    #                 name_cell = cells[2]
    #                 try:
    #                     name_div = name_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
    #                     actual_name = name_div.text.strip()
    #                 except:
    #                     actual_name = name_cell.text.strip()
    #                 if actual_name != material_data["name"]:
    #                     continue
    #             # 物料修改后名称验证（第3列，索引2）
    #             if "edit_name" in material_data and len(cells) > 2:
    #                 print(1231231)
    #                 name_cell = cells[2]
    #                 try:
    #                     name_div = name_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
    #                     actual_name = name_div.text.strip()
    #                 except:
    #                     actual_name = name_cell.text.strip()
    #                 if actual_name != material_data["edit_name"]:
    #                     continue
    #             # 物料规格型号验证（第4列，索引3）
    #             if "specification" in material_data and len(cells) > 3:
    #                 specification_cell = cells[3]
    #                 try:
    #                     specification_div = specification_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
    #                     actual_specification= specification_div.text.strip()
    #                 except:
    #                     actual_specification = specification_cell.text.strip()
    #                 if actual_specification != material_data["specification"]:
    #                     continue
    #             # 物料单位验证（第5列，索引4）
    #             if "unit" in material_data and len(cells) > 4:
    #                 unit_cell = cells[4]
    #                 try:
    #                     unit_div = unit_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
    #                     actual_unit = unit_div.text.strip()
    #                 except:
    #                     actual_unit = unit_cell.text.strip()
    #                 if actual_unit != material_data["unit"]:
    #                     continue
    #             # 物料分类验证（第7列，索引6）
    #             if "category" in material_data and len(cells) > 6:
    #                 category_cell = cells[6]
    #                 try:
    #                     category_div = category_cell.find_element(By.CSS_SELECTOR, "div.cell.el-tooltip")
    #                     actual_category = category_div.text.strip()
    #                 except:
    #                     actual_category = category_cell.text.strip()
    #                 if actual_category != material_data["category"]:
    #                     continue
    #             return True
    #         return False
    #     except Exception as e:
    #         return False

    def add_material(self,add_data : dict):
        # 点击新增
        self.click(MaterialLocators.ADD_BUTTON)
        #输入必填项
        self.input_text(MaterialLocators.MATERIAL_CODE_INPUT, add_data["code"])
        self.input_text(MaterialLocators.MATERIAL_NAME_INPUT, add_data["name"])
        self.input_text(MaterialLocators.MATERIAL_SPECIFICATION_INPUT, add_data["specification"])
        self.select_option(MaterialLocators.UNIT_SELECT, add_data["unit"])
        self.input_text(MaterialLocators.CATEGORY_SELECT, add_data["category"]+ Keys.ENTER)
        #关闭批管理
        self.click(MaterialLocators.BATCH_MANAGEMENT_SWITCH)
        #点击确定，然后点击关闭，回到初始的料管理页面
        self.click(MaterialLocators.ADD_CONFIRM_BUTTON)
        self.click(MaterialLocators.CLOSE_BUTTON)
        time.sleep(0.5)

    def edit_material(self, edit_data: dict):
        """编辑物料信息:param edit_data: 新的物料数据字典，必须包含material_code"""
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
            self.input_text(MaterialLocators.CATEGORY_SELECT, edit_data["category"])
            time.sleep(0.5)
            self.find(MaterialLocators.CATEGORY_SELECT).send_keys(Keys.ENTER)
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


