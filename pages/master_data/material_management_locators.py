# pages/master_data/material_management_locators.py
from selenium.webdriver.common.by import By

class MaterialLocators:
    """物料管理页面元素定位器"""
    # 页面标识
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'物料管理')]")

    # 搜索区域
    SEARCH_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料编码'])[1]")
    SEARCH_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料名称'])[1]")
    SEARCH_BUTTON = (By.XPATH,"//button[contains(@class, 'el-button--primary') and contains(@class, 'el-button--mini')]//span[text()='搜索']")
    CLEAR_SEARCH_BUTTON = (By.XPATH, "//button[.//span[text()='重置']]")

    #表单元素
    MATERIAL_CODE_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料编码'])[2]")
    MATERIAL_NAME_INPUT = (By.XPATH, "(//input[@placeholder='请输入物料名称'])[2]")
    MATERIAL_SPECIFICATION_INPUT = (By.XPATH, "//textarea[@placeholder='请输入规格型号']")
    UNIT_SELECT = (By.XPATH, "//label[text()='单位']/following-sibling::div//input[@class='el-input__inner']")
    CATEGORY_SELECT = (By.XPATH, "//label[text()='物料/产品分类']/following-sibling::div//input[@class='vue-treeselect__input']")

    ADD_CONFIRM_BUTTON = (By.XPATH, "(//button//span[text()='确 定'])[2]")#新增物料页面的确定键
    EDIT_CONFIRM_BUTTON = (By.XPATH, "(//button//span[text()='确 定'])[3]")#修改物料页面的确定键
    DELETE_CONFIRM_BUTTON = (By.XPATH, "(//button//span[contains(text(),'确定')])[2]")#删除物料页面的确定键
    CLOSE_BUTTON = (By.XPATH, "//button//span[text()='关 闭']")

    BATCH_MANAGEMENT_SWITCH = (By.XPATH,"//label[contains(text(), '批次管理')]/following-sibling::div//div[@role='switch']")
    CHECKBOX = (By.XPATH, "(//span//span[@class='el-checkbox__inner'])[2]")#复选框
    # 操作按钮
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'el-button--primary') and .//span[text()='新增']]")
    EDIT_BUTTON = (By.XPATH, "(//button//span[text()='修改'])[1]")
    DELETE_BUTTON = (By.XPATH, "(//button//span[text()='删除'])[1]")
    EXPORT_BUTTON = (By.ID, "btn-export")
    BATCH_DELETE_BUTTON = (By.ID, "btn-batch-delete")
    BATCH_EXPORT_BUTTON = (By.ID, "btn-batch-export")

    # 表格元素
    MATERIAL_TABLE = (By.ID, "material-table")
    TABLE_ROWS = (By.CSS_SELECTOR, "tr.el-table__row")
    TABLE_CELLS =(By.TAG_NAME, "td")
    NO_DATA_TEXT = (By.XPATH, "//span[text()='暂无数据']")
    ROW_CHECKBOX = (By.CSS_SELECTOR, "input[type='checkbox']")
    SELECT_ALL_CHECKBOX = (By.ID, "select-all")

    # 弹窗

    ADD_DIALOG = (By.ID, "add-material-dialog")
    EDIT_DIALOG = (By.ID, "edit-material-dialog")

    # 状态元素
    LOADING_INDICATOR = (By.ID, "loading-spinner")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "el-message__content")

    # 分页元素
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, "next-page")
    PREV_PAGE_BUTTON = (By.CLASS_NAME, "prev-page")
    PAGE_INFO = (By.CLASS_NAME, "page-info")